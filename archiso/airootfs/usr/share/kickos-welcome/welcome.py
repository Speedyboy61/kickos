#!/usr/bin/env python3
# KickOS Welcome App — launches on first boot

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Gio
import os
import subprocess

CSS = """
window {
    background-color: #0d0d1a;
    color: #ffffff;
}
button {
    background-color: #6c5ce7;
    color: #ffffff;
    border-radius: 6px;
    padding: 8px 20px;
    font-weight: 600;
}
button:hover {
    background-color: #7c6cf7;
}
button:disabled {
    background-color: #1a1a3a;
    color: #555;
}
label.title {
    font-size: 24px;
    font-weight: 800;
}
label.subtitle {
    color: #a89ff7;
    font-size: 14px;
}
"""

PAGES = [
    {
        "title": "Welcome to KickOS",
        "desc": "Your gaming Linux distribution is ready.\nLet's get everything set up.",
    },
    {
        "title": "GPU Drivers",
        "desc": "Detecting your graphics hardware...",
    },
    {
        "title": "Gaming Setup",
        "desc": "Configure Proton, AUR, and gaming tools.",
    },
    {
        "title": "Controllers",
        "desc": "Detect and test your game controllers.",
    },
    {
        "title": "You're Ready!",
        "desc": "Everything is set up. Time to game!",
    },
]


class WelcomeApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="dev.kickos.welcome")
        self.current_page = 0
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        if not os.path.exists("/etc/kickos-firstboot"):
            return

        win = Adw.ApplicationWindow(application=app)
        win.set_title("Welcome to KickOS")
        win.set_default_size(600, 450)

        css = Gtk.CssProvider()
        css.load_from_data(CSS.encode())
        Gtk.StyleContext.add_provider_for_display(
            win.get_display(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)
        win.set_content(self.stack)

        for i, page in enumerate(PAGES):
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
            box.set_halign(Gtk.Align.CENTER)
            box.set_valign(Gtk.Align.CENTER)
            box.set_margin_top(40)
            box.set_margin_bottom(40)
            box.set_margin_start(40)
            box.set_margin_end(40)

            title = Gtk.Label(label=page["title"])
            title.set_markup(f"<span size='xx-large' weight='bold'>{page['title']}</span>")
            box.append(title)

            desc = Gtk.Label(label=page["desc"])
            desc.set_markup(f"<span color='#a89ff7'>{page['desc']}</span>")
            desc.set_wrap(True)
            desc.set_justify(Gtk.Justification.CENTER)
            box.append(desc)

            self.stack.add_titled(box, str(i), page["title"])

        nav_box = Gtk.Box(spacing=8)
        nav_box.set_halign(Gtk.Align.CENTER)
        nav_box.set_margin_bottom(20)

        self.back_btn = Gtk.Button(label="Back")
        self.back_btn.connect("clicked", self.on_back)
        nav_box.append(self.back_btn)

        self.dots = Gtk.Box(spacing=8)
        self.dot_widgets = []
        for _ in PAGES:
            dot = Gtk.Label(label="○")
            dot.set_markup("<span size='large'>○</span>")
            self.dots.append(dot)
            self.dot_widgets.append(dot)
        nav_box.append(self.dots)

        self.next_btn = Gtk.Button(label="Next")
        self.next_btn.connect("clicked", self.on_next)
        nav_box.append(self.next_btn)

        self.stack.set_visible_child_name("0")
        self.update_nav()
        win.present()

    def update_nav(self):
        self.back_btn.set_sensitive(self.current_page > 0)
        if self.current_page == len(PAGES) - 1:
            self.next_btn.set_label("Finish")
        else:
            self.next_btn.set_label("Next")
        for i, dot in enumerate(self.dot_widgets):
            if i <= self.current_page:
                dot.set_markup(f"<span size='large' color='#6c5ce7'>●</span>")
            else:
                dot.set_markup(f"<span size='large' color='#333'>○</span>")

    def on_back(self, btn):
        if self.current_page > 0:
            self.current_page -= 1
            self.stack.set_visible_child_name(str(self.current_page))
            self.update_nav()

    def on_next(self, btn):
        if self.current_page < len(PAGES) - 1:
            self.current_page += 1
            self.stack.set_visible_child_name(str(self.current_page))
            self.update_nav()
        else:
            # Finish — remove first-boot flag
            os.remove("/etc/kickos-firstboot")
            self.get_active_window().close()


def main():
    app = WelcomeApp()
    app.run()


if __name__ == "__main__":
    main()

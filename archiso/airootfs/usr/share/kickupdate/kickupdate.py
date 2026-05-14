#!/usr/bin/env python3
# KickUpdate — KickOS Update Manager (GTK4)

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Pango
import subprocess
import os
import threading

CSS = """
window {
    background-color: #0d0d1a;
    color: #ffffff;
}
headerbar {
    background-color: #1a1a3a;
    color: #ffffff;
}
button {
    background-color: #6c5ce7;
    color: #ffffff;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
}
button:hover {
    background-color: #7c6cf7;
}
button.refresh {
    background-color: #1a1a3a;
    border: 1px solid #6c5ce7;
    color: #a89ff7;
}
row {
    background-color: #1a1a3a;
    color: #ffffff;
    border-radius: 6px;
    margin: 2px 0;
}
label.warning {
    color: #ff6b6b;
    font-size: 0.85em;
}
"""

class KickUpdateApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="dev.kickos.update")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        win = Adw.ApplicationWindow(application=app)
        win.set_title("KickUpdate — KickOS Update Manager")
        win.set_default_size(700, 500)

        css = Gtk.CssProvider()
        css.load_from_data(CSS.encode())
        Gtk.StyleContext.add_provider_for_display(
            win.get_display(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        win.set_content(box)

        header = Adw.HeaderBar()
        box.append(header)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        main_box.set_margin_top(16)
        main_box.set_margin_bottom(16)
        main_box.set_margin_start(16)
        main_box.set_margin_end(16)
        box.append(main_box)

        label = Gtk.Label(label="Pending Updates")
        label.set_markup("<span size='x-large' weight='bold'>Pending Updates</span>")
        label.set_halign(Gtk.Align.START)
        main_box.append(label)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        scrolled.set_child(self.listbox)
        main_box.append(scrolled)

        btn_box = Gtk.Box(spacing=8)
        btn_box.set_halign(Gtk.Align.END)
        btn_box.set_margin_top(12)

        refresh_btn = Gtk.Button(label="Refresh")
        refresh_btn.add_css_class("refresh")
        refresh_btn.connect("clicked", self.on_refresh)
        btn_box.append(refresh_btn)

        snapshot_btn = Gtk.Button(label="Take Snapshot")
        snapshot_btn.add_css_class("refresh")
        snapshot_btn.connect("clicked", self.on_snapshot)
        btn_box.append(snapshot_btn)

        update_btn = Gtk.Button(label="Update All")
        update_btn.connect("clicked", self.on_update_all)
        btn_box.append(update_btn)

        main_box.append(btn_box)

        win.present()
        self.refresh_updates()

    def refresh_updates(self):
        while self.listbox.get_first_child():
            self.listbox.remove(self.listbox.get_first_child())

        detected = self.detect_updates()
        if not detected:
            row = Adw.ActionRow()
            row.set_title("No updates available")
            self.listbox.append(row)
            return

        for pkg, old, new in detected:
            row = Adw.ActionRow()
            row.set_title(f"{pkg}")
            row.set_subtitle(f"{old} → {new}")
            if pkg in ("linux-zen", "nvidia", "mesa", "wine", "linux-image-amd64"):
                warning = Gtk.Label(label="System restart required")
                warning.add_css_class("warning")
                row.add_suffix(warning)
            self.listbox.append(row)

    def detect_updates(self):
        output = subprocess.run(
            ["checkupdates"], capture_output=True, text=True, timeout=30
        )
        if output.returncode != 0:
            return []
        updates = []
        for line in output.stdout.strip().split("\n"):
            if "->" in line:
                parts = line.split("->")
                pkg = parts[0].strip().rsplit(" ", 1)[0]
                old = parts[0].strip().rsplit(" ", 1)[-1]
                new = parts[1].strip()
                updates.append((pkg, old, new))
        return updates

    def on_refresh(self, btn):
        self.refresh_updates()

    def on_snapshot(self, btn):
        threading.Thread(target=self.take_snapshot, daemon=True).start()

    def take_snapshot(self):
        subprocess.run(["timeshift", "--create", "--comments", "Pre-update snapshot"])

    def on_update_all(self, btn):
        threading.Thread(target=self.run_updates, daemon=True).start()

    def run_updates(self):
        # Auto snapshot before kernel/gpu driver updates
        output = subprocess.run(
            ["checkupdates"], capture_output=True, text=True, timeout=30
        )
        dangerous = ["linux", "nvidia", "mesa", "wine"]
        if any(d in output.stdout for d in dangerous):
            subprocess.run(["timeshift", "--create", "--comments", "Pre-update snapshot"])

        result = subprocess.run(
            ["pkexec", "pacman", "-Syu", "--noconfirm"],
            capture_output=True, text=True, timeout=600,
        )
        GLib.idle_add(self.refresh_updates)
        subprocess.run(["notify-send", "KickOS Updates", "System updated successfully"])


def main():
    app = KickUpdateApp()
    app.run()


if __name__ == "__main__":
    main()

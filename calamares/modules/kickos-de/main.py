#!/usr/bin/env python3
# KickOS Desktop Environment selection module for Calamares

import calamares

DESKTOPS = [
    {
        "id": "kde",
        "name": "KDE Plasma",
        "desc": "Full-featured desktop, great for gaming and daily use. Best for most users.",
        "tags": ["Beginner friendly"],
        "default": True,
    },
    {
        "id": "hyprland",
        "name": "Hyprland",
        "desc": "Wayland compositor with smooth animations. Highly customizable, intermediate users.",
        "tags": ["Riceable"],
    },
    {
        "id": "i3",
        "name": "i3",
        "desc": "Minimal tiling window manager. Keyboard-driven, very fast, steep learning curve.",
        "tags": ["Lightweight"],
    },
    {
        "id": "niri",
        "name": "Niri",
        "desc": "Experimental scrollable Wayland WM. Unique column layout, early adopters only.",
        "tags": ["Experimental"],
    },
    {
        "id": "cutefish",
        "name": "Cutefish",
        "desc": "macOS-inspired desktop. Clean, minimal, easy to use.",
        "tags": ["macOS-style"],
    },
]


def run():
    names = [d["name"] for d in DESKTOPS]
    descs = [d["desc"] for d in DESKTOPS]
    tags = [", ".join(d["tags"]) for d in DESKTOPS]

    selection = calamares.job.pretty(
        names,
        descs,
        tags,
        "Desktop Environment",
        "Select your preferred desktop environment.",
    )

    with open("/tmp/kickos-de-selection", "w") as f:
        f.write(selection)

    return None

#!/usr/bin/env python3

import os
import subprocess
import calamares

def read_selection(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read().strip()

def install_packages(packages):
    if not packages:
        return
    subprocess.run(["pacman", "-S", "--noconfirm"] + packages)

def run():
    de = read_selection("/tmp/kickos-de-selection")
    gaming = read_selection("/tmp/kickos-gaming-selection")
    bootloader = read_selection("/tmp/kickos-bootloader-selection")

    de_packages = {
        "kde": ["plasma-desktop", "kdeplasma-addons", "sddm", "dolphin", "konsole", "kate", "discover", "packagekit-qt6"],
        "budgie": ["budgie-desktop", "budgie-control-center", "gnome-terminal"],
        "cinnamon": ["cinnamon", "gnome-terminal"],
        # "cosmic": ["cosmic", "cosmic-ext"], # from AUR
        "hyprland": ["hyprland", "waybar", "wofi", "dunst", "hyprpaper"],
        "i3": ["i3-wm", "i3status", "dmenu", "st"],
        "niri": ["niri"],
        "cutefish": ["cutefish"],
    }

    if de in de_packages:
        install_packages(de_packages[de])

    gaming_packages_map = {
        "steam": ["steam"],
        "lutris": ["lutris"],
        "heroic": ["heroic-games-launcher-bin"],
        "mangohud": ["mangohud", "lib32-mangohud"],
        "bottles": ["bottles"],
        "corectrl": ["corectrl"],
        "retroarch": ["retroarch"],
        "prismlauncher": ["prismlauncher"],
    }

    if gaming:
        for line in gaming.split("\n"):
            line = line.strip()
            if line in gaming_packages_map:
                install_packages(gaming_packages_map[line])

    subprocess.run(["/usr/local/bin/kick-hardware-detect"])
    subprocess.run(["systemctl", "enable", "kicknotify.service"])
    subprocess.run(["systemctl", "enable", "timeshift", "--now"])
    subprocess.run(["timeshift", "--create", "--comments", "First boot snapshot"])

    open("/etc/kickos-firstboot", "w").close()

    calamares.job.setprogress(1.0)
    return None

#!/usr/bin/env python3

import calamares

ALWAYS_INSTALLED = [
    {"id": "wine", "name": "Wine", "desc": "Run Windows applications on Linux."},
    {"id": "proton", "name": "Proton-GE", "desc": "Steam Play compatibility tool."},
    {"id": "kickboost", "name": "KickBoost", "desc": "KickOS FPS optimizer."},
    {"id": "vulkan", "name": "Vulkan Drivers", "desc": "GPU graphics drivers."},
    {"id": "gamemode", "name": "GameMode", "desc": "Feral Interactive game optimizations."},
]

OPTIONAL_PACKAGES = [
    {"id": "steam", "name": "Steam", "desc": "The premier PC gaming platform.", "default": True},
    {"id": "lutris", "name": "Lutris", "desc": "Game manager for all your platforms.", "default": True},
    {"id": "heroic", "name": "Heroic Games Launcher", "desc": "Epic Games and GOG alternative launcher.", "default": True},
    {"id": "mangohud", "name": "MangoHud", "desc": "Performance overlay for games.", "default": True},
    {"id": "bottles", "name": "Bottles", "desc": "Run Windows apps in isolated environments.", "default": False},
    {"id": "corectrl", "name": "CoreCtrl", "desc": "GPU and CPU performance control.", "default": False},
    {"id": "retroarch", "name": "RetroArch", "desc": "Emulator frontend for classic games.", "default": False},
    {"id": "prismlauncher", "name": "PrismLauncher", "desc": "Minecraft launcher with mod support.", "default": False},
]

def run():
    names = [p["name"] for p in OPTIONAL_PACKAGES]
    descs = [p["desc"] for p in OPTIONAL_PACKAGES]
    defaults = [p["default"] for p in OPTIONAL_PACKAGES]

    selections = calamares.job.pretty_checks(
        names, descs, defaults, "Gaming Packages", "Select optional gaming packages to install."
    )

    with open("/tmp/kickos-gaming-selection", "w") as f:
        for sel in selections:
            f.write(f"{sel}\n")

    return None

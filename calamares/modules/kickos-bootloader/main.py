#!/usr/bin/env python3
# KickOS Bootloader selection module for Calamares

import calamares

BOOTLOADERS = [
    {"id": "grub", "name": "GRUB", "desc": "Most compatible, works on all hardware.", "default": True},
    {"id": "refind", "name": "rEFInd", "desc": "Prettier boot menu, better for multi-boot setups.", "default": False},
]


def run():
    names = [b["name"] for b in BOOTLOADERS]
    descs = [b["desc"] for b in BOOTLOADERS]

    selection = calamares.job.pretty(
        names, descs, [], "Bootloader", "Select your preferred bootloader."
    )

    with open("/tmp/kickos-bootloader-selection", "w") as f:
        f.write(selection)

    return None

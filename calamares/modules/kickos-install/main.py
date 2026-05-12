#!/usr/bin/env python3
# KickOS Post-install configuration module for Calamares

import os
import subprocess
import calamares


def read_selection(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read().strip()


def run():
    de = read_selection("/tmp/kickos-de-selection")
    gaming = read_selection("/tmp/kickos-gaming-selection")
    bootloader = read_selection("/tmp/kickos-bootloader-selection")

    subprocess.run(["/usr/local/bin/kick-hardware-detect"])
    subprocess.run(["systemctl", "enable", "kicknotify.service"])
    subprocess.run(["systemctl", "enable", "timeshift", "--now"])
    subprocess.run(["timeshift", "--create", "--comments", "First boot snapshot"])

    open("/etc/kickos-firstboot", "w").close()

    calamares.job.setprogress(1.0)
    return None

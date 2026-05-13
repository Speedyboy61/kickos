#!/usr/bin/env bash

iso_name="kickos-arch"
iso_label="KICKOS_ARCH"
iso_publisher="KickOS Project <https://kickos.dev>"
iso_application="KickOS Arch Linux Live/Rescue DVD"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux'
           'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/usr/local/bin/kickboost"]="0:0:755"
  ["/usr/local/bin/kick-hardware-detect"]="0:0:755"
  ["/usr/local/bin/kicknotify"]="0:0:755"
)

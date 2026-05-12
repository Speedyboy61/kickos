#!/bin/bash
iso_name="kickos-arch"
iso_label="KICKOS_ARCH"
iso_publisher="KickOS Project <https://kickos.dev>"
iso_application="KickOS Arch Linux Live/Rescue DVD"
iso_version="$(date +%Y.%m.%d)"
install_dir="arch"
arch="x86_64"
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
           'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
           'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/usr/local/bin/kickboost"]="0:0:755"
  ["/usr/local/bin/kick-hardware-detect"]="0:0:755"
  ["/usr/local/bin/kicknotify"]="0:0:755"
)

# KickOS

```
++
                                        *+++++++++++*
                               #####*****+++++++++++                 +====--
                                 #####*****++++++++        +++++++=========
                                   ###*******+++++*      ++++++++++======
                                   ###************     ++++++++++++====            ++++==
                         **       %##************    *+++++++++++++++    ++             ====
                                  ###************  #**+++++++++++++     #***++++++++++   ====
                                  ##************  ***++++++++++++  %%%%%%%%%%%######+++  ===+
                    *         +  ###******************+++++++++                  ###++   ==*
                   ***           ##*******************++++++++                   ###+  *=+*
                   ***          ###********************+++**                    %#*   ==**
                    *       +   ###***********************                     ###  +=***
                         =     ######*****************##                     %#%  #=***
                      +    ##  ##%####*************### #                    #   +=***
                        **#   %########**********%%% ##**                ##   =****
                     ***  #   %%%########******%%% ####****            #   +=#***  +
                   **# ##     %%############*%%% ######******       %   +=#####  +
                ***# #*      %%%###########%%% %########*******      *=####*  *+
               ++*  *#       %%##########%%%@ %#########*****     =+#####  #*
             +*+* #*#       %%%########%%%@     %#######*     ++%#####          ******
            +++*  ##        %%%######%%%%%        %#%     +++#####% #      *
           + ++   ##       %%%#####%%%%%%@           ++++%%%%#  %####++
          + +++   ####     %%%###%%%%%%@       +=+-+%%%%%%   #####****+++
          +* ===    ######           #   ==++::=%%%%%%  %%####********++++*
           *# =====   ======+=+=======-::=+#%%%%%        %*#***********+++++*
            ***  ===-----=====-:.::#+######%      #       @%#**********++++++=
               *******###*##########%     #**#              %%#######*******++++
                      #%%%%%%%%%     #%
                         %%%%      ##
                        %
        Linux for Gamers  •  kickos.dev
```

**KickOS** is a gaming-focused Linux distribution available in Arch-based, Debian-based, and Handheld editions. Boot into a fully-featured gaming desktop with Wine, Proton-GE, GameMode, MangoHud, and the KickBoost FPS optimizer preinstalled.

## Editions

| Feature | Arch Edition | Debian Edition | Handheld Edition |
|---|---|---|---|
| Base | Arch Linux | Debian Bookworm | Arch Linux |
| Kernel | linux-zen | Liquorix | linux-zen |
| Release model | Rolling | Stable | Rolling |
| AUR | Yes | No (Flatpak) | Yes |
| Desktop environments | KDE, Budgie, Cinnamon, COSMIC, Hyprland, i3, Niri, Cutefish | KDE, Budgie, Cinnamon, COSMIC, Hyprland, i3, Niri, Cutefish | KDE, Budgie, Cinnamon, COSMIC, Hyprland, i3, Niri, Cutefish |
| Best for | Power users | Stability seekers | Handheld gaming PCs |
| Badge | Recommended for gamers | Best for stability | For handheld devices |

## System Requirements

| Edition | Min RAM | Recommended RAM | Storage | CPU |
|---|---|---|---|---|
| Arch | 2 GB | 8 GB | 20 GB | x86_64 |
| Debian | 1 GB | 4 GB | 15 GB | x86_64 |
| Handheld | 4 GB | 16 GB | 32 GB | x86_64 |

## Building from Source

### Prerequisites

**For Arch ISO:**
- `archiso` package (`sudo pacman -S archiso`)

**For Debian ISO:**
- `live-build` package (`sudo apt install live-build`)

### Build

```bash
git clone https://github.com/Speedyboy61/kickos.git
cd kickos

# Build Arch ISO
./build.sh arch

# Build Debian ISO
./build.sh debian

# Build both
./build.sh all

# Clean artifacts
./build.sh clean
```

ISOs will be in the `out/` directory.

### Using the ISO

1. Flash to USB: `dd if=kickos-arch.iso of=/dev/sdX bs=4M status=progress`
2. Boot from USB
3. Click **Install KickOS** on the desktop

## Project Structure

```
kickos/
├── index.html              # Marketing website
├── assets/                 # Logo and images
├── archiso/                # Arch Linux ISO build config
├── debian-live/            # Debian ISO build config
├── calamares/              # Calamares installer modules
│   └── modules/
│       ├── kickos-de/      # Desktop environment picker
│       ├── kickos-gaming/  # Gaming packages picker
│       ├── kickos-bootloader/  # Bootloader picker
│       └── kickos-install/ # Post-install configuration
├── kickupdate/             # GTK4 update manager
├── kickos-welcome/         # First-boot welcome app
├── plymouth-kickos/        # Plymouth boot theme
├── build.sh                # Master build script
└── README.md
```

## Features

- **KickBoost** — CPU/GPU performance mode switcher (balanced/performance/turbo)
- **KickHardwareDetect** — Auto GPU detection and driver installation
- **KickNotify** — Update notification daemon
- **KickUpdate** — GTK4 GUI for system updates
- **Calamares installer** — Choose DE, gaming packages, and bootloader during install
- **Welcome app** — First-boot setup wizard
- **8 desktop environments**: KDE Plasma, Budgie, Cinnamon, COSMIC, Hyprland, i3, Niri, Cutefish

## License

GPL-3.0

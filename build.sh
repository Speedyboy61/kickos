#!/bin/bash
# KickOS Master Build Script
# Usage: ./build.sh [arch|debian|all|clean]

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

build_arch() {
    echo "==> Building KickOS Arch ISO..."
    cd "$ROOT_DIR/archiso"
    if command -v mkarchiso &>/dev/null; then
        mkarchiso -v -w /tmp/kickos-arch-work -o "$ROOT_DIR/out" .
        echo "==> Arch ISO built: $(ls -t "$ROOT_DIR"/out/kickos-arch-*.iso | head -1)"
    else
        echo "ERROR: mkarchiso not found. Install archiso package."
        echo "  sudo pacman -S archiso"
        exit 1
    fi
}

build_debian() {
    echo "==> Building KickOS Debian ISO..."
    cd "$ROOT_DIR/debian-live"
    if command -v lb &>/dev/null; then
        lb clean
        lb config
        lb build
        mkdir -p "$ROOT_DIR/out"
        mv *.iso "$ROOT_DIR/out/" 2>/dev/null || true
        echo "==> Debian ISO built: $(ls -t "$ROOT_DIR"/out/kickos-debian-*.iso | head -1)"
    else
        echo "ERROR: lb (live-build) not found. Install live-build package."
        echo "  sudo apt install live-build"
        exit 1
    fi
}

clean() {
    echo "==> Cleaning build artifacts..."
    rm -rf "$ROOT_DIR/out"
    rm -rf /tmp/kickos-arch-work
    cd "$ROOT_DIR/debian-live" && lb clean 2>/dev/null || true
    echo "==> Clean complete"
}

case "${1:-all}" in
    arch)
        build_arch
        ;;
    debian)
        build_debian
        ;;
    all)
        build_arch
        build_debian
        ;;
    clean)
        clean
        ;;
    *)
        echo "Usage: $0 [arch|debian|all|clean]"
        exit 1
        ;;
esac

#!/bin/bash

set -uex

my_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

: "${NAME:=unknown}"
: "${ID:=unknown}"
: "${ID_LIKE:=unknown}"
if [ -e /etc/os-release ]; then
    # shellcheck disable=SC1091
    source /etc/os-release
else
    # Cygwin / MobaXterm does not have /etc/os-release file
    if [ -e /cygdrive ]; then
        # Found for Cygwin / MobaXterm
        if [ -e /bin/MobaBox.exe ]; then
            # Found MobaXterm
            ID="mobaxterm"
            ID_LIKE="cygwin"
        else
            ID="cygwin"
        fi
    fi
fi
# Debian ID="debian" no ID_LIKE present has wxpython-tools, python3-kivy
# Ubuntu ID="ubuntu" ID_LIKE=debian     has wxpython-tools, python3-kivy
#
# Fedora ID="fedora" no ID_LIKE python3-wxpython4 no kivy package
# epel for el-8 and el-9 also have the python3-wxpython4
# No current cygwin users, no scripted package install known.
# msys2 ID="msys2" has mingw-w64-x86_64-wxPython
# mobaxterm has python3.9 and python39-wx package, no gtk4, no kivy
case "$ID" in
    mobaxterm)
        "${my_dir}/install_mobaxterm.sh"
        ;;
    msys2)
        "${my_dir}/install_msys2.sh"
        ;;
    fedora)
        # Rocky/Alma is probably similar to this
        "${my_dir}/install_fedora.sh"
        ;;
    debian|ubuntu)
        "${my_dir}/install_debian.sh"
        ;;
    *)
        echo "$ID is not yet supported by this script."
        exit 1
        ;;
esac

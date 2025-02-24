#!/usr/bin/bash

set -uex

mingw='mingw-w64-x86_64'

pacman -Syu --noconfirm \
    "${mingw}-ca-certificates" \
    "${mingw}-python" \
    "${mingw}-gtk4" \
    "${mingw}-gettext" \
    "${mingw}-python3-gobject" \
    "${mingw}-aspell" "${mingw}-aspell-en" \
    "${mingw}-python-pywin32" \
    "${mingw}-python-lxml" \
    "${mingw}-python-pyserial" \
    "${mingw}-python-pillow" \
    "${mingw}-python-pycountry" \
    "${mingw}-wxPython"

if [ ! -e /usr/bin/python ]; then
    ln -s /mingw64/bin/python /usr/bin/python
fi

if [ ! -e /usr/bin/python3 ]; then
    ln -s /mingw64/bin/python3 /usr/bin/python3
fi

if [[ "${1:-}" == dev* ]]; then
  # packaging
  # no aspell-it dictionary at this time.
  pacman -Syu --noconfirm \
    git \
    "${mingw}-gcc" \
    "${mingw}-make" \
    "${mingw}-python-codespell" \
    "${mingw}-python-pip" \
    "${mingw}-python-pylint" \
    "${mingw}-python-setuptools" \
    "${mingw}-python-virtualenv"

    # This should not be needed, but is for now.
    if [ ! -e /mingw64/bin/make.exe ]; then
        ln -sf /mingw64/bin/mingw32-make.exe /mingw64/bin/make.exe
    fi
fi

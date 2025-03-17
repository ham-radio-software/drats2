#!/bin/bash

set -uex

my_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

sudo dnf -y install \
    aspell aspell-de aspell-en aspell-es aspell-it aspell-nl \
    ca-certificates \
    gedit \
    libxml2 \
    python3 \
    python3-cairo \
    python3-feedparser \
    python3-flask \
    python3-geopy \
    python3-gevent \
    python3-gobject \
    python3-greenlet \
    python3-libxml2 \
    python3-pillow \
    python3-pyaudio \
    python3-pycountry \
    python3-pyserial \
    python3-wxpython4

pypi_dir=~/drats_support/local/lib/pypi
mkdir -p "$pypi_dir"

if [ -e "$pypi_dir/bin/pip3" ]; then
  echo 'Pip already updated'
else
  # Pip always complains if a newer version is available until
  # you upgrade to it.
  echo "upgrading pip, this will warn that pip needs upgrading"
  pip3 install --upgrade --target="$pypi_dir" pip
  ls "$pypi_dir/bin"
fi
# Need to set PYTHONPATH to use the PyPi packages
PYTHONPATH="$pypi_dir"
export PYTHONPATH
ls "$pypi_dir/bin"
# If we do not include pip here, for some reason pip removes the
# binary for it.  Why???
"$pypi_dir/bin"/pip3 install --upgrade --target="$pypi_dir" \
  -r "${my_dir}/fedora/requirements.txt"

if [[ "${1:-}" == dev* ]]; then
  sudo dnf -y install \
    bandit \
    codespell \
    gcc \
    make \
    pkgconf-pkg-config \
    pylint \
    python3-babel \
    python3-devel \
    python3-ipykernel \
    python3-pip \
    python3-simplejson \
    python3-sphinx \
    python3-tkinter \
    python3-virtualenv \
    shellcheck \
    yamllint
fi

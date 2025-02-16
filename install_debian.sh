#!/bin/bash

set -uex

DEBIAN_FRONTEND=noninteractive
export DEBIAN_FRONTEND

sudo -S -E apt-get --assume-yes update
sudo -S -E apt-get --assume-yes install \
    aspell aspell-de aspell-en aspell-es aspell-it aspell-nl \
    ca-certificates \
    gedit \
    libcairo2-dev \
    libxml2-utils \
    libgirepository1.0-dev \
    python3 \
    python3-feedparser \
    python3-flask \
    python3-geopy \
    python3-gevent \
    python3-gi \
    python3-gi-cairo \
    python3-greenlet \
    python3-kivy \
    python3-lxml \
    python3-pil \
    python3-pyaudio \
    python3-pycountry \
    python3-pydub \
    python3-serial \
    python3-tk \
    python3-toml \
    wxpython-tools

if [[ "${1:-}" == dev* ]]; then
  sudo -S -E apt-get --assume-yes install \
    bandit \
    codespell \
    gcc \
    make \
    pkg-config \
    pylint \
    python3-dev \
    python3-ipykernel \
    python3-pip \
    python3-simplejson \
    python3-sphinx \
    python3_venv \
    shellcheck \
    yamllint
fi

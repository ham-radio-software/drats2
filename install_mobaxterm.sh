#!/bin/bash

set -uex

my_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# MobaXterm has some of these packages built in.
# curl git wget

# MobaXterm uses aliases which are needed in a setup script
apt_get='/bin/MobaBox.exe apt-get'
mkdir='/usr/bin/busybox mkdir'

# This is needed to prevent pop ups that pause the install
DEBIAN_FRONTEND=noninteractive
export DEBIAN_FRONTEND
# Update to current and add packages
# apt-get --assume-yes update
$apt_get -y upgrade
$apt_get -y install \
  aspell aspell-de aspell-en aspell-es aspell-it \
  ffmpeg \
  gedit gettext gettext-devel git gcc-core \
  libgtk3_0 libjpeg-devel libportaudio-devel \
  python3 python3-pip python3-tkinter \
  zlib-devel

python_version_raw="$(python --version)"
python_version="${python_version_raw#* }"
python_major_minimum="${python_version%.*}"
python_major="${python_major_minimum%.*}"
python_minor="${python_major_minimum#*.}"
pyver="python${python_major}${python_minor}"

$apt_get -y install \
  "${pyver}-devel" "${pyver}-gi" "${pyver}-lxml" \
  "${pyver}-sphinx" "${pyver}-wx" \

pypi_dir=/usr/local/lib/pypi
$mkdir -p "$pypi_dir"

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
  -r "${my_dir}/mobaxterm/requirements.txt"
#
# kivy does not apparently install on cygwin/MobaXterm

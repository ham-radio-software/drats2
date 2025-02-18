#!/bin/bash

set -uex

if [ "$#" -lt 1 ] || [ -z "$1" ]; then
    echo "Project directory not specified"
    exit 1
fi

base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Find out what our environment is
: "${NAME:=}"                 # Human readable Name
: "${ID:=}"                   # Usually single word ID
: "${ID_LIKE:=}"              # Seen on Ubuntu, not on fedora.
: "${VERSION_ID:=}"           # Not on Msys2
: "${COMPUTERNAME:=}"         # Only present on Linux emulation on Windows.
: "${MSYSTEM:=}"              # Only present on Msys2
: "${MOBASTARTUPDIR:=}"  # Only seen on MobaXterm
if [ -e /etc/os-release ]; then
    # shellcheck disable=SC1091
    source /etc/os-release
fi

# Calculate the virtual environment filename.
# We should need to recreate the environment if missing.
subtype="$ID"
if [ -n "$COMPUTERNAME" ]; then
    # Found Microsoft Windows hosted linux emulation
    if [ -e /cygdrive ]; then
        # Found "Cygwin or MobaXterm"
        if [ -n "$MOBASTARTUPDIR" ]; then
            subtype="moba"
        else
            subtype="cygwin"
        fi
    elif [ -z "$MSYSTEM" ]; then
        subtype="Unknown"
    fi
fi
environment_name="${HOSTNAME}_${subtype}_build_env"

if [ ! -d "$environment_name" ]; then
    python3 -m venv "$environment_name" --upgrade-deps
fi

# shellcheck disable=SC1091
source "$environment_name/bin/activate"

pip install -U -r build/requirements.txt --no-warn-script-location

: "${PYTHONPATH:=}"
PYTHONPATH="${PWD}/version_git/src/version_git:${PYTHONPATH}"
export PYTHONPATH

pushd "$1"
    "$base_dir/python_pre_build.py" "$1"
    python -m build
popd

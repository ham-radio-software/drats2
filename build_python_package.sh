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
# By default we put the base_env in the current directory.
base_env=''
subtype="$ID"
if [ -n "$COMPUTERNAME" ]; then
    # Found Microsoft Windows hosted linux emulation
    # The virtual environment needs to be a local directory
    base_env=~/
    # Git needs this on a shared directory sometimes.
    git config --global --add safe.directory "$PWD"
    if [ -e /cygdrive ]; then
        # Found "Cygwin or MobaXterm"
        if [ -n "$MOBASTARTUPDIR" ]; then
            subtype="moba"
            # Git needs this on a shared directory sometimes, for some
            # reason git is seeing a slightly different path than $PWD
            # is returning.
            git config --global --add safe.directory "/drives${PWD#/cygdrive}"
        else
            subtype="cygwin"
            # Git needs this on a shared directory sometimes.
            git config --global --add safe.directory "$PWD"
        fi
    elif [ -z "$MSYSTEM" ]; then
        subtype="Unknown"
    fi
fi
environment_name="${base_env}${HOSTNAME}_${subtype}_build_env"

if [ ! -d "$environment_name" ]; then
    python3 -m venv "$environment_name" --upgrade-deps
fi

# shellcheck disable=SC1091
source "$environment_name/bin/activate"

pip install -U -r build_python_rq/requirements.txt --no-warn-script-location
pip freeze

: "${PYTHONPATH:=}"
PYTHONPATH="${PWD}/version_git/src/version_git:${PYTHONPATH}"
export PYTHONPATH

pushd "$1"
    if [[ $# -lt 2 ]] || [[ $2 != "doc" ]]; then
        "$base_dir/python_pre_build.py" "$1"
        python -m build
    fi
    sphinx-build -M html docs/source/ docs/build/
popd

#!/bin/bash

set -uex

base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Iterate through the directories.
for project_name in */; do
    if [ -d "$project_name" ]; then
        if [ -e "${project_name}/pyproject.toml" ]; then
            echo "Processing ${project_name}"
            "$base_dir"/build_python_package.sh "$project_name"
        fi
    fi
done

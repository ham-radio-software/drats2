#!/usr/bin/python3
'''Python pre-build.'''
# Copyright 2008 Dan Smith <dsmith@danplanet.com>
# review 2015-2020 Maurizio Andreotti  <iz2lxi@yahoo.it>
# Copyright 2022 John. E. Malmberg - Python3 Conversion
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

from os import system
from os.path import dirname, join
from glob import glob
from subprocess import check_output
import sys

def default_build():
    '''Default Build.'''

    cmd = 'git describe --tags'
    cmd = cmd.split()
    raw_version = check_output(cmd).decode().strip()

    system(f'towncrier build --yes --version {raw_version}')

    project = sys.argv[1]
    doc_sources = ['NEWS.rst']
    for file_name in doc_sources:
        file_gz = file_name + ".gz"
        system(f"gzip -c {file_name} > {file_gz}")

    man_src_files = glob("share/*.1")
    for file_name in man_src_files:
        file_gz = file_name + ".gz"
        file_name_full = join('src', project, file_name)
        file_gz_full = join('src', project, file_gz)
        system(f"gzip -c {file_name_full} > {file_gz_full}")

    glob_path = join('src', project, 'locale', '*', 'LC_MESSAGES', '*.po')
    locale_po_files = glob(glob_path)
    for file_name in locale_po_files:
        locale_dir = dirname(file_name)
        command = f"msgfmt -o {locale_dir}/D-RATS.mo {locale_dir}/D-RATS"
        system(command)

default_build()

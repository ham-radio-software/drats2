# Package version_git

This is a program to allow using the git describe command to attempt to
calculate the most accurate version information possible with the
minimum of maintenance.

It will also read the pyproject.toml file for additional information.

This is an attempt to make the version display of a program more accurate
so that it can be determined if a user is running a declared release or
if they are running an experimental version.

This is intended to be called by end user programs and packaging
processes.

This module currently can be used to create much of the "about" dialogs.

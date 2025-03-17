# drats2

New implementation of the D-Rats program.

Until we get a beta version running a lot of this will be subject to
change as initially we will be doing experimentation to determine
what works best.

We will need community support to help keep this documentation up
to date.

Developers and even testers are strongly encouraged to add detail about
what they need for their environment.

See the developer_notes.txt file for more information.

## Security warning

Do not use the root or an Administrator account for developing or running
programs, it is only to be used for system administration.

Many PCs setup the systems with a default account that has Administrator
privileges.  Do not use this account.  Instead create new accounts for
all users of the system that do not have Administrator privilege.  This
is one of the basic defenses against malware.

## Some Guiding principles

* Compliance with current known and defacto standards and practices.
* DRY - Do not repeat yourself, avoid duplication.
* Have Unit tests as much as possible.
* Make sure all 3rd party required notices are present.
* Use internet sources for common configuration sources that may change
  independently of D-rats.

## Security warning about PyPi/Pip

PyPI is a well known Python package repository which pip uses as the
default installation directory.

PyPI does not have anyone officially vetting packages to make sure that
they do not have security bugs in them.

PyPI is currently under attack by criminals, some which may be sponsored by
countries to install packages with malware in them.

The most common attack is called typo squatting.  This is the creation of
packages with common misspelling of real package names and the contents of
the package modified to install malware.

For a native implementation of D-Rats on the Microsoft Windows, the only
practical source of dependent packages is PyPI.  We need to be diligent
in making sure that our package list is accurate.

## Security warning about single executable distribution

D-Rats users on Microsoft Windows have indicated that they want a single
package to install with an embedded Python.  The problem with this approach
is that D-Rats depends on lots of additional packages, and a lot of them
will be getting updates.  We probably do not have the cycles to track all
of these changes to get updates out in a timely matter.

## Installation warnings

### Do not try to use setup.py to install packages

The use of setup.py to install python packages is deprecated.
Setup.py may be used in the packaging creation process if present.
<https://packaging.python.org/en/latest/discussions/setup-py-deprecated/>

## Repository Structure

This repository is setup as a "multi-package" repository.  Some of the
package will be experimental.

The current packaging structure preferred for Linux and Python is to have
multiple packages that do a single function, but may be dependent
on other packages.

Each directory that is used for a Python package will have a pyproject.toml
for building a pip installable module.  This module will also provide the
data for populating most of the about dialog.

The base directory for a package directory may not be the same as the actual
package name that is created.

Some packages may end up being split off into separate repositories if
it turns out that they are generic enough for other projects.

### Github Workflows

This is a magic directory for Github Workflow actions.   Github will run
these workflows on its own systems to test a Pull Request (PR).

We will want to run as many unit tests as we can for quality control.

#### Minimum Workflow tests

* Codespell - Spelling checks.   Helps find miss-spelled variables and
  encourages readable variable names.
* pylint - Check for Python PEP compliance, local coding standards, and bugs.
* shellcheck - Checks for issues in Linux shell scripts.
* xmllint - Checks to make sure XML format files are correct.
* yamllint - Checks to make sure that YAML format files are correct.

#### Future Workflow tests

* Unit tests for all modules.
* creating Python and Operating system specific packages.
* Bandit security scanning.

### drats_common

This is code specific to D-Rats that is common to both the D-Rats
repeater and other D-Rats programs.

This also contains the message catalogs for all the D-Rats programs.

### drats_gtk

This is code specific to D-rats GTK coding, target will likely be GTK4.
We do not expect this to be usable natively on Microsoft Windows.

The main advantage of GTK is that that it is the best supported GUI
platform on Linux and Linux emulation environment.

The disadvantage of GTK is that they keep deprecating APIs that we use
and in many cases are not providing documentation on how to do change
the code to use the supported APIs.

### drats_kivy

This is code specific to the Kivy coding.  Kivy can provide support
for an android port, which has been desired.

Building an android project on Kivy has some challenges to set up.

### drats_text

This is for plain-text and "ANSI" terminals.  The reasons for this
module is to assist in automated testing of D-Rats modules that is
harder to do with GUI clients.

### drats_tk

This is for code specific to the Tkinter, which is a built in GUI toolkit
for Python.  This should be the simplest GUI to use to support Windows.

The challenge is if this GUI is good enough for production use.

### drats_wx

This is for code specific to the WxPython coding.  WxPython appears to be
the most widely used for cross platform GUI projects.

### repeater

This is for ratflector specific code.  The ratflector should not have
GUI built in, but can have a GUI for managing the ratflector configuration.

For Linux, the ratflector should be setup as a service.  And a Linux system
should be able to support multiple ratflectors.

For Microsoft Windows, the ratflector should be runnable, but at least at
first it will not be setup as a service.  Todo: Need to determine how to
setup a Python program as a Microsoft Windows Service.

For MacOS, the ratflector should be runnable, but at least at first, it will
not be setup as a service.  Todo: Need to determine how to setup a Python
program as a MacOS service.

### version_git

This is a module designed for eventual standalone use.  Its primary function
is to do its best to find out the version of the program that calls it.

It also reads in the pyproject.toml file to get the information for filling
out most of the "about" dialog boxes.

Once it determines a version, it writes it into the setup_python.py in
the target package source directory for use in package building.

Potential bug: This module has to be able to deal with not having permission
to write to the source directory, as would be the case when the calling
module was installed from a package.

### tests

This is for tests for the entire repository.

The base level contains scripts for installing the test packages needed.
These will mostly be bash scripts for running on Linux or MacOS.

#### Git commit hook installation

A special file "pre-commit" is intended to be run by git before allowing
a commit to be made.  It is intended to run some of the same checks that
will be run by the github actions.

This is used to do checks before committing a change for a pull request.

These checks generally require a Bash shell environment.

~~~bash
cp tests/pre-commit .git/hooks
chmod 755 .git/hooks/pre-commit
~~~

#### pre-commit_d

This contains scripts that can be run before a commit will be made and
will be run by github actions.

## Winlink support

Winlink support requires a [lzhuf][1] compression program to be installed.
Until the lzhuf compression patents expired, open source repositories
and operating system platforms would not provides lzhuf compression packages.

The [lzhuf][1] project has the source and instructions to build the
lzhuf images.   Packages for Microsoft Windows and several Debian based
distributions are available at the [D-Rats Group][3] where a groups.io
account is needed and membership in the [D-Rats Group][3] is needed.

For other platforms you will need to locally build [lzhuf][1] on your
system or convince some one else with a compatible platform to build it
for you and also upload it for others.

## General Development Requirements

* A git program.
* A current supported Python interpreter.
* A good malware scanner if using PyPI modules.

## Recommended Development features

* A Linux system or VM running a current distribution.
* A Microsoft Windows system or VM running a current distribution, or use
  of Cygwin, Msys2, or [MobaXterm][2] environment.
* A system you can install an SMTP mail server with IMAP and POP3 support.
* 2 serial ports and a Null Modem cable to connect them.
* A system that can run Docker or Podman.

## special setup_version.py file

This file will be in the "src/<package_name>".  It is generated / updated
from running a test of the primary module in for that package.  This
module should be updated in git with pull requests so that when someone
tries to run from a downloaded tarball, they will get the version number
to display.

## Internationalization support

For unique sentences, the standard "_()" will be used, but the text
will be in upper case English.   These are intended to be message tags.

For words that are commonly reused, it is planned that one or more python
modules will be made to contain a method of returning a translated string
with some caching to avoid duplicate translated lookups.  This is similar
to how Java handles strings ae resources.

Currently the script has only been tested on Linux.

The script build_python_locale.sh builds a new drats.pot file each time
it is run, so we don't need to store that file in the repository.

That script will update all the po files into the
drats_common/src/drats_common/locale directory with current changes.

For new translations, online translators can be used, but these should be
followed up by users that actually know the languages.

These po files will need to be manually edited.  The updated po files
will need to be checked into the git repository.

After updating the po files, the script needs to be run again to update
the .mo files.  We will need to save the .mo files into the repository.

It has not yet been tested to see if the python packaging needs to be
modified to store the message catalogs.

## Building Python Packages

The setup_version.py file needs to be present and up to date before
running the packaging scripts.

For an actual release, a Python compatible version tag needs to be created
in git for that release.  That tag will be used for the checkout.

If you do a test build of python packages, it will modify the NEWS.rst
module in every package directory.  It will also clear out the newsfragments
directory of fragments.   After a test build you will need to reset these
files back to what they were before.

After a real package build, a pull request is needed to commit the updated
news.RST files and newsfragments directories.  No other pull requests should
should be merged until this pull request merged.

The packaging script needs a bash shell to run and will create a python
virtual environment.  There is one script that will build all the packages,
and it calls a script that will build just one package.

~~~bash
# Build or update the po files.
./build_python_locale.sh

# Build all packages
./build_python_packages.sh

# Build a single package
./build_python_package.sh drats_gtk
~~~

The next step after building python compatible packages is to figure out
how to build platform specific packages.

## Linux specific information

This will include Linux emulation on Windows platforms.

### Running D-Rats on Linux

To be filled in later.

Ideally it will be to download and install a pre-built package.

### Developing D-Rats on Linux

You will need to install the development packages for your distribution.
Eventually install scripts will be provided for the versions being tested.

Visual Studio code claims to also support being able to setup a
Python virtual environment for it to more safely use pip
installed modules.

## Microsoft Windows specific information

Generally we will try to make sure that we can work on the current supported
versions of Microsoft Windows.   We will not intentionally drop support for
older versions of Microsoft Windows, but the dependent libraries D-Rats
depends on may not work on older Microsoft Windows version.

Currently using the [MobaXterm][2] product allows running the D-rats as
far back as Microsoft Windows 7.

### Running D-Rats on Microsoft Windows

To be determined and will change as this project evolves.

Currently Python 3.x needs to be installed, typically from the Microsoft
store.

Then from a non-admin account you can pip install additional modules.

Visual Studio code claims to also support being able to setup a
Python virtual environment for it to more safely evaluate pip
installed modules.

### Developing D-Rats on Microsoft Windows

This will need everything needed to run D-Rats and some additional
packages.

A git package will be needed.

A separate linux system or VM, or one of Cygwin, Msys2, or [MobaXterm][2] will
be needed to run the pre-commit bash check scripts.

Note from wb8tyw: I will be using a Linux system with mirrored disks for the
development storage and will be using it for git access and for running
docker container and linting programs.

#### Software from the Microsoft Store

* Python 3.x (current).
* Visual Studio Code - recommended.

## MacOS specific information

### Running drats2 on MacOS

To be determined. The ambition would be to have drats available as an
installable package.

### Developing drats2 on MacOS

Possible environment to develop drats on MacOS:

* Visual Studio Code, with extensions:
  * Github Pull requests
* Python3 installed via brew

* virtual environment created by Visual Studio Code using
  * macos\requirements.txt

## Android specific information

To be determined.

## Visual Studio code recommendations

### Settings

Use View -> Command Palette to enter in Preferences: Open User Settings (json).

The editor rulers help keep lines to fit in 80 column which makes it more
universally readable.  At this writing, they can only be set in json.

The "files.eol" setting should be set to "\n" globally.  Microsoft Windows
usually has no trouble with \n line endings.  The default of auto or using
crlf can result in corrupted git commits.

With the Codespell Extension installed, this will also have the user
dictionary so that you can edit to remove mis-spellings that were
accidentally added to it.

At this time, it is not planned to include the workspace .vscode directory
and its settings file in the repository, it will be up to each user to
manage it.

~~~json
{
    "editor.rulers": [
        {
            "column": 79,
            "color": "#ff00ff"
        },
        {
            "column": 120,
            "color": "#ff0000"
        }
    ],
    "files.eol": "\n"
}
~~~

### Recommended Extensions

* Code Spell Checker from Street Side Software
* markdownlint from David Anson
* Python from Microsoft (Brings in some more extensions)
* ShellCheck from Timon Wong
* YAML from Red Hat

[1]: https://github.com/ham-radio-software/lzhuf
[2]: https://github.com/ham-radio-software/D-Rats/wiki/010.020-Installation-of-D%E2%80%90Rats-on-Microsoft-Windows-with-MobaXterm
[3]: https://groups.io/g/d-rats/

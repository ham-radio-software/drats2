<# install_windows.ps2
This is a script to install what is needed to run python with an command
line option to in the future install more packages for development.
#>

param(
    [bool]
    $development = 1
)

# Get the directory of the script so it can find the files
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path

# This gets the current python if a python is not installed.
winget install python

# Install required packages for windows
pip install -U -r $scriptDirectory\windows\requirements.txt `
    --no-warn-script-location

if ($null -ne $development) {
    pip install -U -r $scriptDirectory\windows\development\requirements.txt `
        --no-warn-script-location
}

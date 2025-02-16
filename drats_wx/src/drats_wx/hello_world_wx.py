#!/bin/python
'''Hello World WxPython Template program.'''

import logging
import os
from os.path import basename
from os.path import dirname
import sys

logger = logging.getLogger(basename(__file__))

try:
    import wx
except ModuleNotFoundError:
    logger.error('WxPython does not appear to be installed!')
    sys.exit(1)

try:
    import version_git
except ModuleNotFoundError:
    # This is a hack to allow using multiple modules from one git
    # checkout with out having to do special pip installs.

    # Get the current PYTHONPATH, if it exists
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)

    # Add the new path to PYTHONPATH
    module_dir = dirname(__file__)     # directory of program
    my_src = dirname(module_dir)       # src directory
    my_package = dirname(my_src)   # package directory
    my_base = dirname(my_package)  # base repo directory
    my_version_git = os.path.join(my_base, 'version_git', 'src', 'version_git')
    if my_version_git not in pythonpath:
        pythonpath.append(my_version_git)

    # Update the environment variable for child processes
    os.environ['PYTHONPATH'] = os.pathsep.join(pythonpath)

    # Add the new path to sys.path for the current session
    sys.path.append(my_version_git)
    import version_git


def main():
    '''Main Function.'''

    logging.basicConfig(level=logging.INFO)
    my_dir = dirname(__file__)
    version_info = version_git.VersionGit(project_path=my_dir, logger=logger)

    logger.info("VERSION:        %s", version_info.full_version)
    app = wx.App()
    frame = wx.Frame(parent=None, title='Hello World')
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

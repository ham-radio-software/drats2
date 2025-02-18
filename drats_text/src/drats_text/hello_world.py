#!/bin/python
'''Hello World Template program.'''

import logging
import os
from os.path import basename
from os.path import dirname
import sys

try:
    import version_git
except ModuleNotFoundError:
    # Get the current PYTHONPATH, if it exists
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)

    # Add the new path to PYTHONPATH
    my_dir = dirname(__file__)     # directory of program
    my_src = dirname(my_dir)       # src directory
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
    '''Main package for testing.'''
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(basename(__file__))

    version_info = version_git.VersionGit(project_path=my_dir, logger=logger)

    logger.info("VERSION:        %s", version_info.full_version)
    logger.info("PEP440_VERSION: %s", version_info.pep440_version)
    logger.info("NAME:           %s", version_info.project_info['name'])
    logger.info("DESCRIPTION:    %s", version_info.project_info['description'])
    logger.info("AUTHORS:        %s", version_info.project_info['authors'])
    logger.info("LICENSE:        %s", version_info.project_info['license'])
    logger.info("WEBSITE:        %s", version_info.project_info['homepage'])

if __name__ == "__main__":
    main()

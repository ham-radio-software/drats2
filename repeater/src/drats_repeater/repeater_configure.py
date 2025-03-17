#!/bin/python
'''
Repeater configuration.

A D-Rats repeater is intended to be run as an independent background
process.  Normally this is done by running it as service.

There may also be multiple D-Rats repeaters hosted by a system.
'''

import logging
import os
from os.path import basename
from os.path import dirname
from pathlib import Path
import sys

logger = logging.getLogger(basename(__file__))

BASE_MODULE_PATH = None

def import_helper(module_path: str):
    '''
    Import Helper

    This is a hack to allow using multiple modules from one git
    checkout with out having to do special pip installs.

    :param module_path: base directory of additional module
    :type module_path: str
    '''
    # Get the current PYTHONPATH, if it exists
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)

    # pylint: disable=global-statement
    global BASE_MODULE_PATH
    if not BASE_MODULE_PATH:
        # Add the new path to PYTHONPATH
        module_dir = dirname(__file__)          # directory of program
        my_src = dirname(module_dir)            # src directory
        my_package = dirname(my_src)            # package directory
        BASE_MODULE_PATH = dirname(my_package)  # base repo directory

    full_module_path = os.path.join(BASE_MODULE_PATH,
                                    module_path, 'src', module_path)
    if full_module_path not in pythonpath:
        pythonpath.append(full_module_path)

    # Update the environment variable for child processes
    os.environ['PYTHONPATH'] = os.pathsep.join(pythonpath)

    # Add the new path to sys.path for the current session
    sys.path.append(full_module_path)

# Note pylint does not understand how this hack works so will
# report that it can not find the import when it is not in the
# current PYTHONPATH
try:
    import version_git  # type: ignore
except ModuleNotFoundError:
    import_helper('version_git')
    import version_git  # type: ignore

try:
    from common_args import CommonArgs  # type: ignore
    from language import Language  # type: ignore
except ModuleNotFoundError:
    import_helper('drats_common')
    # pylint: disable=ungrouped-imports
    from common_args import CommonArgs  # type: ignore
    # pylint: disable=ungrouped-imports
    from language import Language  # type: ignore


def main():
    '''Main Function.'''

    logging.basicConfig(level=logging.INFO)
    # gettext.install("D-RATS")
    language = Language("drats")

    language.install()

    #lang = gettext.translation("D-RATS",
    #                           localedir="locale",
    #                           fallback=True)
    # lang.install()
    # _ = lang.gettext

    # Setup d-rats message catalogs
    #_language = Language()

    my_dir = dirname(__file__)
    version_info = version_git.VersionGit(project_path=my_dir, logger=logger)

    home = str(Path.home())
    command_defaults = {}

    # A repeater is generally something that will be run as a service.
    # The exception is that we may want to run a repeater from an interactive
    # session for various reasons including testing and debugging.
    command_defaults['config_dir'] = os.path.join(home, '.d-rats-ev')

    common_args = CommonArgs(                         # type: ignore
        description=_("DRATS REPEATER CONFIGURE"),
        defaults=command_defaults,
        logger=logger)

    args = common_args.args

    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=args.loglevel)

    if args.version:
        version_info.log_version()
        sys.exit()

if __name__ == "__main__":
    main()

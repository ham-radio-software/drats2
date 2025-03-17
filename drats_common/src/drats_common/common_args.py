# File: common_args.py

'''
Common Command Argument processing.

Most D-Rats programs take a common set of command line arguments.
'''

import argparse
import logging

class CommonArgs():
    '''
    Common D-Rats Arguments.

    :param description: Description of application
    :type description: str
    :param defaults: Defaults for common parameters
    :type defaults: dict
    :param logger: logger object to inherit, default is None.
    :type logger: :class:`logging.Logger`

        Dictionary keys for defaults:

    :config_dir: Optional Default configuration directory
    :log_file: Optional Default log file
    :stdout: O
    '''

    # pylint wants at least 2 public methods, but we do not need them
    # since this is extending another class.
    # pylint: disable=too-few-public-methods
    class LoglevelAction(argparse.Action):
        '''
        Custom Log Level action.

        This allows entering a log level command line argument
        as either a known log level name or a number.
        '''

        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            if nargs is not None:
                raise ValueError("nargs is not allowed")
            if '_' in globals():
                print("common_args Found _ in globals")
            if '_' in locals():
                print("common_args Found _ in locals")

            argparse.Action.__init__(self, option_strings, dest, **kwargs)

        def __call__(self, _parser, namespace, values, _option_strings=None):
            level = values.upper()
            # pylance has a false alert on getLevelName because of a
            # temporary API change.
            level_name = logging.getLevelName(level)
            # Contrary to documentation, the above returns for me
            # an int if given a name or number of a known named level and
            # str if given a number for a level with out a name.
            if isinstance(level_name, int):
                level_name = level
            elif level_name.startswith('Level '):
                level_name = int(level)
            setattr(namespace, self.dest, level_name)

    def __init__(self, description: str, defaults: dict,
                 logger:logging.Logger = None) -> None:
        self._parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description=description)
        self._args = None
        self._logger = logger

        self._defaults = defaults
        if 'config_dir' in self._defaults:
            self._parser.add_argument('-c', '--config',
                            default=self._defaults['config_dir'],
                            help=_("CONFIGURATION DIRECTORY"))

        # While loglevel actually returns an int, it needs to be set to the
        # default type of str for the action routine to handle both named and
        # numbered levels.
        self._parser.add_argument('--loglevel',
                        action=self.LoglevelAction,
                        default='INFO',
                        help=_('LOG LEVEL FOR DISPLAYED MESSAGES'))

        if 'log_file' in self._defaults:
            self._parser.add_argument("-L", "--log",
                        dest="log_file",
                        default=self._defaults['log_file'],
                        help=_("LOG DIRECTORY"))

        self._parser.add_argument("-v", "--version",
                        action="store_true",
                        help=_("SHOW VERSION"))

        self._args = None

    @property
    def args(self):
        '''
        :returns: '''
        if not self._args:
            self._args = self._parser.parse_args()
        return self._args

    def add_argument(self, *args, **kwargs):
        '''
        add_argument

        Add an argument to the parser via :class:`argparse.ArgumentParser`
        '''
        self._parser.add_argument(*args, **kwargs)

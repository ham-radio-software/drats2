# File: language
'''
Language support.

This provides access to the locale files used by D-Rats.
'''

from os.path import dirname
from os.path import join
import gettext

# pylint: disable=too-few-public-methods
class Language():
    '''
    Access to the Language catalogs for D-Rats.

    While under development D-Rats is expecting the message catalogs
    to be in the drats_common python package.

    This may be changed here to look in to the standard locations
    a distribution package would install the message catalogs.

    :param domain: Domain name of the message file, default 'drats'
    :type domain: str
    '''

    def __init__(self, domain='drats'):
        locale_dir = join(dirname(__file__), 'locale')
        self._lang = gettext.translation(domain, locale_dir, fallback=True)

    def install(self):
        '''
        Install the _() as a translation function globally.
        '''
        self._lang.install()

#!/bin/python

import logging
import os
from sys import exit

logger = logging.getLogger(__name__)

default_gtk = '4.0'
if 'MSYSTEM' in os.environ:
    default_gtk = '3.0'
try:
    import gi                          # type: ignore
    try:
        gi.require_version('Gtk', default_gtk)
    except ValueError:
        logger.info(f'GTK {default_gtk} is not available!')
        try:
            gi.require_version('Gtk', '3.0')
        except ValueError:
            logger.error('GTK 3 does not appear to be installed!')
            exit(1)
    from gi.repository import Gtk      # type: ignore
except ModuleNotFoundError:
    logger.error('GTK does not appear to be installed!')
    exit(1)

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.present()

def main():
    app = Gtk.Application()
    app.connect('activate', on_activate)

    app.run(None)

if __name__ == "__main__":
    main()

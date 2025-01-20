#!/bin/python

import logging
# import os
from sys import exit

logger = logging.getLogger(__name__)

try:
    from kivy.app import App
    from kivy.uix.widget import Widget
except ModuleNotFoundError:
    logger.error('Kivy does not appear to be installed!')
    exit(1)


class HelloWorld(Widget):
    pass


class HelloApp(App):
    def build(self):
        return HelloWorld()


def main():
    HelloApp().run()

if __name__ == "__main__":
    main()

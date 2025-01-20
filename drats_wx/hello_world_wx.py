#!/bin/python

import wx

def main():
    app = wx.App()
    frame = wx.Frame(parent=None, title='Hello World')
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

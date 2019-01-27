#!/usr/bin/env python
# (c) Stefan Countryman, 2019

"""
Browse NDS2 channels for a given time frame. Select channels and time windows
and open an `ndscope` window to view interactive plots of timeseries data (look
up `ndscope` documentation for details).
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_Dialog

class Browser(QtWidgets.QDialog):

    def __init__(self):
        super(Browser, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Browser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# (c) Stefan Countryman, 2019

import sys
from PyQt5 import QtWidgets
from .controller import Browser, top_level_channel_widgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Browser()
    # from https://stackoverflow.com/questions/41204234/python-pyqt5-qtreewidget-sub-item
    for tlw in top_level_channel_widgets().values():
        ex.ui.treeWidget.addTopLevelItem(tlw)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

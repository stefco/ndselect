#!/usr/bin/env python
# (c) Stefan Countryman, 2019

"""
Browse NDS2 channels for a given time frame. Select channels and time windows
and open an `ndscope` window to view interactive plots of timeseries data (look
up `ndscope` documentation for details).
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from window import Ui_Dialog
from xdg.BaseDirectory import save_cache_path

CACHE_ROOT = save_cache_path('ndselect')

TOP_LEVEL_CHANNELS = {
    'LLO': (
        'L0:ACM',
        'L0:FMC',
        'L0:PEM',
        'L1:ALS',
        'L1:AOS',
        'L1:ASC',
        'L1:AWC',
        'L1:CAL',
        'L1:CAM',
        'L1:CDS',
        'L1:DAQ',
        'L1:DMT',
        'L1:FEC',
        'L1:GRD',
        'L1:HPI',
        'L1:IMC',
        'L1:IOP',
        'L1:ISC',
        'L1:ISI',
        'L1:LSC',
        'L1:OAF',
        'L1:ODC',
        'L1:OMC',
        'L1:PEM',
        'L1:PSL',
        'L1:SEI',
        'L1:SQZ',
        'L1:SUS',
        'L1:SYS',
        'L1:TCS',
        'LVE',
    ),
    'LHO': (
        'H0:FMC',
        'H0:SAF',
        'H0:VAC',
        'H1:ALS',
        'H1:AOS',
        'H1:ASC',
        'H1:AWC',
        'H1:CAL',
        'H1:CDS',
        'H1:DAQ',
        'H1:DMT',
        'H1:FEC',
        'H1:GDS',
        'H1:GRD',
        'H1:HPI',
        'H1:IMC',
        'H1:IOP',
        'H1:ISC',
        'H1:ISI',
        'H1:LSC',
        'H1:OAF',
        'H1:ODC',
        'H1:OMC',
        'H1:PEM',
        'H1:PSL',
        'H1:SEI',
        'H1:SQZ',
        'H1:SUS',
        'H1:SYS',
        'H1:TCS',
        'H1:VID',
    ),
}

class Browser(QtWidgets.QDialog):

    def __init__(self):
        super(Browser, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


def top_level_channel_widgets():
    obs_widgets = {obs: QTreeWidgetItem([obs])
                   for obs in TOP_LEVEL_CHANNELS}
    for obs, obs_widget in obs_widgets.items():
        for top_level_channel in TOP_LEVEL_CHANNELS[obs]:
            obs_widget.addChild(QTreeWidgetItem([top_level_channel]))
    return obs_widgets

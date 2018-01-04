# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DispatchHeroDockWidget
                                 A QGIS plugin
 This plugin dispatches firetrucks
                             -------------------
        begin                : 2017-12-13
        git sha              : $Format:%H$
        copyright            : (C) 2017 by TU Delft
        email                : pim.o.klaassen@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtCore import pyqtSignal
import DispatchHero_visualisation as visual
import DispatchHero_calculations as calc

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'DispatchHero_dockwidget_base.ui'))


class DispatchHeroDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()
    #custom signals
    updateAttribute = QtCore.pyqtSignal(str)

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(DispatchHeroDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        #setup global variables
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        # set up GUI operation signals
        # GUI button connections
        self.autoOnButton.clicked.connect(self.autoOn)
        self.autoOffButton.clicked.connect(self.autoOff)
        self.previousButton.clicked.connect(self.previous)
        self.nextButton.clicked.connect(self.next)
        self.addButton.clicked.connect(self.add)
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomOutButton.clicked.connect(self.zoomOut)
        
        # visualisation connections

        # initialisation

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def autoOn(self):
        pass

    def autoOff(self):
        visual.testing()

    def previous(self):
        pass

    def next(self):
        calc.shortestpath(self.canvas)

    def add(self):
        pass

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def cancelSelection(self):
        pass

    def drawPolygon(self):
        pass

    def dispatch(self):
        pass

    def setDestination(self):
        pass

    def displayMap(self):
        pass
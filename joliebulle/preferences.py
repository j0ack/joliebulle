#!/usr/bin/python3
# ­*­coding: utf­8 -­*­


# joliebulle 3.6
# Copyright (C) 2010-2016 Pierre Tavares
# Copyright (C) 2012-2015 joliebulle's authors
# See AUTHORS file.

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import logging
from PyQt5 import QtWidgets, QtCore
from preferences_ui import Ui_Preferences
from settings import Settings
from globals import recettes_dir, home_dir
from sys import platform

logger = logging.getLogger(__name__)


class DialogPref(QtWidgets.QDialog):
    prefAccepted = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.settings = Settings()
        self.ui = Ui_Preferences()
        self.ui.setupUi(self)
        self.ui.lineEditPathLib.setText(recettes_dir)
        try:
            self.ui.spinBoxBoilOff.setValue(
                int(self.settings.conf.value("BoilOffRate")))
            self.ui.spinBoxCooling.setValue(
                int(self.settings.conf.value("CoolingLoss")))
        except:
            pass
        try:
            self.ui.spinBoxGrainTemp.setValue(
                int(self.settings.conf.value("GrainTemp")))
            self.ui.doubleSpinBoxFudgeFactor.setValue(
                float(self.settings.conf.value("FudgeFactor")))
        except:
            pass
        try:
            self.ui.doubleSpinBoxGrainRetention.setValue(
                int(self.settings.conf.value("GrainRetention")))
        except:
            pass

        # les connexions
        self.ui.pushButtonChangeLib.clicked.connect(self.changePushed)
        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

    def changePushed(self):
        self.d = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            self.tr("Choisir un dossier"),
            home_dir)
        if not self.d:
            pass
        else:
            self.ui.lineEditPathLib.setText(self.d)

    def accepted(self):

        if platform == 'win32':
            self.settings.conf.setValue("pathWin32", self.ui.lineEditPathLib.text())
        else:
            self.settings.conf.setValue("pathUnix", self.ui.lineEditPathLib.text())
            logger.debug(self.settings.conf.value("pathUnix"))

        self.settings.conf.setValue("BoilOffRate", self.ui.spinBoxBoilOff.value())
        self.settings.conf.setValue("CoolingLoss", self.ui.spinBoxCooling.value())
        self.settings.conf.setValue("GrainTemp", self.ui.spinBoxGrainTemp.value())
        self.settings.conf.setValue(
            "FudgeFactor", self.ui.doubleSpinBoxFudgeFactor.value())
        self.settings.conf.setValue(
            "GrainRetention", self.ui.doubleSpinBoxGrainRetention.value())

        self.prefAccepted.emit()

    def rejected(self):
        self.ui.lineEditPathLib.setText(recettes_dir)

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


from PyQt5 import QtWidgets
from PyQt5 import QtCore
import view.base
from base import ImportBase
from model.misc import Misc
from editorM_ui import Ui_Dialog


class DialogD(QtWidgets.QDialog):
    baseChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()

        self.ui.listViewDivers.setModel(view.base.getMiscsQtModel())
        self.ui.comboBoxType.addItem(self.tr("Epice"))
        self.ui.comboBoxType.addItem(self.tr("Clarifiant"))
        self.ui.comboBoxType.addItem(self.tr("Traitement Eau"))
        self.ui.comboBoxType.addItem(self.tr("Herbe"))
        self.ui.comboBoxType.addItem(self.tr("Arôme"))
        self.ui.comboBoxType.addItem(self.tr("Autre"))

        self.selectionModel = self.ui.listViewDivers.selectionModel()
        self.selectionModel.currentChanged.connect(self.voir)
        self.ui.pushButtonNouveau.clicked.connect(self.nouveau)
        self.ui.pushButtonEnlever.clicked.connect(self.enlever)
        self.ui.pushButtonAjouter.clicked.connect(self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxType.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)

    def setModel(self):
        self.ui.listViewDivers.setModel(view.base.getMiscsQtModel())
        self.selectionModel.currentChanged.connect(self.voir)

    def voir(self, current, previous):
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        m = current.data(view.constants.MODEL_DATA_ROLE)

        self.ui.lineEditNom.setText(m.name)
        if m.type == 'Spice':
            self.ui.comboBoxType.setCurrentIndex(0)
        elif m.type == 'Fining':
            self.ui.comboBoxType.setCurrentIndex(1)
        elif m.type == 'Water Agent':
            self.ui.comboBoxType.setCurrentIndex(2)
        elif m.type == 'Herb':
            self.ui.comboBoxType.setCurrentIndex(3)
        elif m.type == 'Flavor':
            self.ui.comboBoxType.setCurrentIndex(4)
        elif m.type == 'Other':
            self.ui.comboBoxType.setCurrentIndex(5)
        else:
            self.ui.comboBoxType.setCurrentIndex(0)

    def ajouter(self):
        m = Misc()
        m.name = self.ui.lineEditNom.text()

        if self.ui.comboBoxType.currentIndex() is 0:
            m.type = 'Spice'
        elif self.ui.comboBoxType.currentIndex() is 1:
            m.type = 'Fining'
        elif self.ui.comboBoxType.currentIndex() is 2:
            m.type = 'Water Agent'
        elif self.ui.comboBoxType.currentIndex() is 3:
            m.type = 'Herb'
        elif self.ui.comboBoxType.currentIndex() is 4:
            m.type = 'Flavor'
        elif self.ui.comboBoxType.currentIndex() is 5:
            m.type = 'Other'
        else:
            m.type = 'Spice'
        ImportBase.addMisc(m)
        self.setModel()

    def nouveau(self):
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        self.ui.lineEditNom.setText('')
        self.ui.comboBoxType.setCurrentIndex(0)

    def enlever(self):
        selection = self.ui.listViewDivers.selectionModel().selectedIndexes()
        for index in selection:
            m = index.data(view.constants.MODEL_DATA_ROLE)
            ImportBase().delMisc(m)
        self.setModel()

    def rejected(self):
        self.baseChanged.emit()

#!/usr/bin/python3.1
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
import view.base  # noqa
from PyQt5 import QtWidgets
import xml.etree.ElementTree as ET
from model.fermentable import Fermentable
from model.hop import Hop
from model.yeast import Yeast
from model.misc import Misc
from base import ImportBase

logger = logging.getLogger(__name__)


class ImportIng(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

    def parseFile(self, s):
        fichierBeerXML = s
        try:
            self.arbre = ET.parse(fichierBeerXML)
            presentation = self.arbre.find('.//RECIPE')  # noqa
            fermentables = self.arbre.findall('.//FERMENTABLE')
            hops = self.arbre.findall('.//HOP')
            levures = self.arbre.findall('.//YEAST')
            misc = self.arbre.findall('.//MISC')

            for element in hops:
                ImportBase.addHop(Hop.parse(element))
            for element in fermentables:
                ImportBase.addFermentable(Fermentable.parse(element))
            for element in misc:
                ImportBase.addMisc(Misc.parse(element))
            for element in levures:
                ImportBase.addYeast(Yeast.parse(element))
        except:
            self.warningFile()

        self.hopsNum = len(hops)
        self.fermNum = len(fermentables)
        self.miscNum = len(misc)
        self.yeastNum = len(levures)

        self.info()

    def info(self):
        info = QtWidgets.QMessageBox.information(  # noqa
            self,
            self.tr("Importation réussie"),
            self.tr((
                "Importation réussie de {} houblons, "
                "{} fermentables, {} ingrédients divers, "
                "{} levures."
            ).format(self.hopsNum, self.fermNum, self.miscNum, self.yeastNum))
        )

    def warningFile(self):
        warning = QtWidgets.QMessageBox.warning(  # noqa
            self,
            self.tr("Fichier non compatible"),
            self.tr("Le fichier n'est pas compatible.")
        )

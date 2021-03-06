#!/usr/bin/python3
# ­*­coding: utf­8 -­*­

# joliebulle 3.4
# Copyright (C) 2013 Thomas Gerbet

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

from helper.recipeimporter.importBeerXML import (
    importBeerXMLFermentable, importBeerXMLHop, importBeerXMLMash,
    importBeerXMLMashStep, importBeerXMLMisc, importBeerXMLYeast,
    importBeerXMLRecipe
)
from helper.recipeimporter.importBSMX import (
    importBSMXFermentable, importBSMXHop, importBSMXMash, importBSMXMashStep,
    importBSMXMisc, importBSMXYeast, importBSMXRecipe
)
from model.fermentable import Fermentable
from model.hop import Hop
from model.mash import Mash
from model.mashstep import MashStep
from model.misc import Misc
from model.recipe import Recipe
from model.yeast import Yeast

RecipeImporterRepository = {
    "beerxml": {
        Recipe: importBeerXMLRecipe,
        Fermentable: importBeerXMLFermentable,
        Hop: importBeerXMLHop,
        Mash: importBeerXMLMash,
        MashStep: importBeerXMLMashStep,
        Misc: importBeerXMLMisc,
        Yeast: importBeerXMLYeast
    },
    "bsmx": {
        Recipe: importBSMXRecipe,
        Fermentable: importBSMXFermentable,
        Hop: importBSMXHop,
        Mash: importBSMXMash,
        MashStep: importBSMXMashStep,
        Misc: importBSMXMisc,
        Yeast: importBSMXYeast
    }
}

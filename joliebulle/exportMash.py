# joliebulle 3.6
# Copyright (C) 2010-2016 Pierre Tavares
# Copyright (C) 2012-2015 joliebulle's authors
# See AUTHORS file.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import json
import xml.etree.ElementTree as ET
from operator import attrgetter


class ExportMash:

    def export(self, listMash):
        self.database = ET.Element('DATABASE')
        listMash = sorted(listMash, key=attrgetter('name'))
        for m in listMash:
            mash = ET.SubElement(self.database, 'MASH')
            mashVersion = ET.SubElement(mash, 'VERSION')
            mashVersion.text = '1'
            mashName = ET.SubElement(mash, 'NAME')
            mashName.text = m.name
            grainTemp = ET.SubElement(mash, 'GRAIN_TEMP')
            grainTemp.text = '20'
            tunTemp = ET.SubElement(mash, 'TUN_TEMP')
            tunTemp.text = '20'
            ph = ET.SubElement(mash, 'PH')
            ph.text = str(m.ph)
            spargeTemp = ET.SubElement(mash, 'SPARGE_TEMP')
            spargeTemp.text = str(m.spargeTemp)
            steps = ET.SubElement(mash, 'MASH_STEPS')

            for s in m.listeSteps:
                step = ET.SubElement(steps, 'MASH_STEP')
                stepVersion = ET.SubElement(step, 'VERSION')
                stepVersion.text = '1'
                stepName = ET.SubElement(step, 'NAME')
                stepName.text = s.name
                stepType = ET.SubElement(step, 'TYPE')
                stepType.text = s.type
                stepTemp = ET.SubElement(step, 'STEP_TEMP')
                stepTemp.text = str(s.temp)
                stepTime = ET.SubElement(step, 'STEP_TIME')
                stepTime.text = str(s.time)
                stepVol = ET.SubElement(step, 'INFUSE_AMOUNT')
                stepVol.text = '0'

    def enregistrer(self, s):
        ET.ElementTree(self.database).write(s, encoding="utf-8")

    def exportJson(self, listMash):
        listMash = sorted(listMash, key=attrgetter('name'))

        dic = {}

        mashes = []
        for m in listMash:
            mash = {}
            mash['name'] = m.name
            mash['ph'] = m.ph
            mash['sparge'] = m.spargeTemp
            steps = []
            mashes.append(mash)
            for s in m.listeSteps:
                step = {}
                step['name'] = s.name
                step['temp'] = s.temp
                step['time'] = s.time
                step['type'] = s.type
                steps.append(step)
            mash['steps'] = steps

        dic['mashes'] = mashes
        dic = json.dumps(dic)

        return dic

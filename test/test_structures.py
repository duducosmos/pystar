#!/usr/bin/env python3
# *-* Coding: UTF-8 *-*
__author__ = "Eduardo dos Santos Pereira"
__email__ = "pereira.somoza@gmail.com"
__credits__ = ["Eduardo dos Santos Pereira"]
__license__ = "GPLV3"
__version__ = "1.0.1"
__maintainer__ = "Eduardo dos Santos Pereira"
__status__ = "Stable"

"""
This file is part of cosmicstar.
copyright : Eduardo dos Santos Pereira

cosmicstar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.
cosmicstar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

"""
import unittest

from pycosmicstar.structures import structures
from pycosmicstar.lcdmcosmology import lcdmcosmology


class test_structures(unittest.TestCase):

    myStructures = structures(lcdmcosmology)

    def test_massFunction(self):
        self.assertEqual(round(self.myStructures.massFunction(9.0, 1.0), 11),
                          8.45e-09)

    def test_fstm(self):
        self.assertEqual(round(self.myStructures.fstm(6.0), 2),
                          515.94)

    def test_halos_n(self):
        self.assertEqual(round(self.myStructures.halos_n(0.0), 2),
                          23584651682.25)

    def test_fbstruc(self):
        self.assertEqual(round(self.myStructures.fbstruc(0.0), 2),
                          0.73)

    def test_numerical_density_halos(self):
        self.assertEqual(
            round(self.myStructures.numerical_density_halos(0.0), 7),
                          6.76e-05)

    def test_abt(self):
        self.assertEqual(round(self.myStructures.abt(1.0), 4),
                            0.0082)

    def test_creatCachDiretory(self):
        self.assertTrue(self.myStructures.getCacheDir()[0],
        "The directory not Exist")

    def test_setDeltaHTinker(self):
        self.myStructures = structures(lcdmcosmology, massFunctionType="TK")
        self.assertTrue(self.myStructures.setDeltaHTinker(200))

if(__name__ == "__main__"):
    unittest.main()

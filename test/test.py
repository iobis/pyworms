# -*- coding: utf-8 -*-
import unittest
import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pyworms
import datetime

os.environ["PYWORMS_VERBOSE"] = "1"

class Test(unittest.TestCase):

    def setUp(self):
        self.abraAlbaID = 141433
        self.nonExistingID = 9999999
        self.invalidID = "abcde"
        logging.disable(logging.CRITICAL)

    def testAphiaRecordByAphiaID(self):
        res = pyworms.aphiaRecordByAphiaID(0)
        self.assertIsNone(res)
        res = pyworms.aphiaRecordByAphiaID(self.nonExistingID)
        self.assertIsNone(res)
        res = pyworms.aphiaRecordByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(ValueError):
            pyworms.aphiaRecordByAphiaID(self.invalidID)

    def testAphiaDistributionsByAphiaID(self):
        res = pyworms.aphiaDistributionsByAphiaID(self.nonExistingID)
        self.assertIsNone(res)
        res = pyworms.aphiaDistributionsByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(ValueError):
            pyworms.aphiaDistributionsByAphiaID(self.invalidID)

    def testAphiaAttributesByAphiaID(self):
        res = pyworms.aphiaAttributesByAphiaID(self.nonExistingID)
        self.assertIsNone(res)
        res = pyworms.aphiaAttributesByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(ValueError):
            pyworms.aphiaAttributesByAphiaID(self.invalidID)

    def testAphiaRecordsByName(self):
        res = pyworms.aphiaRecordsByName("Abra alba")
        self.assertIsNotNone(res)
        res = pyworms.aphiaRecordsByName("xxxxxxxxx")
        self.assertIsNone(res)

    def testAphiaClassificationByAphiaID(self):
        res = pyworms.aphiaClassificationByAphiaID(self.abraAlbaID)
        self.assertTrue("species" in res)
        self.assertTrue("speciesid" in res)
        self.assertTrue(res["speciesid"] is not None)
        self.assertTrue("kingdom" in res)
        self.assertTrue("kingdomid" in res)
        self.assertTrue(res["kingdomid"] is not None)
        with self.assertRaises(ValueError):
            pyworms.aphiaClassificationByAphiaID(self.invalidID)
        res = pyworms.aphiaClassificationByAphiaID(self.nonExistingID)
        self.assertIsNone(res)

    def testCache(self):
        pyworms.aphiaRecordByAphiaID.cache_clear()
        self.assertEquals(pyworms.aphiaRecordByAphiaID.cache_info()[3], 0)
        pyworms.aphiaRecordByAphiaID(123459)
        self.assertEquals(pyworms.aphiaRecordByAphiaID.cache_info()[3], 1)

    def testAphiaRecordsByMatchNames(self):
        res = pyworms.aphiaRecordsByMatchNames(["Abra albo", "Lanice conchilega"])
        self.assertIsNotNone(res)
        self.assertEquals(len(res), 2)
        self.assertEquals(len(res[0]), 1)
        self.assertEquals(len(res[1]), 1)
        self.assertEquals(res[0][0]["match_type"], "phonetic")
        self.assertEquals(res[1][0]["match_type"], "exact")
        res = pyworms.aphiaRecordsByMatchNames("Abra albo")
        self.assertIsNotNone(res)
        self.assertEquals(len(res), 1)
        names = ["Barbatia tenella (Reeve, 1844)",
                 "Mitra kantori Poppe, Tagaro & Salisbury, 2009",
                 "Diminovula culmen (Cate, 1973)",
                 "Hastulopsis turrita (E. A. Smith, 1873)",
                 "Purpurcapsula bayeri (Fehse, 1998)",
                 "Hebra corticata (A. Adams, 1852)",
                 "Tridentarius dentatus (Linnaeus, 1758)",
                 "Terebra textilis Hinds, 1844",
                 "Psammobiidae",
                 "Monstrotyphis singularis Houart, 2002",
                 "Morula nodulifera (Menke, 1829)",
                 "Lithophaga corrugata (Philippi, 1846)",
                 "Turritellidae",
                 "Conus planorbis Born, 1778",
                 "Favartia Jousseaume, 1880",
                 "Conus exiguus Lamarck, 1810",
                 "Pictorium versicolor Strong & Bouchet, 2013",
                 "Imbricaria Schumacher, 1817",
                 "Liotiidae",
                 "Contradusta bregeriana (Crosse, 1868)",
                 "Anomiidae",
                 "Monetaria moneta (Linnaeus, 1758)",
                 "Vasticardium elongatum coralense (Vidal, 1993)",
                 "Euprotomus vomer (Röding, 1798)",
                 "Duplicaria teramachii Burch, 1965",
                 "Coralliophila bulbiformis (Conrad, 1837)",
                 "Maculotriton serriale (Deshayes, 1834)",
                 "Hastula strigilata (Linnaeus, 1758)",
                 "Architectonicidae",
                 "Oxymeris areolata (Link, 1807)",
                 "Schwartziella ephamilla (Watson, 1886)",
                 "Cadulus Philippi, 1844",
                 "Conus lividus Hwass in Bruguiére, 1792",
                 "Mitra aurantia aurantia",
                 "Trochidae",
                 "Jujubinus Monterosato, 1884",
                 "Distorsio anus (Linnaeus, 1758)",
                 "Nassarius fraudulentus (Marrat, 1877)",
                 "Cystiscus punctatus Boyer, 2003",
                 "Labiostrombus epidromis (Linnaeus, 1758)",
                 "Barbatia tenella (Reeve, 1844)",
                 "Mitra kantori Poppe, Tagaro & Salisbury, 2009",
                 "Diminovula culmen (Cate, 1973)",
                 "Hastulopsis turrita (E. A. Smith, 1873)",
                 "Purpurcapsula bayeri (Fehse, 1998)",
                 "Hebra corticata (A. Adams, 1852)",
                 "Tridentarius dentatus (Linnaeus, 1758)",
                 "Terebra textilis Hinds, 1844",
                 "Psammobiidae",
                 "Monstrotyphis singularis Houart, 2002",
                 "Morula nodulifera (Menke, 1829)",
                 "Lithophaga corrugata (Philippi, 1846)",
                 "Turritellidae",
                 "Conus planorbis Born, 1778",
                 "Favartia Jousseaume, 1880",
                 "Conus exiguus Lamarck, 1810",
                 "Pictorium versicolor Strong & Bouchet, 2013",
                 "Imbricaria Schumacher, 1817",
                 "Liotiidae",
                 "Contradusta bregeriana (Crosse, 1868)",
                 "Anomiidae",
                 "Monetaria moneta (Linnaeus, 1758)",
                 "Vasticardium elongatum coralense (Vidal, 1993)"]
        res = pyworms.aphiaRecordsByMatchNames(names)
        self.assertIsNotNone(res)
        self.assertEquals(len(res), len(names))
        names = ["Barbatia tenella (Reeve, 1844)",
                 None,
                 "Mitra kantori Poppe, Tagaro & Salisbury, 2009",
                 "Diminovula culmen (Cate, 1973)"]
        res = pyworms.aphiaRecordsByMatchNames(names)
        self.assertIsNotNone(res)
        self.assertEquals(len(res), 4)

    def testAphiaRecordsByMatchNamesNoMatches(self):
        res = pyworms.aphiaRecordsByMatchNames(["xxxxxxxx", "yyyyyyyy"])
        self.assertIsNotNone(res)
        self.assertEquals(len(res), 2)
        res = pyworms.aphiaRecordsByMatchNames(["xxxxxxxx"] * 60)
        self.assertIsNotNone(res)
        self.assertEquals(len(res), 60)

    def testAphiaRecordsByDate(self):
        res = pyworms.aphiaRecordsByDate(datetime.datetime.utcnow() - datetime.timedelta(hours=5))
        self.assertTrue(len(res) > 0)
        res = pyworms.aphiaRecordsByDate(datetime.datetime.utcnow() + datetime.timedelta(hours=1))
        self.assertTrue(res is None)

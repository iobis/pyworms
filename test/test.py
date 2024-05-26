import unittest
import os
import logging
import pyworms
import datetime


os.environ["PYWORMS_VERBOSE"] = "1"


class Test(unittest.TestCase):

    def setUp(self):
        self.abraAlbaID = 141433
        self.nonExistingID = 9999999
        self.invalidID = "abcde"
        self.ncbiID = 399303
        logging.disable(logging.CRITICAL)

    def testAphiaRecordByExternalID(self):
        res = pyworms.aphiaRecordByExternalID(self.ncbiID, type="ncbi")
        self.assertIsNotNone(res)

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
        self.assertEqual(pyworms.aphiaRecordByAphiaID.cache_info()[3], 0)
        pyworms.aphiaRecordByAphiaID(123459)
        self.assertEqual(pyworms.aphiaRecordByAphiaID.cache_info()[3], 1)

    def testAphiaRecordsByMatchNames2(self):
        names = [
            "14(25-33 part)",
            "FWS 6050",
            "FWS 8307",
            "14(25-34)",
            "N 69-4",
            "FWS 8349",
            "Jar no. D327",
            "FWS 18955",
            "FWS 8315",
            "B",
            "14 WD 28-3",
            "FWS 18009",
            "14(25-18)",
            "FWSD 4137",
            "FWS 8435",
            "FWS 8834",
            "FWS 19107",
            "FWS 8643",
            "74-12",
            "LL04-131",
            "74-15",
            "14(25-11)",
            "GPE 17",
            "FWS 4088",
            "FWS 8391",
            "sample #101",
            "32-1",
            "14 WD 28-8",
            "FWS 8540",
            "FWS 8532 B"
        ]
        res = pyworms.aphiaRecordsByMatchNames(names)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), len(names))

    def testAphiaRecordsByMatchNames3(self):
        names = ["Leporellus vittatus", "Leporinus bistriatus", "Cetopsis candiru", "Vandellia", "Bryconops", "Myleus setiger"]
        res = pyworms.aphiaRecordsByMatchNames(names)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), len(names))

    def testAphiaRecordsByMatchNames(self):
        res = pyworms.aphiaRecordsByMatchNames(["Abra albo", "Lanice conchilega"])
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 2)
        self.assertEqual(len(res[0]), 1)
        self.assertEqual(len(res[1]), 1)
        self.assertEqual(res[0][0]["match_type"], "phonetic")
        self.assertEqual(res[1][0]["match_type"], "exact")
        res = pyworms.aphiaRecordsByMatchNames("Abra albo")
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 1)
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
        self.assertEqual(len(res), len(names))
        names = ["Barbatia tenella (Reeve, 1844)",
                 None,
                 "Mitra kantori Poppe, Tagaro & Salisbury, 2009",
                 "Diminovula culmen (Cate, 1973)"]
        res = pyworms.aphiaRecordsByMatchNames(names)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 4)

    def testAphiaRecordsByMatchNamesNoMatches(self):
        res = pyworms.aphiaRecordsByMatchNames(["xxxxxxxx", "yyyyyyyy"])
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 2)
        res = pyworms.aphiaRecordsByMatchNames(["xxxxxxxx"] * 60)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 60)

    def testAphiaRecordsByDate(self):
        res = pyworms.aphiaRecordsByDate(datetime.datetime.utcnow() - datetime.timedelta(hours=10))
        self.assertTrue(len(res) > 0)
        res = pyworms.aphiaRecordsByDate(datetime.datetime.utcnow() + datetime.timedelta(hours=10))
        print(res)
        self.assertTrue(res is None)

    def testAphiaExternalIDByAphiaID(self):
        res = pyworms.aphiaExternalIDByAphiaID(141433, "bold")
        self.assertTrue(len(res) == 1)
        self.assertTrue("642814" in res)


if __name__ == "__main__":
    unittest.main()

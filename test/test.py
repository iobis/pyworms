import unittest
import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pyworms

class Test(unittest.TestCase):

    def setUp(self):
        self.abraAlbaID = 141433
        self.nonExistingID = 9999999
        self.invalidID = "abcde"
        logging.disable(logging.CRITICAL)

    def testAphiaRecordByAphiaID(self):
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

    def testParseLSID(self):
        id = pyworms.parseLSID("urn:lsid:marinespecies.org:taxname:134546")
        self.assertEquals(id, "134546")
        id = pyworms.parseLSID("134546")
        self.assertIsNone(id)

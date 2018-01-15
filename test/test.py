import unittest
import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pyworms

class Test(unittest.TestCase):

    def setUp(self):
        self.abraAlbaID = 141433
        self.invalidID = 9999999
        logging.disable(logging.CRITICAL)

    def testAphiaRecordByAphiaID(self):
        res = pyworms.aphiaRecordByAphiaID(self.invalidID)
        self.assertIsNone(res)
        res = pyworms.aphiaRecordByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(Exception):
            pyworms.aphiaRecordByAphiaID("abcd")

    def testAphiaDistributionsByAphiaID(self):
        res = pyworms.aphiaDistributionsByAphiaID(self.invalidID)
        self.assertIsNone(res)
        res = pyworms.aphiaDistributionsByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(Exception):
            pyworms.aphiaDistributionsByAphiaID("abcd")

    def testAphiaAttributesByAphiaID(self):
        res = pyworms.aphiaAttributesByAphiaID(self.invalidID)
        self.assertIsNone(res)
        res = pyworms.aphiaAttributesByAphiaID(self.abraAlbaID)
        self.assertIsNotNone(res)
        with self.assertRaises(Exception):
            pyworms.aphiaAttributesByAphiaID("abcd")

    def testAphiaRecordsByName(self):
        res = pyworms.aphiaRecordsByName("Abra alba")
        self.assertIsNotNone(res)
        res = pyworms.aphiaRecordsByName("xxxxxxxxx")
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

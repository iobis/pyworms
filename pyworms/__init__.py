# -*- coding: utf-8 -*-
import requests
from .utils import *
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

@lru_cache(maxsize=200)
def aphiaRecordByAphiaID(id):
    try:
        val = int(id)
    except ValueError:
        print("id should be an integer")
    url = wormsURL() + "AphiaRecordByAphiaID/" + str(id)
    r = requests.get(url)
    if r.status_code == 204:
        return None
    elif r.status_code == 200:
        return r.json()
    else:
        raise Exception()

def aphiaAttributeKeysByID(): raise Exception("Method not implemented")

def aphiaAttributesByAphiaID(): raise Exception("Method not implemented")

def aphiaAttributeValuesByCategoryID(): raise Exception("Method not implemented")

def aphiaIDsByAttributeKeyID(): raise Exception("Method not implemented")

def aphiaDistributionsByAphiaID(): raise Exception("Method not implemented")

def aphiaExternalIDByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordByExternalID(): raise Exception("Method not implemented")

def aphiaSourcesByAphiaID(): raise Exception("Method not implemented")

def aphiaChildrenByAphiaID(): raise Exception("Method not implemented")

def aphiaClassificationByAphiaID(): raise Exception("Method not implemented")

def aphiaIDByName(): raise Exception("Method not implemented")

def aphiaNameByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByDate(): raise Exception("Method not implemented")

def aphiaRecordsByMatchNames(): raise Exception("Method not implemented")

def aphiaRecordsByName(): raise Exception("Method not implemented")

def aphiaRecordsByNames(): raise Exception("Method not implemented")

def aphiaSynonymsByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByVernacular(): raise Exception("Method not implemented")

def aphiaVernacularsByAphiaID(): raise Exception("Method not implemented")

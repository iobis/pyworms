# -*- coding: utf-8 -*-
from .utils import wormsURL, parseLSID, validateAphiaID, doGet, flatten
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

@lru_cache(maxsize=200)
def aphiaRecordByAphiaID(id):
    """Returns the Aphia record for an AphiaID.

    :param id: AphiaID
    :returns: Aphia record, None if not found.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaRecordByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=200)
def aphiaRecordsByName(name, like=True, marine_only=True):
    """Returns the Aphia records for a name.

    :param id: AphiaID
    :param like: SQL like query with % wildcard after input
    :param marine_only: Limit to marine taxa
    :returns: Aphia records.
    """
    url = wormsURL() + "AphiaRecordsByName/" + name + "?like=" + utils.renderBool(like) + "&marine_only=" + utils.renderBool(marine_only)
    return doGet(url)

@lru_cache(maxsize=200)
def aphiaDistributionsByAphiaID(id):
    """Returns the Aphia distributions for an AphiaID.

    :param id: AphiaID
    :returns: Aphia distributions.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaDistributionsByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=200)
def aphiaAttributesByAphiaID(id):
    """Returns the Aphia attributes for an AphiaID.

    :param id: AphiaID
    :returns: Aphia attributes.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaAttributesByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=200)
def aphiaClassificationByAphiaID(id):
    validateAphiaID(id)
    url = wormsURL() + "AphiaClassificationByAphiaID/" + str(id)
    res = doGet(url)
    return flatten(res)

def aphiaAttributeKeysByID(): raise Exception("Method not implemented")

def aphiaAttributeValuesByCategoryID(): raise Exception("Method not implemented")

def aphiaIDsByAttributeKeyID(): raise Exception("Method not implemented")

def aphiaExternalIDByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordByExternalID(): raise Exception("Method not implemented")

def aphiaSourcesByAphiaID(): raise Exception("Method not implemented")

def aphiaChildrenByAphiaID(): raise Exception("Method not implemented")

def aphiaIDByName(): raise Exception("Method not implemented")

def aphiaNameByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByDate(): raise Exception("Method not implemented")

def aphiaRecordsByMatchNames(): raise Exception("Method not implemented")

def aphiaRecordsByNames(): raise Exception("Method not implemented")

def aphiaSynonymsByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByVernacular(): raise Exception("Method not implemented")

def aphiaVernacularsByAphiaID(): raise Exception("Method not implemented")

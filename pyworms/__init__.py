# -*- coding: utf-8 -*-
from .utils import wormsURL, parseLSID, validateAphiaID, doGet, doGetPaginated, flatten
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

@lru_cache(maxsize=2000)
def aphiaRecordByAphiaID(id):
    """Returns the Aphia record for an AphiaID.

    :param id: AphiaID
    :returns: Aphia record, None if not found.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaRecordByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=2000)
def aphiaRecordsByName(name, like=True, marine_only=True):
    """Returns the Aphia records for a name.

    :param id: AphiaID
    :param like: SQL like query with % wildcard after input
    :param marine_only: Limit to marine taxa
    :returns: Aphia records.
    """
    url = wormsURL() + "AphiaRecordsByName/" + name + "?like=" + utils.renderBool(like) + "&marine_only=" + utils.renderBool(marine_only)
    return doGet(url)

@lru_cache(maxsize=2000)
def aphiaDistributionsByAphiaID(id):
    """Returns the Aphia distributions for an AphiaID.

    :param id: AphiaID
    :returns: Aphia distributions.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaDistributionsByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=2000)
def aphiaAttributesByAphiaID(id):
    """Returns the Aphia attributes for an AphiaID.

    :param id: AphiaID
    :returns: Aphia attributes.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaAttributesByAphiaID/" + str(id)
    return doGet(url)

@lru_cache(maxsize=2000)
def aphiaClassificationByAphiaID(id):
    """Returns the Aphia classification for an AphiaID.

    :param id: AphiaID
    :returns: Aphia classification.
    """
    validateAphiaID(id)
    url = wormsURL() + "AphiaClassificationByAphiaID/" + str(id)
    res = doGet(url)
    return flatten(res)

@lru_cache(maxsize=2000)
def _aphiaRecordsByMatchNamesCacheable(q):
    url = wormsURL() + "AphiaRecordsByMatchNames?" + q
    return doGet(url)

def batch(iterable):
    l = len(iterable)
    for ndx in range(0, l, 50):
        yield iterable[ndx:min(ndx + 50, l)]

def aphiaRecordsByMatchNames(names):
    """Returns Aphia matches for a set of names.

    :param names: Names
    :returns: Aphia matches.
    """
    names = [names] if not isinstance(names, (list,)) else names
    results = []

    for n in batch(names):
        q = "&".join(["scientificnames[]=" + name for name in n])
        res = _aphiaRecordsByMatchNamesCacheable(q)
        if res is None:
            results = results + [[]] * len(names)
        else:
            results = results + res
    return results

def aphiaRecordsByDate(start_date, end_date=None, marine_only=True):
    """Returns Aphia records by change date.

    :param start_date: Start date
    :param end_date: End date
    :param marine_only: Marine only
    :returns: Aphia records.
    """
    url = wormsURL() + "AphiaRecordsByDate?marine_only=" + utils.renderBool(marine_only) + "&startdate=" + utils.renderDate(start_date) + "&enddate=" + utils.renderDate(end_date) + "&offset=##"
    return doGetPaginated(url)

def cache_clear():
    aphiaRecordByAphiaID.cache_clear()
    aphiaRecordsByName.cache_clear()
    aphiaDistributionsByAphiaID.cache_clear()
    aphiaDistributionsByAphiaID.cache_clear()
    aphiaAttributesByAphiaID.cache_clear()
    aphiaClassificationByAphiaID.cache_clear()
    _aphiaRecordsByMatchNamesCacheable.cache_clear()

def aphiaAttributeKeysByID(): raise Exception("Method not implemented")

def aphiaAttributeValuesByCategoryID(): raise Exception("Method not implemented")

def aphiaIDsByAttributeKeyID(): raise Exception("Method not implemented")

def aphiaExternalIDByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordByExternalID(): raise Exception("Method not implemented")

def aphiaSourcesByAphiaID(): raise Exception("Method not implemented")

def aphiaChildrenByAphiaID(): raise Exception("Method not implemented")

def aphiaIDByName(): raise Exception("Method not implemented")

def aphiaNameByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByNames(): raise Exception("Method not implemented")

def aphiaSynonymsByAphiaID(): raise Exception("Method not implemented")

def aphiaRecordsByVernacular(): raise Exception("Method not implemented")

def aphiaVernacularsByAphiaID(): raise Exception("Method not implemented")

from .utils import worms_url, parse_lsid, validate_aphia_id, do_get, do_get_paginated, flatten
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
    validate_aphia_id(id)
    url = worms_url() + "AphiaRecordByAphiaID/" + str(id)
    return do_get(url)


@lru_cache(maxsize=2000)
def aphiaRecordsByName(name, like=True, marine_only=True):
    """Returns the Aphia records for a name.

    :param id: AphiaID
    :param like: SQL like query with % wildcard after input
    :param marine_only: Limit to marine taxa
    :returns: Aphia records.
    """
    url = worms_url() + "AphiaRecordsByName/" + name + "?like=" + utils.render_bool(like) + "&marine_only=" + utils.render_bool(marine_only)
    return do_get(url)


@lru_cache(maxsize=2000)
def aphiaDistributionsByAphiaID(id):
    """Returns the Aphia distributions for an AphiaID.

    :param id: AphiaID
    :returns: Aphia distributions.
    """
    validate_aphia_id(id)
    url = worms_url() + "AphiaDistributionsByAphiaID/" + str(id)
    return do_get(url)


@lru_cache(maxsize=2000)
def aphiaAttributesByAphiaID(id):
    """Returns the Aphia attributes for an AphiaID.

    :param id: AphiaID
    :returns: Aphia attributes.
    """
    validate_aphia_id(id)
    url = worms_url() + "AphiaAttributesByAphiaID/" + str(id)
    return do_get(url)


@lru_cache(maxsize=2000)
def aphiaClassificationByAphiaID(id):
    """Returns the Aphia classification for an AphiaID.

    :param id: AphiaID
    :returns: Aphia classification.
    """
    validate_aphia_id(id)
    url = worms_url() + "AphiaClassificationByAphiaID/" + str(id)
    res = do_get(url)
    return flatten(res)


@lru_cache(maxsize=2000)
def aphiaExternalIDByAphiaID(id, type):
    """Returns an external identifier for an AphiaID.

    :param id: AphiaID
    :param type: One of algaebase, bold, dyntaxa, eol, fishbase, iucn, lsid, ncbi, tsn, gisd
    :returns: Aphia classification.
    """
    validate_aphia_id(id)
    url = worms_url() + "AphiaExternalIDByAphiaID/" + str(id) + "?type=" + type
    return do_get(url)


@lru_cache(maxsize=2000)
def _aphiaRecordsByMatchNamesCacheable(q):
    url = worms_url() + "AphiaRecordsByMatchNames?" + q
    return do_get(url)


def aphiaRecordsByMatchNames(names, marine_only=True):
    """Returns Aphia matches for a set of names.

    :param names: Names
    :param marine_only: Marine only
    :returns: Aphia matches.
    """
    names = [names] if not isinstance(names, (list,)) else names
    names = ["" if n is None else n for n in names]
    results = []

    for n in batch(names):
        q = "&".join(["scientificnames[]=" + name for name in n])
        q = q + "&marine_only=" + utils.render_bool(marine_only)
        res = _aphiaRecordsByMatchNamesCacheable(q)
        if res is None:
            results = results + [[]] * len(n)
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
    url = worms_url() + "AphiaRecordsByDate?marine_only=" + utils.render_bool(marine_only) + "&startdate=" + utils.render_date(start_date) + "&enddate=" + utils.render_date(end_date) + "&offset=##"
    return do_get_paginated(url)


@lru_cache(maxsize=2000)
def aphiaRecordByExternalID(id, type):
    """Returns an Aphia record for an external identifier.

    :param id: AphiaID
    :param type: One of algaebase, bold, dyntaxa, eol, fishbase, iucn, lsid, ncbi, tsn, gisd
    :returns: Aphia record.
    """
    url = worms_url() + "AphiaRecordByExternalID/" + str(id) + "?type=" + type
    return do_get(url)


def batch(iterable):
    l = len(iterable)
    for ndx in range(0, l, 50):
        yield iterable[ndx:min(ndx + 50, l)]


def cache_clear():
    aphiaRecordByAphiaID.cache_clear()
    aphiaRecordsByName.cache_clear()
    aphiaRecordByExternalID.cache_clear()
    aphiaDistributionsByAphiaID.cache_clear()
    aphiaDistributionsByAphiaID.cache_clear()
    aphiaAttributesByAphiaID.cache_clear()
    aphiaClassificationByAphiaID.cache_clear()
    _aphiaRecordsByMatchNamesCacheable.cache_clear()


def aphiaAttributeKeysByID(): raise Exception("Method not implemented")


def aphiaAttributeValuesByCategoryID(): raise Exception("Method not implemented")


def aphiaIDsByAttributeKeyID(): raise Exception("Method not implemented")


def aphiaSourcesByAphiaID(): raise Exception("Method not implemented")


def aphiaChildrenByAphiaID(): raise Exception("Method not implemented")


def aphiaIDByName(): raise Exception("Method not implemented")


def aphiaNameByAphiaID(): raise Exception("Method not implemented")


def aphiaRecordsByNames(): raise Exception("Method not implemented")


def aphiaSynonymsByAphiaID(): raise Exception("Method not implemented")


def aphiaRecordsByVernacular(): raise Exception("Method not implemented")


def aphiaVernacularsByAphiaID(): raise Exception("Method not implemented")

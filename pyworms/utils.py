import re
import requests
import time
import datetime
import os

def wormsURL():
    return "http://www.marinespecies.org/rest/"

def parseLSID(input):
    m = re.search("^urn:lsid:marinespecies.org:taxname:([0-9]+)$", input)
    if m:
        return m.group(1)
    else:
        return None

def renderBool(b):
    return "true" if b else "false"

def renderDate(d):
    if d is None:
        return ""
    elif isinstance(d, datetime.date) or isinstance(d, datetime.datetime):
        return d.isoformat()
    elif isinstance(d, basestring):
        return d
    else:
        raise ValueError("Is not a date.")

def validateAphiaID(id):
    try:
        int(id)
    except:
        raise ValueError("id should be an integer")

def doGetPaginated(url):
    offset = 1
    results = []
    while True:
        final_url = url.replace("##", str(offset))
        res = doGet(final_url)
        if res is None or len(res) == 0:
            return None if len(results) == 0 else results
        else:
            results = results + res
            offset = offset + 50

def doGet(url):
    if os.environ.get("PYWORMS_VERBOSE") is not None and os.environ.get("PYWORMS_VERBOSE") == "1":
        print url
    attempts = 0
    while True:
        try:
            r = requests.get(url, timeout=300)
            if r.status_code == 204 or r.status_code == 400:
                return None
            elif r.status_code == 200:
                return r.json()
            else:
                raise Exception(url + " return status " + str(r.status_code))
        except Exception as e:
            attempts = attempts + 1
            if attempts > 10:
                raise Exception(e)
            time.sleep(5)

def flatten(classification, result=None):
    result = {} if result is None else result
    if classification is not None:
        rank = classification["rank"].lower()
        result[rank] = classification["scientificname"]
        result[rank + "id"] = classification["AphiaID"]
        if "child" in classification and classification["child"] is not None:
            result["parentNameUsage"] = classification["scientificname"]
            result["parentNameUsageID"] = classification["AphiaID"]
            flatten(classification["child"], result)
        return result
    else:
        return None

import re
import requests
import time

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

def validateAphiaID(id):
    try:
        int(id)
    except:
        raise ValueError("id should be an integer")

def doGet(url):
    attempts = 0
    while True:
        try:
            r = requests.get(url)
            if r.status_code == 204 or r.status_code == 400:
                return None
            elif r.status_code == 200:
                return r.json()
            else:
                raise Exception(url + " return status " + str(r.status_code))
        except Exception as e:
            attempts = attempts + 1
            if attempts > 3:
                raise Exception(e)
            time.sleep(3)

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

import re
import requests

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
        print("id should be an integer")

def doGet(url):
    r = requests.get(url)
    if r.status_code == 204:
        return None
    elif r.status_code == 200:
        return r.json()
    else:
        raise Exception()

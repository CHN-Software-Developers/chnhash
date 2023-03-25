from urllib.request import urlopen
import json

updateUrl = "https://api.github.com/repos/CHN-Software-Developers/chnhash/releases/latest"

def isUpdateAvailable(version):
    try:
        tagName = json.loads(urlopen(updateUrl).read())["tag_name"]

        if(version < tagName):
            return [True, tagName]
        else:
            return [False]
    except:
            return ["ERROR"]

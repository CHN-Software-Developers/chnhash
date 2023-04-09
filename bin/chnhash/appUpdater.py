"""
chnhash provides you with the functionalities of generating and comparing hash values.
Copyright (C) 2022-2023 Himashana Suraweera (Email : Himashana@chnsoftwaredevelopers.com)

This file is part of chnhash.

chnhash is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

chnhash is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with chnhash. If not, see
<https://www.gnu.org/licenses/>.

"""

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

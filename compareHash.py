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

import sys
from filehash import FileHash

# This function receives the hashing algorithm, file and the received hash values as input parameters,
# and returns a list that contains the usingAlgorithm, fileHashValue, receivedHashValue, validity.
def compareHash(algorithm, file, receivedHash):
    fileHashValue = ""
    receivedHashValue = ""
    usingAlgorithm = ""
    
    try: 
        f = open(receivedHash, "r")
        receivedHashValue = f.read().replace(" ", "")
        f.close()
    except: 
        receivedHashValue = receivedHash.replace(" ", "")

    if algorithm == "sha1":
        usingAlgorithm = "SHA-1"
        
        hasher = FileHash('sha1')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")

    elif algorithm == "sha256":
        usingAlgorithm = "SHA-256"
        
        hasher = FileHash('sha256')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")

    elif algorithm == "sha512":
        usingAlgorithm = "SHA-512"

        hasher = FileHash('sha512')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")


    if fileHashValue == "":
        validity = "ERROR"
    elif fileHashValue == receivedHashValue:
        validity = "OK"
    else:
        validity = "INVALID"

    return [usingAlgorithm, fileHashValue, receivedHashValue, validity]
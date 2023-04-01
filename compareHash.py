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
    
    # Try to open the text file that contains the received hash value and if in any case of failure to 
    # open the file, read the text value in the receivedHashValue variable (hash value or this is also 
    # can be the filename. but, in that case, the output will be an invalid one).
    try: 
        f = open(receivedHash, "r")
        receivedHashValue = f.read().replace(" ", "")
        f.close()
    except: 
        receivedHashValue = receivedHash.replace(" ", "")


    if algorithm == "sha1": # If the requested algorithm is SHA-1,
        usingAlgorithm = "SHA-1"
        
        # Using sha1.
        hasher = FileHash('sha1')

        # Hashing the file to be compared with the received hash value.
        fileHashValue = hasher.hash_file(file)
        # Replacing the whitespaces.
        fileHashValue = fileHashValue.replace(" ", "")

    elif algorithm == "sha256": # If the requested algorithm is SHA-256,
        usingAlgorithm = "SHA-256"
        
        # Using sha256.
        hasher = FileHash('sha256')

        # Hashing the file to be compared with the received hash value.
        fileHashValue = hasher.hash_file(file)
        # Replacing the whitespaces.
        fileHashValue = fileHashValue.replace(" ", "")

    elif algorithm == "sha512": # If the requested algorithm is SHA-512,
        usingAlgorithm = "SHA-512"

        # Using sha512.
        hasher = FileHash('sha512')

        # Hashing the file to be compared with the received hash value.
        fileHashValue = hasher.hash_file(file)
        # Replacing the whitespaces.
        fileHashValue = fileHashValue.replace(" ", "")

    # Comparing the hash values.
    if fileHashValue == "":
        validity = "ERROR"
    elif fileHashValue == receivedHashValue:
        validity = "OK"
    else:
        validity = "INVALID"

    # Returning the usingAlgorithm, fileHashValue, receivedHashValue and the validity from the function as a list.
    return [usingAlgorithm, fileHashValue, receivedHashValue, validity]
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

def generateHash(algorithm, file):
    if algorithm == "sha1":
        print("Using: SHA-1")

        hasher = FileHash('sha1')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")

        print("SHA-1: " + fileHashValue , file)

    elif algorithm == "sha256":
        print("Using: SHA-256")

        hasher = FileHash('sha256')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")

        print("SHA-256: " + fileHashValue , file)

    elif algorithm == "sha512":
        print("Using: SHA-512")

        hasher = FileHash('sha512')

        fileHashValue = hasher.hash_file(file)
        fileHashValue = fileHashValue.replace(" ", "")

        print("SHA-512: " + fileHashValue , file)
    else:
        print("Sorry, an error occurred, or the algorithm is not supported with this tool. Please try to use a supported algorithm.")
    

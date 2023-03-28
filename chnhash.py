#!/usr/bin/python3

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
import compareHash
import generateHash
import appUpdater

version = "v0.0.3"

print("\nchnhash " + version)
print("Copyright (C) 2022-2023 Himashana Suraweera (https://chnsoftwaredevelopers.com)")
print("Licensed under the terms of the GNU GPLv3\n")

print("Loading...", end="\r")

# Calling the isUpdateAvailable() function to check for updates by passing the current app version as the parameter.
updateDetails = appUpdater.isUpdateAvailable(version)

if(updateDetails[0] == True): # If an update available, 
    print("-" * 60)
    print("A new update is available. Please run the following commands to update this tool to the latest version.")
    print("wget https://github.com/CHN-Software-Developers/chnhash/archive/refs/tags/" + updateDetails[1] + ".zip")
    print("or download the zip file manually via the above link.")
    print("\nUnzip the downloaded zip file and run the setup.sh file to perform the installation.")
    print("sudo sh setup.sh")
    print("-" * 60 + "\n")
elif(updateDetails[0] == "ERROR"): # If an error occurred while checking for updates,
    print("-" * 60)
    print("Unable to check for updates. Please try again.")
    print("-" * 60 + "\n")

def showUsage():
    print("\nusage: chnhash.py <TASK> <ALGORITHM> <FILE> <RECEIVED HASH VALUE/FILE>")
    print("\nCompare the hash values:")
    print("     chnhash.py -c <ALGORITHM> <FILE> <RECEIVED HASH VALUE/FILE>")
    print("\nGenerate a new hash value:")
    print("     chnhash.py -g <ALGORITHM> <FILE>")

try:
    # Getting the command line arguments as the inputs.
    task = sys.argv[1]
    algorithm = sys.argv[2]
    file = sys.argv[3]

    # If didn't receive the 4th argument (receivedHash), set receivedHash to "NONE"
    try: receivedHash = sys.argv[4] 
    except: receivedHash = "NONE"

    if task == "-c": # If the request is to compare the hash values, , 
        print("process - is hash(" + file + ") == receivedHash(" + receivedHash + ") ?")

        # Calling the compareHash() function to compare the hash values.
        results = compareHash.compareHash(algorithm, file, receivedHash)

        if results[3] != "ERROR": # If the result is not an error,
            print("Using: " + results[0])
            print(results[0] + ":" , results[1] , file)
            print("FILE " + file + ":", results[3])
        else: # If the entered algorithm is not supported,
            print("This hash function is not supported right now. Please try to use any other supported hash functions.")

    elif task == "-g": # If the request is to generate the hash values, 
        print("process - hash(" + file + ")")
        
        # Calling the generateHash() function to generate a hash value.
        generateHash.generateHash(algorithm, file)

except: # If any exception occured,
    print("An unexpected error occurred!")
    showUsage()
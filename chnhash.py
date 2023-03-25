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
#!/usr/bin/python3
import sys
import compareHash
import generateHash
import appUpdater

version = "v0.0.2"

print("\nchnhash v0.0.2")
print("Copyright (C) 2022-2023 Himashana Suraweera (https://chnsoftwaredevelopers.com)")
print("Licensed under the terms of the GNU GPLv3\n")

updateDetails = appUpdater.isUpdateAvailable(version)

if(updateDetails[0] == True):
    print("-" * 60)
    print("A new update is available. Please run the following commands to update this tool to the latest version.")
    print("wget https://github.com/CHN-Software-Developers/chnhash/archive/refs/tags/" + updateDetails[1] + ".zip")
    print("or download the zip file manually via the above link.")
    print("\nUnzip the downloaded zip file and run the setup.sh file to perform the installation.")
    print("sudo sh setup.sh")
    print("-" * 60 + "\n")
elif(updateDetails[0] == "ERROR"):
    print("-" * 60)
    print("Unable to check for updates. Please try again.")
    print("-" * 60 + "\n")
    
try:
    task = sys.argv[1]
    algorithm = sys.argv[2]
    file = sys.argv[3]

    try: receivedHash = sys.argv[4] 
    except: receivedHash = "NONE"

    if task == "-c":
        print("process - is hash(" + file + ") == readFile(" + receivedHash + ") ?")
        compareHash.compareHash(algorithm, file, receivedHash)
    elif task == "-g":
        print("process - hash(" + file + ")")
        generateHash.generateHash(algorithm, file)
except:
    print("An unexpected error occurred!")
    print("usage: chnhash.py <TASK> <ALGORITHM> <FILE> <RECEIVED HASH>")

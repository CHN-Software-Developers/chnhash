#!/usr/bin/python3
import sys
import compareHash
import appUpdater

version = "v0.0.2"

print("\nchnhash -v0.0.2 - CHN Software Developers(https://chnsoftwaredevelopers.com)\n")

updateDetails = appUpdater.isUpdateAvailable(version)

if(updateDetails[0] == True):
    print("-" * 60)
    print("A new update is available. Please run the following commands to update this tool to the latest version.")
    print("wget https://github.com/CHN-Software-Developers/chnhash/archive/refs/tags/" + updateDetails[1] + ".zip")
    print("or download the zip file manually via the above link.")
    print("\nUnzip the downloaded zip file and run the setup.sh file to perform the installation.")
    print("sudo sh setup.sh")
    print("-" * 60 + "\n")
try:
    task = sys.argv[1]
    algorithm = sys.argv[2]
    file = sys.argv[3]
    receivedHash = sys.argv[4]

    if task == "-c":
        print("process - is hash(" + file + ") == readFile(" + receivedHash + ") ?")
        compareHash.compareHash(algorithm, file, receivedHash)
except:
    print("An unexpected error occurred!")
    print("usage: chnhash.py <TASK> <ALGORITHM> <FILE> <RECEIVED HASH>")
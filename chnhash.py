#!/usr/bin/python3
import sys
from filehash import FileHash
import compareHash


print("\nchnhash -v0.0.1 - CHN Software Developers(https://chnsoftwaredevelopers.com)\n")

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

#!/usr/bin/python3
import sys
from filehash import FileHash

def compareHash(algorithm, file, receivedHash):
    f = open(receivedHash, "r")

    if algorithm == "sha512":
        print("Using: SHA-512")
        sha512hasher = FileHash('sha512')
        sha512Hash = sha512hasher.hash_file(file)

        sha512Hash = sha512Hash.replace(" ", "")
        receivedHashValue = f.read().replace(" ", "")

        print("SHA-512: " + sha512Hash , file)

        if sha512Hash == receivedHashValue:
            print("FILE " + file + ": OK")
        else:
            print("FILE " + file + ": INVALID")

    f.close()


print("\nchnhash -v0.0.1 - CHN Software Developers(https://chnsoftwaredevelopers.com)\n")

try:
    task = sys.argv[1]
    algorithm = sys.argv[2]
    file = sys.argv[3]
    receivedHash = sys.argv[4]

    if task == "-c":
        print("process - is hash(" + file + ") == readFile(" + receivedHash + ") ?")
        compareHash(algorithm, file, receivedHash)
except:
    print("An unexpected error occurred!")
    print("usage: chnhash.py <TASK> <ALGORITHM> <FILE> <RECEIVED HASH>")

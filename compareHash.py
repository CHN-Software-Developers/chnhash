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

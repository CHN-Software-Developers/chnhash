import sys
from filehash import FileHash

def generateHash(algorithm, file):
    if algorithm == "sha512":
        print("Using: SHA-512")
        sha512hasher = FileHash('sha512')
        sha512Hash = sha512hasher.hash_file(file)

        sha512Hash = sha512Hash.replace(" ", "")

        print("SHA-512: " + sha512Hash , file)
    

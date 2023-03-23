import sys
from filehash import FileHash

def compareHash(algorithm, file, receivedHash):
    fileHashValue = ""
    receivedHashValue = ""

    try: 
        f = open(receivedHash, "r")
        receivedHashValue = f.read().replace(" ", "")
        f.close()
    except: 
        receivedHashValue = receivedHash.replace(" ", "")

    if algorithm == "sha512":
        print("Using: SHA-512")
        sha512hasher = FileHash('sha512')
        fileHashValue = sha512hasher.hash_file(file)

        fileHashValue = fileHashValue.replace(" ", "")
        
        
        print("SHA-512: " + fileHashValue , file)



    if fileHashValue == "" and receivedHashValue == "":
        print("This hash function is not supported right now. Please try to use any other supported hash functions.")
    elif fileHashValue == receivedHashValue:
        print("FILE " + file + ": OK")
    else:
        print("FILE " + file + ": INVALID")

import hashlib
file1 = open('passlist.txt', 'r')
Lines = file1.readlines()
passwordhash = input("enter the hash to crack: ")
for plaintext in Lines:
    wordhash = hashlib.md5(plaintext.strip().encode('utf-8')).hexdigest()
    if wordhash == passwordhash:
            print('plain text of the given hash is ',plaintext)
            break
    else:
            print("not found")

    

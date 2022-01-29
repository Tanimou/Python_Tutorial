import os
import hashlib
from os.path import join

hashes = {}
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            with open(thefile, 'r') as fhand:
                data = fhand.read()
            hash = hashlib.md5(data.encode()).hexdigest()
            # print thefile, hash
            if hash in hashes:
                print(hashes[hash], thefile)
            else:
                hashes[hash] = thefile

import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            size = os.path.getsize(thefile)
            if size in [2578, 2565]:
                continue
            with open(thefile, 'r') as fhand:
                lines = list(fhand)
            if len(lines) > 1:
                print(len(lines), thefile)
                print(lines[:4])

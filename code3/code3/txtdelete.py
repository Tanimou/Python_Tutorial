import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            size = os.path.getsize(thefile)
            if size in [2578, 2565]:
                print('T-Mobile:', thefile)
                os.remove(thefile)
                continue
            with open(thefile, 'r') as fhand:
                lines = list(fhand)
            if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
                print('iPhone:', thefile)
                os.remove(thefile)
                continue

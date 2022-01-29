import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
with open('cover3.jpg', 'wb') as fhand:
    fhand.write(img)

fname = input('Enter file name: ')
fhand = open(fname)
c = {}
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    time = pieces[5]
    parts = time.split(':')
    hour = parts[0]
    c[hour] = c.get(hour, 0) + 1

lst = [(value, key) for key, value in c.items()]
lst.sort()

for value, key in lst:
    print(key, value)

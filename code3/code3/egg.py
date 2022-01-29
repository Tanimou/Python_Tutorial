fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = sum(1 for line in fhand if line.startswith('Subject:'))
print('There were', count, 'subject lines in', fname)

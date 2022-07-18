import sqlite3
import time
import zlib

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, sender FROM Senders')
senders = {message_row[0]: message_row[1] for message_row in cur}
cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
messages = {
    message_row[0]: (
        message_row[1],
        message_row[2],
        message_row[3],
        message_row[4],
    )
    for message_row in cur
}

print("Loaded messages=",len(messages),"senders=",len(senders))

sendorgs = {}
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns,0) + 1

# pick the top schools
orgs = sorted(sendorgs, key=sendorgs.get, reverse=True)
orgs = orgs[:10]
print("Top 10 Organizations")
print(orgs)

counts = {}
months = []
# cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
for (message_id, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    if dns not in orgs : continue
    month = message[3][:7]
    if month not in months : months.append(month)
    key = (month, dns)
    counts[key] = counts.get(key,0) + 1

months.sort()
with open('gline.js','w') as fhand:
    fhand.write("gline = [ ['Month'")
    for org in orgs:
        fhand.write(",'"+org+"'")
    fhand.write("]")

    for month in months:
        fhand.write(",\n['"+month+"'")
        for org in orgs:
            key = (month, org)
            val = counts.get(key,0)
            fhand.write(f",{str(val)}")
        fhand.write("]");

    fhand.write("\n];\n")
print("Output written to gline.js")
print("Open gline.htm to visualize the data")

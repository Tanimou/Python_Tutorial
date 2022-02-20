s = {'blueberry', 'raspberry', 'strawberry'}
#print(s)
s.add("blueberry")
#print("s: ", s)
d = {"blueberry", "Harry potter", "strawberry", "hunger games","raspberry"}
#print("d: ", d)
#print("s union d: ", s.union(d))
#print("s inter d: ", s.intersection(d))
#print("s diff d: ", s.difference(d))
#print("d diff s: ", d.difference(s))
#*will return both in set s and set d the difference
#print("diff between s and d :", s.symmetric_difference(d))

#*to see if a set is a subset of another set
print(s.issubset(d))
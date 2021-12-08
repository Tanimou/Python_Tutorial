# here i can import a specific element from another python file
import calendar
import datetime as dt
import re
import turtle
from collections import Counter, namedtuple
from functools import reduce
from pathlib import Path

import pytz

import inc_dec
from POO_tutorial import Item, Phone

#!simplifying counting with get()
#*this code:
##counts = dict()
##names = ["csev", "cwen", "csev", "zqian", "cwen"]
##for name in names:
##  if name not in counts:
##    counts[name] = 1
##else:
##  counts[name] += 1

#*can be simplified with get() and become:
counts = {}
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
   # *if name in counts:counts[name]=counts[name]+1 else: counts[name] =0+1=1
   counts[name] = counts.get(name, 0)+1
print("\n")
print(counts)
print("\n")

#*we can do this in one line by using the built-in function from collections module:
names = Counter(["csev", "cwen", "csev", "zqian", "cwen"])
print(names)
print("\n")

#*subtract function
c = Counter(a=4, b=4, c=0, d=-2)
d = ["a", "b", "c", "d", "b", "a"]
c.subtract(d)
print("c: ", c)
print("\n")
#*update function
c.update(d)
print(c)
print("\n")
#*intersection : take minimum common element
d = Counter(["a", "b", "b", "d", "b", "a"])
print(c & d)
#*Union : take the maximum common element
print(c | d)

#!Counting pattern
#print("Counting pattern")
#line = input("enter a line of text: ")
#words = line.split()
#print("words: ", words)
#print("counting...")
#counts=Counter(words)
#print("counts:", counts)
#print("\n")

#!definite loop and dictionaries
#*even though dictionaries are not stored in order, we can still write a for loop that goes through all the entries
#*it goes through all of the keys in the dictionary and look up the values
counts = {"chuck": 1, "fred": 2, "jan": 100}
for key in counts:
    print(key, counts[key])

#*we can get a list of keys, values or items(both) from a dictionary
jjj = {"chuck": 1, "fred": 2, "jan": 100}
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#*we can loop through the key-value pairs in a dictionary using two iteration variables
for aa, bb in jjj.items():
    print(aa, bb)

#*to delete an element of a dictionary we use pop() and specify the key.
#*it will return the value of that key and delete the key/value pairs from the dictionary
l = jjj.pop("jan")
print(jjj)
print(l)

#!2D dictionary, Binary search
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

test2={
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
}

test3 = {
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
}

test4 = {
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
}
#print(test["input"]["cards"])
tests = [test, test2, test3, test4]
#print(tests)

def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

card2=tests[2]["input"]["cards"]
query2 = tests[2]["input"]["query"]
result = locate_card(card2,query2)
print(result)

#!Sets
#*unlike dictionary where we have key/value pairs pattern, a set is kind of dictionary with only values pattern
#*and we can't have duplicate values
s = {'blueberry', 'raspberry', 'strawberry'}
print(s)
s.add("blueberry")
print("s: ", s)
d = {"blueberry", "Harry potter", "strawberry", "hunger games"}
print("d: ", d)
print("s union d: ", s.union(d))
print("s inter d: ", s.intersection(d))
print("s diff d: ", s.difference(d))
print("d diff s: ", d.difference(s))
#*we can convert a set to a list and vice-versa. this is called casting
l = [1, 2, 3, 3, 4, 4, 4, 5, 8, 8, 6, ]
s = set(l)  # casting the list to a set
l = list(s)  # casting back to a list
print(s)
print(l)

#! Tuples
#*Tuples are like lists except that they are immutable: we can't make change on tuples unlike lists
#*And they have parenthesis instead2 of brackets
x = [9, 5, 3]  # this is a list
y = (5, 9, 2)  # this is a tuple
x[2] = 8  # ok!!!
##y[1]=4#error
##we can't use sort(), reverse() or append() on tuples

#!Tuples and assingment
tuple = (4, "fred")
(x, y) = tuple
print(y)
print("\n")

#!Tuples and dictionnaries
#*the items() method in dictionaries returns a list of (key,value) tuples
print("Tuples and dictionaries")
d = {"chuck": 1, "fred": 2, "jan": 100}
tups = d.items()
print(tups)

#!Tuples sorting
#*we can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
d = {"z": 1, "f": 200, "c": 45, "a": 10}  # this is a dictionary
print("\n")
print("Tuples dictionary sorted:")
print(d.items())  # the output is a list of tuples
print(sorted(d.items()))  # return a list of tuple
print("\n")
#*sorting by keys
for k, v in sorted(d.items()):
    print(k, v)
print("\n")
#*sorting by values in descending order
tmp = [(v, k) for k, v in d.items()]
print(tmp)
for k, v in sorted(tmp, reverse=True):
    print(k, v)
print("\n")

#!List comprehension
#*List comprehension creates a dynamic list. Here we are making a list of reversed tuples and then sort it
c = {"a": 10, "b": 1, "c": 22}
print(sorted((v, k) for k, v in c.items()))
print("\n")

#!Named tuples
#*Named tuples assign meaning to each position in a tuple and allow for more readable, self documenting code
#*They can be used wherever regular tuples are used and they add ability to access fields by the name
#*instead of position index
Point = namedtuple("Point", "x y z")  # we named the tuple (x,y,z) Point
newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)  # we can access field by their name
print(newP._asdict())
newp = newP._replace(y=6)
print(newp)
print(newp._fields)
print("\n")

with open("mbox.txt") as hand:
   for line in hand:
       line = line.rstrip()
   print(line) if re.search("^From", line) else print("Not found")
#*greedy matching
##the repeat characters(*and+) push outward in both directions to match the largest possible string

x = "From: Using the: character"
# the ^ means to search all the matchs starting with the character F
y = re.findall("^F.+:", x)
print(y)  # the .+ means one or more characters
##the : is the last character in the match

#*non-greedy matching
##the ? character is used for non-greedy pattern
y = re.findall("^F.+?:", x)
print(y)

#!Fine-tuning string extraction
#*we can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
x = "From stephen.marquard@uct.ac.za Sat Jan 5"
# the \S+ character is used to say we want at least one non-whitespace character
y = re.findall("\S+@\S+", x)
print(y)
print("\n")
# so we search starting by From but we want what is coming after From
y = re.findall("^From (\S+@\S+)", x)
##that's why we put parentheses, we say what we want findall() method to return with parenteses

print(y)

#!Module and pip
#*a module is a part of program we can actually import from a python file to another one in order to use that part of program
#*this is really useful instead of copy paste a programm all accross
#*we use the import keyword at the top of the file where we want to import our module
#*let's say we want to import inc_dec.py so we can use increment and decrement functions here
#*Now we can use the decrement function like this:
inc_dec.decrement(6)

#!Class and Objects in python
#*we can import the Item class from POO_tutorial python file(see the top of this file)
#*and it will import all the data of Item class

#item=POO_tutorial.Item("consolegame",195,10)
item = Item("consolegame", 195, 10)
print(item)
print("\n")
#print(POO_tutorial.Phone.listphone)
print(Phone.listphone)
print("\n")
print(item.getName)
print("\n")
item.setName = "Microsoft"
print("\n")
print(item.getName)
print("\n")

#!map function()
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(x):
    return x**2
print(list(map(func, li)))
#*we can do this with list comprehension
print([func(x) for x in li])
print("\n")

#! filter function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def isOdd(x):
    return x % 2 != 0

def add7(x):
    return x+7
print(list(filter(isOdd, li)))
c = list(map(add7, filter(isOdd, li)))
print(c)

#! the reduce function
#*we need to import functools
#*unlike the map() and filter() functions, reduce() function doesn't return a list but a single cumulative value based on the function we pass in
#*reduce(function,list)
c = reduce(lambda x, y: x*y, c)
print(c)

#!lambda function or anonymous function like in javascript
func2=lambda x:x+5# similar to func2=function(x){return x+5} or func2= x =>x+5 in javascript
print(func2(9))

def funcc(x):
    return func2(x)+85
print(funcc(9))

#*without parameter
afficher=lambda :"hey there"
print(afficher())

#*with multiple parameters
calculer=lambda x,y,z:x+y*z
print(calculer(2, 3, 4))
print("\n")
newList = list(map(lambda x: x+5, li))# like newList=li.map( x =>x+5) in javascript
newList1 = list(filter(lambda x: x % 2 == 0, li))
print(newList)
print(newList1)
print("\n")

#!Decorators

##the *args and **kwargs(arguments and keyword arguments) means to take any arguments and keyword arguments that comes in
##this allows us to pass any function that takes any arguments
#* *args: parameter that will pack all arguments into a tuple
def add(*args):
    return sum(args)
print(add(12, 1, 45, 75))
#* **kwargs: parameter that will pack all arguments into a dictionary
def hello(**kwargs):
    print("hello", end=" ")
    for value in kwargs.values():
        # with end keyword we can print all values in one line
        print(value, end=" ")

hello(title="Mr.", firstname="Cisse", middlename="Amadou", lastname="Tanimou")

def func(f):
    def wrapper(*args, **kwargs):
        print("started")
        f(*args, **kwargs)
        print("Ended")
    return wrapper

@func  # this a decorator. with that we don't need to write func2=func(func2)
def func2(*args):
    print("i am ", args[0], "and i am ", args[1], "yers old")

@func
def func3(**b):
    # we need to casting the dictionary of values to a list because we don't know the keys of the dictionary since it is created when calling the function
    f = list(b.values())
    print("i am ", f[0], " and my profession is ", f[1])

#*we can avoid writing this code by putting a decorator above func3()
#func2=func(func2)
#func3=func(func3)
func2("tanimou", 24)
func3(name="affane", profession="developper javascript")
print("\n")

#!Creating a new package in python
#*we can create a new package by creating a folder and inside it creating a python file called _init_.py.
#*Python will treat automatically the folder as a package

#!Working with directories
#*we need to import the path library from pathlib
##searching all files in the current directory
path = Path()
for file in path.glob("*.py"):
    print(file)

#!Turtle
#*we need to import tutrle library
def square():
    turtl = turtle.Turtle()
    turtl.forward(100)
    turtl.right(90)
    turtl.forward(100)
    turtl.right(90)
    turtl.forward(100)
    turtl.right(90)
    turtl.forward(100)
#square()

#!calendar stuff
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2021, 3))
print()
print(calendar.calendar(2021))

#!Date time
#*to have the date of today
today = dt.date.today()
print(today)
#*to create a date. This function returns an object
print(dt.date(1997, 9, 25))
#*to calculate the number of days between 2 dates
day_since_birthday = today-dt.date(1997, 9, 25)
print(day_since_birthday.days)
#* to calculate the upcoming date
numberOfDays = dt.timedelta(days=100)
print(today+numberOfDays)
#*to create a time
print(dt.time(7, 2, 20, 14))
#dt.date(Year,Month,Day)
#dt.time(Hours,Minutes,Seconds,Millisec)
#dt.datetime(Year,Month,Day,Hours,Minutes,Seconds,Millisec)

#!Time zone
datetime_today = dt.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone("US/Pacific"))
print(datetime_pacific)
#*string formatting with dates with strftime()
# 2019-09-19 ->Sep 19,2019
# "%B" is for the month
# "%d" is for the day
# "%Y" is for the year
# "%a" is for the name of the day like monday, friday,etc
# "%X" is for the time

print(datetime_pacific.strftime("%B %d %Y %X"))

#*String parsing: getting datetime object from date string with strptime()
# Sep 19, 2019 -> datetime(2019,09,19)
print(dt.datetime.strptime("November 13, 2021", "%B %d, %Y"))

#!Assignment with the walrus operator ":="
#*assigns values to variables as part of a larger expression
print(x := 12)
def cub(num):
    return num*3
num_list = [1, 2, 3, 4, 5]
print(ttt := [y for x in num_list if(y := cub(x)) < 14])

##happy=True
##print( happy)
print(happy := True)
## we cannot say: print(happy=True)
#*for example this code:
#?foods=[]
#?while True:
#?  food=input("what food do you like? : ")
#?  if food=="quit":
#?        break
#?  foods.append(food)

#*can be easily be simplified with the walrus operator:
#?foods=[]
#?while (food:=input("what food do you like? : ")) != "quit":
#?  foods.append(food)
#?print(foods)
##here is some examples with walrus operator
#numlist = []
#while (inp := input("Enter a number: "))!="done":
# value = float(inp.strip())
#numlist.append(value)
#print("Average:", sum(numlist)/len(numlist))

#inputs = []
#while (current = input ("Input data: "))!="ennd":
#inputs.append(current)
#print(inputs)

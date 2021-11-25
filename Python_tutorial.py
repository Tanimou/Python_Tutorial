#import pathlib
import re,turtle,calendar,datetime as dt,inc_dec,pytz,random,os,shutil

#import POO_tutorial
from POO_tutorial import Item ,Phone##here i can import a specific element from another python file
from collections import Counter, deque, namedtuple## in order to use collections's features
from pathlib import Path
##!we can ask python what type something is by using the type() function
print(type("hello"))

#nam = input("who are you?")
#print("welcome", nam)
#!the format function
#*optional method that gives users more control when displaying output

animal="cow"
item="moon"
print("the {} jumped over the {}".format(animal, item))

#!Random function
x=random.randint(1,6)#will print a random number between 1 and 6
print(x)
mylist=["rock","paper","scissors"]
z=random.choice(mylist)#will choose between rock, paper and scissors
print(z)
cards=[1,2,3,4,5,6,7,8,9,"j","Q","K","A"]
random.shuffle(cards)
print(cards)

animal="cow"
item="moon"
print("the {} jumped over the {}".format(animal, item))

#!Random function
x=random.randint(1,6)#will print a random number between 1 and 6
print(x)
mylist=["rock","paper","scissors"]
z=random.choice(mylist)#will choose between rock, paper and scissors
print(z)
cards=[1,2,3,4,5,6,7,8,9,"j","Q","K","A"]
random.shuffle(cards)
print(cards)
#! if statement
x = 30
if x < 10:
    print("bigger")

if x > 20:
    print("smaller")
x = 4
#! if else statement
if x < 10:
    print("bigger")
else:
    print("less than 100")
print("All done.")

#! nested if else statement with elif
if x < 10:
    print("bigger")
elif x < 20:
    print("smaller")
else:
    print("Large")
print("all done.")

#! multi way
if x < 10:
    print("bigger")
elif x < 20:
    print("smaller")
print("all done.")

#!advanced if else statement with or operator
is_snowing=True
is_raining=False
is_cold=is_raining or is_snowing
print(is_cold)

#!While loop
i=1
while(i!=10):
    i+=1
    print(i)
print("Done")

#! try/except structure
#*you surround a dangerous code section with try and except. similar to try_catch function in javascript
#*but it will not going to throw an error

astr = "hello bob"
try:
    ## because we can't use int() if the argument doesn't contain numbers, python will see it as an error and then pass onto the except block
    istr = int(astr)

except:
    print("An exception occurred. Bad use of int()")

astr = "123"
try:
    istr = (astr)  # here, no probleme, python's gonna skip the except block
    print("yeah. no error. Here is istr's value:", istr)
except:
    print('An exception occurred')

##sample try/except

#print("sample try/except")
#rawstr = input("Enter a number:")
#try:
 #   ival = int(rawstr)
#except:
 #   ival = -1

#if ival > 0:
 #   print("Nice work")
#else:
 #   print("Not a number")

#!Functions Strucuture in python
#*we define a function in python with the def reserved keyword


def print_lyrics():

    print("Im a lumberjack")
    print("I sleep all night")


print_lyrics()

#*Return statement


def greet():
    return"hello"

print(greet(), "Tanimou")

#*Nested function:
def func(x):
    if x == 1:
        def rv():
            print("x equal to 1")
    else:
        def rv():
            print("x is not equal to 1")
    return rv

new_func=func(1)##now new_func becomes a new function
new_func()

#*keyword argument
def greet_user(firstname,lastname):
    print(f"hi {firstname} {lastname}")
    print("welcome aboard")
greet_user(lastname="smith",firstname="Jim")##lastname and firstname here are what it's called keyword argument

#! Loop and iteration
#*definite loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

friends = ["Joseph", "Glenn", "Gill", "Sally"]
for friend in friends:
    print("Happy year", friend)

#! the "is" and "is not" operators
#*these operators are the same as "===" and "!==" in javascript

#!Len function
fruit = "banana"
print(len(fruit))
fruits = 'apple'
for x in fruits:
    print(x)
#! Slicing Strings
#*We can also look at any continuous section of a string using a colon operator
#*the second number is one beyond the end of the slice "up to but not including"
#*if the second number is beyond the end of the string, it stops at the end
s = "Monty python"
print(s[0:4])
print(s[6:7])
print(s[6:20])

#*if we leave the first number or the second number of the slice, it's assumed to be the beginning or the end of the string respectively
print(s[:2])
print(s[8:])

#*we can specify the stephen
print(s[::2])##meaning go through s with the step of 2, the result will be: Mnypto
print(s[2::2])##meaning start from the second letter till the end with a step of 2
#! using in as a logical operator
fruit = "mango"
if "a" in fruit:
    print("Found it")

#! strip()
#* removes both beginning and ending whitespace
greet = " hello bob"
print(greet.strip())

#! parsing and extracting
#* we want to extract uct.ac.za from "From stephen.marquard@uct.ac.za Sat Jan 5"
data = "From stephen.marquard@uct.ac.za Sat Jan 5"
atpos = data.find("@")
print(atpos)
sppot = data.find(" ", atpos)
print(sppot)
print(data[atpos+1:sppot])

#!Detection of file
#*we need to import os first
#*we specify the path where we want to check the existence of the file
path="C:\\Users\\tanim\\Desktop\\procuration.docx"
if os.path.exists(path):
    print("the location exists")
    if os.path.isdir(path):
        print("that is a directory")
    elif os.path.isfile(path):
        print("that is a file")
else:
    print("the location doesn't exist")

#! Reading files
#*opening a file
##Before we can read the contents of the file, we must tell python which file we are going to work with and what we'll be doing with this file
##this is done by open() function
##it returns a "file handle"-a variable used to perform operations on the file

#?handle=open(filename,mode)
##file name is a string
##mode is optional and should be "r" if we're planning to read the file and "w if to write"
fhand = open("mbox.txt")#*we can also say: with open("mbox.txt") as fhand:
print(fhand)
print("\n")

#*Read a file
##A file handle opened for read can be treated as a sequence of strings
##where each line in the file is a string in the sequence
##we can use the for statement to iterate through a sequence
countLine = 0
for cheese in fhand:
    countLine += 1
    print(cheese)
print("Line count:", countLine)
print("\n")
fhand.close()

#*reading the whole file
fhandd = open("mbox.txt")
inp = fhandd.read()
print((inp))
fhandd.close()
print("\n")

#*reading each lines of the file
fhandd = open("mbox.txt")
inp = fhandd.readlines()
print((inp))
fhandd.close()
print("\n")

#*Searching through a file
fhanddd = open("mbox.txt")
for line in fhanddd:
    line = line.rstrip()
    if line.startswith("hey"):
        print(line)
fhanddd.close()

#!Write in the file
#with open("mbox.txt","a") as fhand: ## "a" means we want to write at the end of the file. "a" stands for "append"
 #   fhand.write("\nwatashi wa")
  #  fhand.close()

#* "w" overwrite an existing file or create a new file.
#*int this way we can create different files  in different formats using python 
with open("index.html", "w") as fhand:
    fhand.write("<p>Hey there</p>")
    fhand.close()
 
 #! Copying a file
 #*there is 3 ways of copying a file but we need to import shutil first   
 ##copyfile()= copies contents of a file
 ##copy()= copyfile() + permission mode + destination can be a directory
 ##copy2()= copy() + copies metadata (file's creation and modification times)

shutil.copyfile("mbox.txt", "mbox2.txt")##will copy the file that is in the current directory to a new file in the same directory. We can specify the path where we want the new file to be stored

#!Moving a file
#* need to import os
source="mbox2.txt"
destination="C:\\Users\\tanim\\Desktop\\mbox2.docx" #At the end we specify the name of the new file. we can move a directory as well
if os.path.exists(destination):
    print("there is already a file there")
else:
    os.replace(source,destination)
    print("{} was moved".format(source))

#! Deletiong a file
if os.path.exists(source):
     os.remove(source)##if the file is in the same directory just specify the name, otherwise must specify the path
else:
    print("there is no file to delete")
    
#*to remove an empty directory (folder): os.rmdir(name_directory or path_to_the_directory)
#* to delete an unempty folder: shutil.rmtree(name_directory or path_to_the_directory) must import shutil first


#! Python list
#*Data structures
#? Using range function
#* the range function returns a list of numbers that range from 0 to one less than the parameter. It actually gives an array of indexes, simply put
print(range(4))
friends = ["Joseph", "Glenn","Glenn","Glenn", "Gill"]
print(range(len(friends)))
for friend_ in friends:
    print("happy new year:", friend_)

#*in Python we have negatif indexes that allow us to iterate from the end of the list
friends = ["Joseph", "Kanna", "Shinozaki", "Glenn", "Gill"]
print(friends[-len(friends)])##if we want to iterate from the end, the index =-1

print(friends[::-2])##gonna print elements from the end with a step of 2

#*we can count the number of an element in the list with count()
friends = ["Joseph", "Glenn", "Glenn", "Glenn", "Gill"]
print(friends.count("Glenn"))

#*we can sort it
friends.sort()
print(friends)

#*we can append another list to a list with extend()
friends.extend([4,8,15,16,23])
print(friends)

#*to insert a value inside of a list at any position we use insert()
friends.insert(1, "tanimou")
print(friends) 

#*append() is used to add at the end of the list a value
friends.append("hey")
print(friends)

#*we can also reverse
friends.reverse()
print(friends)
friends.reverse()

#*and also remove an element
friends.remove("Joseph")
print(friends)

#*to remove the last element of a list we use pop()
print(friends.pop())

#*or even clear a list 
friends.clear()
print(friends)


#!Building a list from Scratch
#*we can create a empty list and then add elements using the append method
stuff = ['book', 99, 'cookie']
print(stuff)

#!Average using list
#numlist = []
#while True:
 #   inp = input("Enter a number: ")
  #  if inp == "done":
   #     break
    #value = float(inp.strip())
    #numlist.append(value)
#print("Average:", sum(numlist)/len(numlist))

#!split() function
#*the split function split a text into a list of words by using the space delimiter by default
line = "first;second;third"
print(line.split())
# *the output is 1 because there is no space between the text in line variable.
print(len(line.split()))
## we can specify what delimiter character to use in the splitting
print(line.split(";"))
l=line.split(";")
print(len(l))
print("\n")

#!Join() function
joined=" and ".join(l)
print(joined)
print("\n")
#!Another type of list:Deque(Double-ended queue)
#*Deques are generalisation of stacks and queues. They support thread-safe,memory efficient appends and pops from either side of deque
#*with approximately the same performance in either direction
#*Deque is faster than a list in terms of adding retrieving elements
d=deque("hello")
print(d)
d.append("4")
d.appendleft("pf")
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
d.extend("456")
print(d)
d.extendleft("olleh")
print(d)
d.rotate(-5)#rotate from the left 5 times
print(d)
c=deque("yahoo",maxlen=5)
print(c)
c.append(1)
print(c)
print("\n")


#!Python dictionnaries
#*dictionnaries are like list but while lists are ordered, dictionnaries are not ordered. We can access values of lists using indexes while in dictionnaries we access them with keys
purse = dict()
purse["money"] = 12
purse["candy"] = 30
purse["tissues"] = 75
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"]+2
print(purse)
#*Dictionnaries are like lists except that they use keys instead of numbers to look up values
##List
print("List:")
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)
print("\n")

##Dictionnary
print("Dictionnary:")
ddd = dict()
ddd["age"] = 21
ddd["course"] = 188
print(ddd)
ddd["age"] = 54
print(ddd)
print("\n")

#!Dictionnary literals
#*Another way to declare a dictionary they are like objects in javascript
print("Dictionnary literals:")
jjj = {
    "chuck": 1,
    "frad": 42,
    "jan": 100
}
print(jjj)
print(jjj.get("chuck"))#same as print(jjj["chuck"]) but this is an old way
print(jjj.get("frad"))
print("\n")
#*it's an error to reference a key which is not in the dictionary
#*we can use the in operator to see if a key is in the dictionary
ccc = dict()
print('csev' in ccc)

print("\n")

#!Name's counting
print("names's counting:")
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts: 
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

#!The get method for dictionary
#*the pattern of checking to see if a key is already in a dictionnary and assuming a default value if the key is not there is so common
# *that there is a method called get() that does this for us

if name in counts:
    x = counts[name]
else:
    x = 0
#*instead of doing that we can simply do:
x = counts.get(name, 0)  # *0 is the default balue if name not in counts

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
counts = dict()
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
c=Counter(a=4,b=4,c=0,d=-2)
d=["a","b","c","d","b","a"]
c.subtract(d)
print("c: ",c)
print("\n")
#*update function
c.update(d)
print(c)
print("\n")
#*intersection : take minimum common element
d=Counter(["a","b","b","d","b","a"])
print(c&d)
#*Union : take the maximum common element
print(c|d)
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
l=jjj.pop("jan")
print(jjj)
print(l)

#!Sets
#*unlike dictionary where we have key/value pairs pattern, a set is kind of dictionary with only values pattern
#*and we can't have duplicate values
s = {"blueberry", "raspberry"}
s.add("strawberry")
print(s)
s.add("blueberry")
print("s: ",s)
d = {"blueberry", "Harry potter", "strawberry", "hunger games"}
print("d: ",d)
print("s union d: ",s.union(d))
print("s inter d: ",s.intersection(d))
print("s diff d: ",s.difference(d))
print("d diff s: ",d.difference(s))
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
tuple=(4, "fred") 
(x, y) = tuple
print(y)
print("\n")

#!Tuples and dictionnaries
#*the items() method in dictionaries returns a list of (key,value) tuples
print("Tuples and dictionaries")
d={"chuck": 1, "fred": 2, "jan": 100}
tups=d.items()
print(tups)

#!Tuples sorting
#*we can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
d = {"z": 1, "f": 200, "c": 45, "a": 10}  # this is a dictionary
print("\n")
print("Tuples dictionary sorted:")
print(d.items())##the output is a list of tuples
print(sorted(d.items()))##return a list of tuple
print("\n")
#*sorting by keys
for k,v in sorted(d.items()):
    print(k,v)
print("\n")
#*sorting by values in descending order
tmp=[]##this is an empty list
for k,v in d.items():
    tmp.append((v,k))
print(tmp)
for k, v in sorted(tmp,reverse=True):
    print(k, v)
print("\n")

#!List comprehension
#*List comprehension creates a dynamic list. Here we are making a list of reversed tuples and then sort it
c={"a":10,"b":1,"c":22}
print(sorted((v,k) for k,v in c.items()) )
print("\n")

#!Named tuples
#*Named tuples assign meaning to each position in a tuple and allow for more readable, self documenting code
#*They can be used wherever regular tuples are used and they add ability to access fields by the name 
#*instead of position index
Point= namedtuple("Point","x y z")##we named the tuple (x,y,z) Point
newP=Point(3,4,5)
print(newP)
print(newP.x,newP.y,newP.z)##we can access field by their name
print(newP._asdict())
newp=newP._replace(y=6)
print(newp)
print(newp._fields)
print("\n")



#!regular expressions or regex
#*need to import re, very useful when we want to search in a file
 
hand=open("mbox.txt")
for line in hand:
    line=line.rstrip()
print(line) if re.search("^From",line) else print("Not found")
hand.close()
#*greedy matching
##the repeat characters(*and+) push outward in both directions to match the largest possible string

x="From: Using the: character"
y=re.findall("^F.+:",x) ##the ^ means to search all the matchs starting with the character F
print(y)                ##the .+ means one or more characters
                        ##the : is the last character in the match 

#*non-greedy matching
##the ? character is used for non-greedy pattern
y = re.findall("^F.+?:", x)
print(y)

#!Fine-tuning string extraction
#*we can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
x="From stephen.marquard@uct.ac.za Sat Jan 5"
y=re.findall("\S+@\S+",x) ##the \S+ character is used to say we want at least one non-whitespace character
print(y)
print("\n")
y=re.findall("^From (\S+@\S+)",x)##so we search starting by From but we want what is coming after From
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
item.setName="Microsoft"
print("\n")
print(item.getName) 
print("\n")

#!map function()
li=[1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x**2
print(list(map(func,li)))
#*we can do this with list comprehension
print([func(x) for x in li])
print("\n")

#! filter function
li=[1,2,3,4,5,6,7,8,9,10]
def isOdd(x):
    return x%2!=0

def add7(x):
    return x+7
print(list(filter(isOdd,li)))
c=list(map(add7,filter(isOdd,li)))
print(c)

#!lambda function or anonymous function like in javascript
func2=lambda x:x+5##similar to func2=function(x){return x+5} or func2= x =>x+5 in javascript
print(func2(9))
def funcc(x):
    return func2(x)+85
print(funcc(9))
#*without parameter
afficher=lambda :"hey there"
print(afficher())
#*with multiple parameters
calculer=lambda x,y,z:x+y*z
print(calculer(2,3,4))
print("\n")
newList=list(map(lambda x:x+5,li))##like newList=li.map( x =>x+5) in javascript
newList1=list(filter(lambda x:x%2==0,li))
print(newList)
print(newList1)
print("\n")

#!Decorators

##the *args and **kwargs(arguments and keyword arguments) means to take any arguments and keyword arguments that comes in
##this allows us to pass any function that takes any arguments

#* *args: parameter that will pack all arguments into a tuple
def add(*args):
    return sum(args)
print(add(12,1,45,75))

#* **kwargs: parameter that will pack all arguments into a dictionary
def hello(**kwargs):
    print("hello",end=" ")
    for value in kwargs.values():
        print(value,end=" ")#with end keyword we can print all values in one line

hello(title="Mr.",firstname="Cisse",middlename="Amadou",lastname="Tanimou")

def func(f):
    def wrapper(*args, **kwargs):
        print("started")
        f(*args, **kwargs)
        print("Ended")
        
    return wrapper

@func##this a decorator. with that we don't need to write func2=func(func2)
def func2(*args):
    print("i am ",args[0],"and i am ",args[1],"yers old")

@func
def func3(**b):
    f=list(b.values())#we need to casting the dictionary of values to a list because we don't know the keys of the dictionary since it is created when calling the function
    print("i am ",f[0]," and my profession is ",f[1])
  
#*we can avoid writing this code by putting a decorator above func3()  
#func2=func(func2)
#func3=func(func3)
func2("tanimou",24)
func3(name="affane",profession="developper javascript")
print("\n")

#!Creating a new package in python
#*we can create a new package by creating a folder and inside it creating a python file called _init_.py.
#*Python will treat automatically the folder as a package

#!Working with directories
#*we need to import the path library from pathlib
##searching all files in the current directory
path=Path()
for file in path.glob("*.py"):
    print(file)

#!Turtle
#*we need to import tutrle library
def square():
    turtl=turtle.Turtle()
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
print(calendar.month(2021,3))
print()
print(calendar.calendar(2021))

#!Date time
#*to have the date of today
today=dt.date.today()
print(today)
#*to create a date. This function returns an object
print(dt.date(1997,9,25))
#*to calculate the number of days between 2 dates
day_since_birthday = today-dt.date(1997, 9, 25)
print(day_since_birthday.days)
#* to calculate the upcoming date
numberOfDays=dt.timedelta(days=100)
print(today+numberOfDays)
#*to create a time
print(dt.time(7,2,20,14))
#dt.date(Year,Month,Day)
#dt.time(Hours,Minutes,Seconds,Millisec)
#dt.datetime(Year,Month,Day,Hours,Minutes,Seconds,Millisec)

#!Time zone
datetime_today=dt.datetime.now(tz=pytz.UTC)
datetime_pacific=datetime_today.astimezone(pytz.timezone("US/Pacific"))
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
print(dt.datetime.strptime("November 13, 2021","%B %d, %Y"))

#!Assignment with the walrus operator ":="
#*assigns values to variables as part of a larger expression
print(x:=12)
def cub(num):
    return num*3
num_list=[1,2,3,4,5]
print(ttt:=[y for x in num_list if(y:=cub(x))<14])

##happy=True
##print( happy)
print(happy:=True)
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



import random
import os
import shutil
from collections import deque  # in order to use collections's features

##!we can ask python what type something is by using the type() function
print(type("hello"))

#nam = input("who are you?")
#print("welcome", nam)

#!the format function
#*optional method that gives users more control when displaying output

animal = "cow"
item = "moon"
print("the {} jumped over the {}".format(animal, item))

#!Random function
x = random.randint(1, 6)  # will print a random number between 1 and 6
print(x)
mylist = ["rock", "paper", "scissors"]
z = random.choice(mylist)  # will choose between rock, paper and scissors
print(z)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "j", "Q", "K", "A"]
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
is_snowing = True
is_raining = False
is_cold = is_raining or is_snowing
print(is_cold)

#!While loop
i = 1
while(i != 10):
    i += 1
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
    istr = int(astr)  # here, no probleme, python's gonna skip the except block
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


new_func = func(1)  # now new_func becomes a new function
new_func()

#*keyword argument


def greet_user(firstname, lastname):
    print(f"hi {firstname} {lastname}")
    print("welcome aboard")


# lastname and firstname here are what it's called keyword argument
# sourcery skip: assign-if-exp, aug-assign, default-get, dict-literal, ensure-file-closed, list-literal, merge-dict-assign, merge-list-append, remove-redundant-slice-index
greet_user(lastname="smith", firstname="Jim")

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
print(s[::2])  # meaning go through s with the step of 2, the result will be: Mnypto
print(s[2::2])  # meaning start from the third letter till the end with a step of 2
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
path = "C:\\Users\\tanim\\Desktop\\procuration.docx"
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
fhand = open("mbox.txt")  # *we can also say: with open("mbox.txt") as fhand:
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

# will copy the file that is in the current directory to a new file in the same directory. We can specify the path where we want the new file to be stored
shutil.copyfile("mbox.txt", "mbox2.txt")

#!Moving a file
#* need to import os
source = "mbox2.txt"
# At the end we specify the name of the new file. we can move a directory as well
destination = "C:\\Users\\tanim\\Desktop\\mbox2.docx"
if os.path.exists(destination):
    print("there is already a file there")
else:
    os.replace(source, destination)
    print("{} was moved".format(source))

#! Deleting a file
if os.path.exists(source):
    # if the file is in the same directory just specify the name, otherwise must specify the path
   os.remove(source)
   pass
else:
    print("there is no file to delete")

#*to remove an empty directory (folder): os.rmdir(name_directory or path_to_the_directory)
#* to delete an unempty folder: shutil.rmtree(name_directory or path_to_the_directory) must import shutil first


#! Python list
#*Data structures
#? Using range function
#* the range function returns a list of numbers that range from 0 to one less than the parameter. It actually gives an array of indexes, simply put
print(range(4))
friends = ["Joseph", "Glenn", "Glenn", "Glenn", "Gill"]
print(range(len(friends)))
for friend in friends:
    print("happy new year:", friend)

#*in Python we have negatif indexes that allow us to iterate from the end of the list
friends = ["Joseph", "Kanna", "Shinozaki", "Glenn", "Gill"]
# if we want to iterate from the end, the index =-1
print(friends[-len(friends)])

print(friends[::-2])  # gonna print elements from the end with a step of 2

#*we can count the number of an element in the list with count()
friends = ["Joseph", "Glenn", "Glenn", "Glenn", "Gill"]
print(friends.count("Glenn"))

#*we can sort it
friends.sort()
print(friends)

#*we can append another list to a list with extend()
friends.extend([4, 8, 15, 16, 23])
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

#*when we assign a variable to a list, both refer to the same list adress
friend2=friends
#*that's why if we do something to friend2, changes will occurs to friends too
friend2.append("lala")
print(friend2)
print(friends)
#*to remediate to that we use some method like copy(), slicing
#friend2=friends.copy()
#friend2=friends[:]
#!creating a list of empty lists
#*with this method the same object (here an empty list) is duplicated 10 times
l1=[[]]*10
print(l1)
#*that's why eventhough we just modify the first element of our list
#*all elements get modified with the same value 1
l1[0].append(1)
print(l1)

#*to remediate to that problem we use the for loop method
##when we don't use a variable in a for loop we can simply replace it by "_"
l2=[[] for _ in range(10)]
print(l2)
l2[0].append(1)
print(l2)

#! enumerate function
for i,val in enumerate([5,3,4,1]):
    print(i,val)
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
l = line.split(";")
print(len(l))
print("\n")

#!Join() function
joined = " and ".join(l)
print(joined)
print("\n")
#!Another type of list:Deque(Double-ended queue)
#*Deques are generalisation of stacks and queues. They support thread-safe,memory efficient appends and pops from either side of deque
#*with approximately the same performance in either direction
#*Deque is faster than a list in terms of adding retrieving elements
#*must import it from collections
d = deque("hello")
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
d.rotate(-5)  # rotate from the left 5 times
print(d)
c = deque("yahoo", maxlen=5)
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
#delete an item of  list
del ddd["age"]
#*same thing like lists when we assigning a variable to a dictionary, both refer to the same dictionary address
#fff=ddd
#*so if we change fff's items, ddd's items will be changed as well
#*to remedeiate e can use the copy method

#*update 2 dictionaries
fff={"name":"mary","age":30,"course":188}
ddd.update(fff)
print(ddd)
#!Dictionnary literals
#*Another way to declare a dictionary they are like objects in javascript
#dictionary={key:expression for (key,value) in iterable}
print("Dictionnary literals:")
jjj = {
    "chuck": 1,
    "frad": 42,
    "jan": 100
}
print(jjj)
print(jjj.get("chuck"))  # this is an old way. Same as print(jjj["chuck"])
print(jjj.get("frad"))
print("\n")
cities_in_farenheit = {'new york': 32, "Boston": 75, "los angeles": 100}
cities_in_celsius = {key: round((value-32)*(5/9))
                     for (key, value) in cities_in_farenheit.items() if value != 100}
desc_cities = {key: ("warm" if value >= 45 else "cold")
               for (key, value) in cities_in_farenheit.items()}
print(cities_in_celsius)
print(desc_cities)
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
x = counts.get(name, 0)  # *0 is the default value if name not in counts

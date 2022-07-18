import json
import os
import smtplib
import ssl
import time  # (smtplib:simple mail transfert protocol library)
from contextlib import contextmanager
from email.message import EmailMessage
from itertools import (accumulate, combinations, cycle, groupby, permutations,
                       product, repeat)
from json import JSONEncoder
from multiprocessing import Array, Lock, Pool, Process, Value
from threading import Lock, Thread

#! the zip function
# *combines elements from two or more iterables(list,tuple,sets,etc)
# *create a zip object with paired elements stored in tuples for each element
usernames = ["Dude", "Bro", "Mister"]
passwords = ("pass", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords)
usersfull = zip(usernames, passwords, login_date)

'''
for i in users:
    print(i)
print(list(zip(usernames, passwords)))
userdict = dict(zip(usernames, passwords))
for key, value in userdict.items():
    print(key, ":", value)
for i in usersfull:
    print(i)
''' 

#!Threads
#*a flow of execution. Like a separate order of instructions.
#*it is a entity within a process
#*However each thread takes a turn running to achieve concurrency
#*threads share same memory data
##print the active_count of thread that is in charge of executing our program
#print(threading.active_count())

##print a list of all threads running
#*the main thread is in charge of running the main program
#print(threading.enumerate())
#!Multithreading
#*we can have many threads running concurrently but not truly in parallele by using the concept of multithreading
#*better for i/o bound tasks
"""
Advantages:
All hreads within a process share the same memory
Leightweight
Starting a thread is faster than starting a process

Disadvantages:
Limited by GIL: only one thread at the time
No effect for CPU-bound tasks
Not interruptable/killable
Careful with race conditions (occurs when 2 or more threads want to modify the same variable at the same time)

A GIL is global interpreter lock that allows only one thread at a time to execute
"""


def eat():
    time.sleep(3)
    print("you're eating")


def drink():
    time.sleep(3)
    print("you're drinking")


def study():
    time.sleep(3)
    print("you're studying")

#?whithout multithreading
#eat()
#drink()
#study()

#print(threading.active_count())
#print(threading.enumerate())


#?with multithreading
#*we create a thread that is in charge of each function
# generally we pass our parameters into args field
x = Thread(target=eat, args=())
#x.start()

y = Thread(target=drink, args=())
#y.start()

z = Thread(target=study, args=())
#z.start()

#print(threading.active_count())
#print(threading.enumerate())
#*the main thread will just create the 3 threads and immediately execute the next instruction which is to print active_count
#*then our 3 threads will start running

##threads accessing to the same data
#?2 threads that are accessing to the same data 
database_value=0
def increase(lock):
    global database_value
    ##with lock we can prevent another thread to access this code part at the same time
    ##it prevents race conditions
    with lock:
        local_copy=database_value
        local_copy+=1
        #? as we pause the execution here, the program will switch from thread1 to thread2 (database_value is still 0)
        #?therefore database_value didn't get changed, that's how a race condition occurs
        #?when thread2 will pause the program switch back to thread1 to complete its task
        #?and come back to thread2 to complete it also
        
        time.sleep(0.1)
        database_value=local_copy
        
if __name__ == "__main__":
    lock=Lock()
    print("start value",database_value)
    thread1=Thread(target=increase,args=(lock,))
    thread2=Thread(target=increase,args=(lock,))
    #?thread1 starts first until it finishes then thread2 starts
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    #? the output should display "end value 2" but displays instead "end value 1"
    #? this is because we have a race condition here: thread1 and thread2 both tried to modify database_value at the same time
    #?to prevent this we use Lock() 
    print("end value",database_value)
    print("end main")

#!thread synchronisation
#*we can have a calling thread (in this case the main thread) wait around for another thread to finish before it can move on

#x.join()#the main thread will wait till the thread 1 x finish
#y.join()#same thing here
#z.join()#so the main thread has to wait till these 3 threads complete their tasks

#print(threading.active_count())
#print(threading.enumerate())

#!daemon thread
#*a thread that runs in the background, not important for program to run
#*your program will not wait for daemon threads to complete before existing
#*daemon thread are killed as soon as the main thread complete its task(complete the main program)
#*non-daemon threads cannot be normally killed, stay alive till task is finished
#*usually used for background tasks


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


#* this normal thread will still running  even if after the main thread has completed its task
#x=threading.Thread(target=timer, args=())
#*to turn a normal thread into a daemon thread we set the flags daemon to true:
x = Thread(target=timer, args=(), daemon=True)
#x.start()

#answer=input("please enter your credentials: ")

#!Multiprocessing
#*a process can have multiple threads inside
#*running tasks in parallele on different cpu cores, bypass gil for thread
#*better for cpu bound tasks
"""
Advantage:
Takes advantage of multiple CPUs and cores
separate memory space (memory is not shared between processes)
New process is started independently from other processes
Processes are killable/interruptable
One GIL for each process (avoids GIL limitation)

Disadvantages:
Heavyweight
Starting a process is slower than starting a thred
More memory
IPC(inter-process communication) is more complicated    
"""
def cube(number):
    return number*number*number
def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)
def add_100(number,lock):
        for _ in range(100):
            time.sleep(0.1)
            with lock:
             number.value+=1
##how to share same public data to different processes
##we need to use special shared memory objects
if __name__ == "__main__":
  #  processes=[]
   # num_processes=os.cpu_count()

    #for _ in range(num_processes):
     #   p=Process(target=square_numbers)
      #  processes.append(p)

    #for p in processes:
     #   p.start()

    #for p in processes:
     #   p.join()
    #print("end main")

    #lock=Lock()
    #shared_number=Value("i",0) #i for integer
    #print("number  at beginning",shared_number.value)
    #*let's create 2 processes that will modify shared_number
    #p1=Process(target=add_100,args=(shared_number,lock))
    #p2=Process(target=add_100,args=(shared_number,lock))

    #p1.start()
    #p2.start()

    #p1.join()
    #p2.join()

    #?again a race condition will happen
    #? to prevent this we need Lock()
    #print("number at end",shared_number.value)
#!Process pool
#*a process pool can be used to manage multiple processes
#*it can manage the available number of processes for you and split data 
#*into smaller chunks,which can be then be processed in parallel
#*by different processses
    numbers=range(10)
    pool=Pool()
    #*this will automatically allocate the maximum number of available processes
    #*and create different processes and split this iterable into an equal size chunks
    #*and submit this to this function, so this function will now be executed in parallel
    result=pool.map(cube,numbers)
    pool.close()
    pool.join()
    print(result)

#!send an email(only works with gmail adress for now)
#*need to import smtplib

sender = "tanimoucisse@gmail.com"
receiver = "mahamadous22@gmail.com"
password = "candyccove456789"
subject = "Test with python"
body = "this mail was sent from vscode with python"

message = f"""From:{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender, password)
    print("loggin...")
    server.sendmail(sender, receiver, message)
    print("email has been sent successfully")
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate")

#*another way of sending email
message=EmailMessage()
message["From"]=sender
message["To"]=receiver
message["Subject"]=subject


#*if we want to send an email designed in html
html=f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
 </html>
"""
message.set_content(body)
#*set this when sending an html email:
#message.add_alternative(html,subtype="html")

#context=ssl.create_default_context()
#with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
 #   server.login(sender,password)
  #  server.sendmail(sender,receiver, message.as_string())

#!product from itertools
#*pattern: product(*iterables, repeat=(number))
#*Cartesian product of input iterables. Equivalent to nested for-loops
#*For example, product(A, B) returns the same as: ((x,y) for x in A for y in B).
#*The leftmost iterators are in the outermost for-loop, so the output tuples cycle
#*in a manner similar to an odometer (with the rightmost element changing on every iteration).
#*To compute the product of an iterable with itself, 
#*specify the number of repetitions with the optional repeat keyword argument.
#*For example, product(A, repeat=4) means the same as product(A, A, A, A).
#*product('ab', range(3)) - -> ('a', 0)('a', 1)('a', 2)('b', 0)('b', 1)('b', 2)
#*product((0, 1), (0, 1), (0, 1)) - -> (0, 0, 0)(0, 0, 1)(0, 1, 0)(0, 1, 1)(1, 0, 0) ...

a=[1,2]
b=[3]
prod=product(a,b,repeat=2) 
print(list(prod))

#!permutations
#*Return successive r-length permutations of elements in the iterable.
#*permutations(range(3), 2) - -> (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)
#*the second argument return the length of our permutations that we want it would be
a=[1,2,3,4]
perm=permutations(a,2)
print(list(perm)) 
print()
#!combinations
#*Return successive r-length combinations of elements in the iterable.
#*combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
#*the second argument return the length of our permutations that we want it would be
#*the difference between the permutations, here there's no repetions of elements. like (1,3) and(3,1), (2,4) and (4,2)
comb=combinations(a,2)
print(list(comb))
print()

#!accumulate function
#*Return series of accumulated sums (or other binary function results)
acc=accumulate(a)
print(list(acc))
print() 
#!groupby function
#*make an iterator that returns consecutive keys and groups from the iterable
#*iterable:Elements to divide into groups according to the key function.
#*key:A function for computing the group category for each element. If the key function is not specified or is None, the element itself is used for grouping.

groupe=groupby(a,key=lambda x: x < 3)
for key,value in groupe:
    print(key,list(value))

persons=[{"name":"Tim", "age":25},{"name":"John", "age":25}, {"name":"lisa", "age":27}, {"name":"claire", "age":28}]
groupe=groupby(persons,key=lambda x: x["age"])
for key, value in groupe:
    print(key, list(value))

#!cycle function
#for i in cycle(a):
 #   print(i)
  #  break
#!repeat function
for i in repeat(1,4):
    print(i) 

#!JSON
#*convert a dict to json format, also called serialization or encoding
#*need to import json
person={"name":"John","age":38,"city":"new york","hasChildren":False,"titles":["engineer","programmer"]}
#*we can specify the indent for better presentation of json object
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)
#*we can also convert it into a file
with open("person.json","w") as file:
    #*will create a json file with our dict converted into a json object
    json.dump(person,file,indent=4)

#*convert back a json object to a python dict, also called deserialization or decoding
person2=json.loads(personJSON)
print(person2)

#*from json file
with open("person.json","r") as file:
    person3=json.load(file)
    print(person3)

#*how to convet a class to a json object  
class User:
    def __init__(self, name, age):
      self.name = name
      self.age = age

user=User("Max",37)
#*we need a custome encoding function that will convert the class to a dict,to help the dumps() function
def encode_user(object):
    if isinstance(object,User):
        return {"name":object.name,"age":object.age,object.__class__.__name__:True}
    else:
        raise TypeError("Object type User is not JSON serializable")
#*and we specify the function to be run as default when encoding   
userJSON=json.dumps(user,default=encode_user)
print(userJSON)

##another way
#*need to import JSONEncoder from json

class UserEncoder(JSONEncoder):
    #*we overwrite the default encoder function:
    def default(self,object):
        if isinstance(object, User):
           return {"name": object.name, "age": object.age, object.__class__.__name__: True}
       #*will encode every other type of object as usually
        return JSONEncoder.default(self,object)
#*and instead of specifying the default function to be used, we specify the class to be used
userJSON2=json.dumps(user,cls=UserEncoder)
print(userJSON2)

#*convert back to a user object
#need to convert first in dict and then to a class object
def decode_user(dict):
    #*check if our dict contain an user object by checking the name of our class User
    if User.__name__ in dict:
        #*then we create the object
        return User(name=dict["name"],age=dict["age"])
    #*otherwise simply return the dict
    return dict
#will return back an user object if userJSON was converted from an user object, else retun simply a dict as usually
usr2=json.loads(userJSON,object_hook=decode_user)
print(usr2.name)

#!generators
#*generators are functions that return an object tha can be iterated over
#*they generate items inside the object, only one at the time and only when you ask for it
#*they are much more memory efficient than other sequence objects
#*they are defined like a normal function but with the yield keyword intead of the return keyword
#*therefore we can return many times and we don't quit the function

def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    
g=mygenerator()
#for i in g:
 #   print(i)
#*we can also get the values one at the time with next function

val=next(g)
print(val)
val=next(g)
print(val)
val = next(g)
print(val)
print(sorted(g))

def countdown(num):
    print("starting")
    while num>0:
        yield num
        num-=1
cd =countdown(10)
print(next(cd))
print(next(cd))
print(next(cd))

#*big advantage of generators: memory efficiency
##this function down here takes much memory
def firstn(n):
    nums=[]
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

##while this function down here takes less but do the same thing than the function up here
def firstn_generator(n):
    num=0
    while num<n:
        yield num
        num+=1
        
print(sum(firstn(10)))
print(sum(firstn_generator(10)))

#*generators expressions: the same as list comprehension but with parentheses instead of brackets
mygeneraor=(i for i in range(10) if i%2==0) #generator expression
mylist=[i for i in range(10) if i%2==0] #list comprehension
#*we can convert a generator object to a list
mylist2=list(mygeneraor)
print(next(mygeneraor))
print(next(mygeneraor))
for i in mygeneraor:
    print(i)

#!context managers
#*great tool for resource management
#*it's caracterized with "with" statement
#*we can create our own context managers with class or functions

##with class
class ManagedFile:
    def __init__(self, filename):
      self.filename = filename
    
    #*the enter method will be executed as soon as we enter the with statement
    def __enter__(self):
        print("enter")
        self.file=open(self.filename,"w")
        return self.file
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
            print("exc: ",exc_type,exc_value)
        print("exit")
       

with ManagedFile("notebook.txt") as f:
    print("do some stuffs")
    f.write("haha")
    f.dosomething()
print("continuing")

##with function
#*we need to import contextmanager from contextlib and use it as a decorator
@contextmanager
def open_manager(filename):
    f=open(filename,"w")
    try:
        yield f
    finally:
        f.close()
with open_manager("notebook.txt") as f:
    f.write("hahahaha")
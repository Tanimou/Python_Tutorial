import threading
import time
from multiprocessing import Process, cpu_count

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
#*However each thread takes a turn running to achieve concurrency
##print the active_count of thread that is in charge of executing our program
#print(threading.active_count())

##print a list of all threads running
#*the main thread is in charge of running the main program
#print(threading.enumerate())
#!Multithreading
#*we can have many threads running concurrently but not truly in parallele by using the concept of multithreading
#*better for i/o bound tasks


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
x = threading.Thread(target=eat, args=())
#x.start()

y = threading.Thread(target=drink, args=())
#y.start()

z = threading.Thread(target=study, args=())
#z.start()

#print(threading.active_count())
#print(threading.enumerate())
#*the main thread will just create the 3 threads and immediately execute the next instruction which is to print active_count
#*then our 3 threads will start running

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
x = threading.Thread(target=timer, args=(), daemon=True)
#x.start()

#answer=input("please enter your credentials: ")

#!Multiprocessing
#*running tasks in parallele on different cpu cores, bypass gil for thread
#*better for cpu bound tasks


def counter(number):
    count = 0
    while count < number:
        count += 1


def main():
    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

   # a.join()
    #b.join()
    #c.join()
    #d.join()

    print("finished in: ", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()

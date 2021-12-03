from operator import index
from tkinter import *

#!GUI: Graphical User Interface in python
#*this part requires tkinter
#*widgets:GUI elements like buttons,textboxes,labels
#*windows:serves as a container to hold or contain these widgets

windows=Tk()#instanciate an object of a windows from the class Tk
#*changing the size of our windows
#windows.geometry("400x200")

#*changing the title of the windows
#windows.title("Graphical User Interface in Python")

#*Changing the titlebar icon of the windows(works only with png images)
icon=PhotoImage(file="zeref.png")
#windows.iconphoto(True,icon)

#*changing the background of the windows
#windows.config(background="white")
#windows.config(background="#5cfcff")

#!labels
#*an area widget that holds text and/or an image within a window
#windows=Tk()

photo1 = PhotoImage(file="midoriya.png")
label=Label(windows,
            text="hey there",
            font=("Arial",40,"bold"),
            fg="green",#fg stands for forground
            bg="black",#bg stands for background
            relief=RAISED,#relief is for border
            bd=10,#bd is for amount of border
            padx=20,#is for padding on the x axis(horizontal)
            pady=20,#is for padding on the y axis(vetical)
           # image=photo1,
            #compound="bottom",#compound will place the image a the bottom, top, left or right of the text
            ) 

#label.pack()
#label.place(x=20,y=0)

#!buttons
#windows=Tk()

count=0
def click():
    global count
    count+=1
    print("you clicked ",count,"times")

button=Button(windows,
              text="click me",
              command=click,#function that will be executed when clicked
              font=("Comic Sans",30),
              fg="green",
              bg="black",
              activeforeground="green",
              activebackground="black",
             # state=DISABLED, #to disable the button
            # image=photo1,
             #compound="top"
              )
#button.pack()


#!Entry box
#*textbox that accepts a single line of user input
#windows=Tk()

def submit():
    username=entry.get()
    #*disable the entry box after typing some text
    entry.config(state=DISABLED)
    print("hello "+username)
    
def delete():
    entry.delete(0,END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)

#*this is a constructor of our entry box
entry=Entry(windows,
            font=("Arial",50),
            fg="green",
            #bg="black",
            show="*"#instead of showing the text that are typing, "*" will be shown. Very useful for hidding password for example
            )
##we can also define some configuration after the constructor like this:
#entry.config(show="*")

#*inserting some default text
#entry.insert(0,"sponge bob")

#entry.pack(side=LEFT)

submit=Button(windows,text="submit",command=submit)
#submit.pack(side=RIGHT)

delete = Button(windows, text="delete", command=delete)
#delete.pack(side=RIGHT)

backspace = Button(windows, text="backspace", command=backspace)
#backspace.pack(side=RIGHT)

#!checkbox
#windows=Tk()
def display():
    if(x.get()==1):
        print("you checked this")
    else:
        print("you unchecked this")
    
x= IntVar()#create an in variable but not setted
photo = PhotoImage(file="python2.png")
check_button=Checkbutton(windows, 
                         text="check this button",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font=("Arial",20),
                         image=photo,
                         compound="left",
                         )

#check_button.pack()

#!radio buttons
#*similar to checkbox but you can only select one from a group
#windows=Tk()

food=["pizza","hamburger","hotdog"]
pizzaImage=PhotoImage(file="pizza.png")
hamburgerImage=PhotoImage(file="hamburger.png")
hotdogImage=PhotoImage(file="hotdog.png")
foodImages=[pizzaImage,hamburgerImage,hotdogImage]
food = dict(zip(food, foodImages))
x=StringVar()
def display2():
   if(x.get()=="pizza"):
       print("here's your pizza")

   if(x.get() == "hamburger"):
       print("here's your hamburger")
       
   if(x.get()=="hotdog"):
       print("here's your hotdog")
   
    
for k,v in food.items():
    radiobutton = Radiobutton(windows, text=k,
                              variable=x,#group radio buttons together if they share the same variable
                              value=k,#assigns each radio button a different value
                              image=v,
                              compound="left",
                              command=display2,
                              indicatoron=0,#eliminate circle indicators
                              width=375,#set width of radio buttons
                              )
#    radiobutton.pack(anchor=W) #to place radio buttons to the left
#!scale
#windows=Tk()
def submit():
    print("temperature:",scale.get())
scale=Scale(windows,from_=100,
            to=0,
            tickinterval=10,
            length=600,
            showvalue=0,
            resolution=5,
            troughcolor="#69eaff")
scale.set(50)
button=Button(windows,text="submit",command=submit)

#scale.pack()
#button.pack()

#!listbox
#*a listing of selectable text items within its own container
#windows=Tk()
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
  #  listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

def submit():
        food=[]
        for index in listbox.curselection():
            food.insert(index,listbox.get(index))
        print("you ordered:")
        for index in food:
            print(index)
            
listbox=Listbox(windows,
                bg="#f7ffde",
                width=12,
                font=("Arial",35),
                selectmode=MULTIPLE,
                )

listbox.insert(1,"pizza")
listbox.insert(2, "pizza")
listbox.insert(3, "pizza")


entrybox=Entry(windows)
add=Button(windows,text="add",command=add)
delete = Button(windows, text="delete", command=delete)
submit=Button(windows, text="submit", command=submit)

listbox.pack()
entrybox.pack()
add.pack()
delete.pack()
submit.pack()
windows.mainloop()  # create a windows on computer screen, listen for events

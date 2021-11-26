from tkinter import *

#!GUI: Graphical User Interface in python
#*this part requires tkinter
#*widgets:GUI elements like buttons,textboxes,labels
#*windows:serves as a container to hold or contain these widgets

windows=Tk()#instanciate an object of a windows from the class Tk
#*changing the size of our windows
windows.geometry("400x200")

#*changing the title of the windows
windows.title("Graphical User Interface in Python")

#*Changing the titlebar icon of the windows(works only with png images)
icon=PhotoImage(file="zeref.png")
windows.iconphoto(True,icon)

#*changing the background of the windows
windows.config(background="white")
#windows.config(background="#5cfcff")

#!labels
#*an area widget that holds text and/or an image within a window
photo = PhotoImage(file="midoriya.png")
label=Label(windows,
            text="hey there",
            font=("Arial",40,"bold"),
            fg="green",#fg stands for forground
            bg="black",#bg stands for background
            relief=RAISED,#relief is for border
            bd=10,#bd is for amount of border
            padx=20,#is for padding on the x axis(horizontal)
            pady=20,#is for padding on the y axis(vetical)
           # image=photo,
            #compound="bottom",#compound will place the image a the bottom, top, left or right of the text
            ) 

#label.pack()
#label.place(x=20,y=0)

#!buttons
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
            # image=photo,
             #compound="top"
              )
button.pack()
windows.mainloop()#create a windows on computer screen, listen for events

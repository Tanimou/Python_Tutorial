# from tkinter.ttk import *
import time
from heapq import heappush
from operator import index
from textwrap import wrap
from tkinter import *
from tkinter import colorchooser, filedialog, messagebox, ttk

from ball import Ball

#!GUI: Graphical User Interface in python
# *this part requires tkinter
# *widgets:GUI elements like buttons,textboxes,labels
# *windows:serves as a container to hold or contain these widgets

windows = Tk()  # instanciate an object of a windows from the class Tk
# *changing the size of our windows
# windows.geometry("400x200")

# *changing the title of the windows
# windows.title("Graphical User Interface in Python")

# *Changing the titlebar icon of the windows(works only with png images)
icon = PhotoImage(file="images/zeref.png")
# windows.iconphoto(True,icon)

# *changing the background of the windows
# windows.config(background="white")
# windows.config(background="#5cfcff")

# windows.mainloop()

#!labels
# *an area widget that holds text and/or an image within a window
# windows=Tk()

photo1 = PhotoImage(file="images/midoriya.png")

label = Label(
    windows,
    text="hey there",
    font=("Arial", 40, "bold"),
    fg="green",  # fg stands for forground
    bg="black",  # bg stands for background
    relief=RAISED,  # relief is for border
    bd=10,  # bd is for amount of border
    padx=20,  # is for padding on the x axis(horizontal)
    pady=20,  # is for padding on the y axis(vetical)
    # image=photo1,
    # compound="bottom",#compound will place the image a the bottom, top, left or right of the text
)


# label.pack()
# label.place(x=20,y=0)

# windows.mainloop()

#!buttons
# windows=Tk()

count = 0


def click():
    global count
    count += 1
    print("you clicked ", count, "times")


button = Button(
    windows,
    text="click me",
    command=click,  # function that will be executed when clicked
    font=("Comic Sans", 30),
    fg="green",
    bg="black",
    activeforeground="green",
    activebackground="black",
    # state=DISABLED, #to disable the button
    # image=photo1,
    # compound="top"
)
# button.pack()

# windows.mainloop()

#!Entry box
# *textbox that accepts a single line of user input
# windows=Tk()


def submit():
    username = entry.get()
    # *disable the entry box after typing some text
    # entry.config(state=DISABLED)
    print(f"hello {username}")


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


# *this is a constructor of our entry box
entry = Entry(
    windows,
    font=("Arial", 10),
    fg="green",
    # bg="black",
    show="*",  # instead of showing the text that are typing, "*" will be shown. Very useful for hidding password for example
)
##we can also define some configuration after the constructor like this:
# entry.config(show="*")

# *inserting some default text
# entry.insert(0,"sponge bob")

# entry.pack(side=LEFT)

submit = Button(windows, text="submit", command=submit)
# submit.pack(side=RIGHT)

delete = Button(windows, text="delete", command=delete)
# delete.pack(side=RIGHT)

backspace = Button(windows, text="backspace", command=backspace)
# backspace.pack(side=RIGHT)

# windows.mainloop()

#!checkbox
# windows=Tk()


def display():
    if x.get() == 1:
        print("you checked this")
    else:
        print("you unchecked this")


x = IntVar()  # create an in variable but not setted
photo = PhotoImage(file="images/python2.png")
check_button = Checkbutton(
    windows,
    text="check this button",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    image=photo,
    compound="left",
)

# check_button.pack()

# windows.mainloop()

#!radio buttons
# *similar to checkbox but you can only select one from a group
# windows=Tk()

food = ["pizza", "hamburger", "hotdog"]
pizzaImage = PhotoImage(file="images/pizza.png")
hamburgerImage = PhotoImage(file="images/hamburger.png")
hotdogImage = PhotoImage(file="images/hotdog.png")
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
food = dict(zip(food, foodImages))
x = StringVar()


def display2():
    if x.get() == "pizza":
        print("here's your pizza")

    if x.get() == "hamburger":
        print("here's your hamburger")

    if x.get() == "hotdog":
        print("here's your hotdog")


for k, v in food.items():
    radiobutton = Radiobutton(
        windows,
        text=k,
        variable=x,  # group radio buttons together if they share the same variable
        value=k,  # assigns each radio button a different value
        image=v,
        compound="left",
        command=display2,
        indicatoron=0,  # eliminate circle indicators
        width=375,  # set width of radio buttons
    )
#    radiobutton.pack(anchor=W) #to place radio buttons to the left

# windows.mainloop()

#!scale
# windows=Tk()
def submit():
    print("temperature:", scale.get())


scale = Scale(
    windows,
    from_=100,
    to=0,
    tickinterval=10,
    length=600,
    showvalue=0,
    resolution=5,
    troughcolor="#69eaff",
)
scale.set(50)
button = Button(windows, text="submit", command=submit)

# scale.pack()
# button.pack()

# windows.mainloop()
#!listbox
# *a listing of selectable text items within its own container
# windows=Tk()
def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())


def delete():
    #  listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("you ordered:")
    for index in food:
        print(index)


listbox = Listbox(
    windows,
    bg="#f7ffde",
    width=12,
    font=("Arial", 35),
    selectmode=MULTIPLE,
)

listbox.insert(1, "pizza")
listbox.insert(2, "pizza")
listbox.insert(3, "pizza")

entrybox = Entry(windows)
add = Button(windows, text="add", command=add)
delete = Button(windows, text="delete", command=delete)
submit = Button(windows, text="submit", command=submit)


# listbox.pack()
# entrybox.pack()
# add.pack()
# delete.pack()
# submit.pack()

# windows.mainloop()

#!message box
# windows=Tk()
def click():
    #  messagebox.showinfo(title="info",message="you clicked me")
    # messagebox.showwarning(title="Attention", message="A virus has been detected")
    # messagebox.showerror(title="Error", message="Something went wrong")
    """
    if messagebox.askokcancel(title="ask", message="Are you sure about that?"):
        print("got it")
    else:
        print("canceling")
    """
    """
  if messagebox.askretrycancel(title="ask", message="Are you sure about that?"):
      print("got it")
  else:
      print("canceling")
  """
    """
  if messagebox.askyesno(title="ask", message="Are you sure about that?"):
      print("got it")
  else:
      print("canceling")
  """
    # print(messagebox.askquestion(title="question", message="Are you sure about that?"))
    print(
        messagebox.askyesnocancel(title="question", message="Are you sure about that?")
    )


clickme = Button(windows, text="click me", command=click)
# clickme.pack()

# windows.mainloop()

#!color chooser
# windows=Tk()
def click():
    windows.config(bg=colorchooser.askcolor()[1])


windows.geometry("420x420")
button = Button(text="click me", command=click)
# button.pack()
# windows.mainloop()  # create a windows on computer screen, listen for events

#!Text widget
# *functions like a text area, you can enter multiple line of text
# windows=Tk()
def submit():
    input = text.get("1.0", END)
    print(input)


text = Text(
    windows,
    bg="light yellow",
    font=("Ink Free", 25),
    height=8,
    width=20,
    padx=20,
    pady=20,
    fg="purple",
)
# text.pack()
button = Button(text="submit", command=submit)
# button.pack()
# windows.mainloop()

#!File dialog
# windows=Tk()
# *open a file
def openFile():
    filepath = filedialog.askopenfilename(
        title="open a file", filetypes=(("text files", "*.txt"), ("all files", "*.*"))
    )
    with open(filepath, "r") as file:
        print(file.read())


button = Button(text="open", command=openFile)
# button.pack()

# *save a file
def Save():
    file = filedialog.asksaveasfile(
        initialdir="C:\\Users\\tanim\\Programmation projects\\Tutorials\\Python_Tutorial",
        defaultextension=".txt",
        filetypes=(
            ("Text file", ".txt"),
            ("PDF document", ".pdf"),
            ("Html file", ".html"),
            ("all files", ".*"),
        ),
    )
    filetext = str(text.get("1.0", END))
    file.write(filetext)
    file.close()


button1 = Button(text="save", command=Save)
# button1.pack()
text = Text(windows)
# text.pack()
# windows.mainloop()

#!Menu bar
# windows=Tk()
"""
def cut():
    pass
def copy():
    pass
def paste():
    pass

menubar=Menu(windows)
windows.config(menu=menubar)

#*to add a file menu to our menubar
fileMenu=Menu(menubar,tearoff=0)
#*to have a dropdown menu effect to our file menu
menubar.add_cascade(label="File",menu=fileMenu)
#*to add command to our dropdown fileMenu
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=Save)
#*to add a separator
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

#*to add an edit menu to our menubar
editMenu=Menu(menubar,tearoff=0)
#*to have a dropdown menu effect to our edit menu
menubar.add_cascade(label="Edit", menu=editMenu)
#*to add command to our dropdown editMenu
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

text = Text(windows,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple",)
text.pack()
windows.mainloop()
"""
#!Frame
# windows=Tk()
# frame=Frame(windows)
# frame.pack(fill=BOTH,expand=1)

# windows.mainloop()


#!scrollbar
# windows=Tk()
# frame=Frame(windows)
# frame.pack()

# label=Label(frame, text="Scroll Bar")
# label.pack()

# yscrollbar=Scrollbar(frame,orient=VERTICAL)
# yscrollbar.pack(side=RIGHT,fill=Y)

# xscrollbar=Scrollbar(frame,orient=HORIZONTAL)
# xscrollbar.pack(side=BOTTOM,fill=X)

# listbox=Listbox(frame,width=30,yscrollcommand=yscrollbar.set)
# for val in range(100):
#   listbox.insert(END,"Value: "+str(val))
# listbox.pack(pady=5)
# yscrollbar.config(command=listbox.yview)

# text=Text(frame,yscrollcommand=yscrollbar.set,
#         xscrollcommand=xscrollbar.set,
#        wrap=NONE)
# text.pack()

# yscrollbar.config(command=text.yview)
# xscrollbar.config(command=text.xview)
# windows.mainloop()

#!combo box
# windows=Tk()
frame = Frame(windows, width=200, height=200)
# frame.pack()
viewlist = ["option1", "option2", "option3", "option4"]
# combo=ttk.Combobox(frame,values=viewlist)
# *put some default value
# combo.set("option1")
# combo.place(x=30,y=50)
# windows.mainloop()

#!New window
def create_window():
    # *Toplevel(): a new window "on top" of other windows, linked to a "bottom" window
    # *different to Tk() which creates a new window that is not linked
    new_window = Toplevel()
    # new_window=Tk()
    # windows.destroy()


# windows=Tk()
# button=Button(windows,text="create a new window",command=create_window).pack()
# windows.mainloop()

#!Windows Tab
# *need to import ttk library from tkinter
# windows=Tk()
# *Notebook: a widget that manages a collection of windows/displays
# notebook=ttk.Notebook(windows)
# tab1=Frame(notebook)
# tab2=Frame(notebook)
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both")

# Label(tab1,text="hello this is tab1",width=50,height=25).pack()
# Label(tab2,text="hello this is tab2",width=50,height=25).pack()

# windows.mainloop()

#!Progress bar
# *need to import ttk library from tkinter like this:from tkinter.ttk import *
# *and also time
def start():
    for x, _ in enumerate(range(100), start=1):
        time.sleep(0.05)
        bar["value"] += (1 / 100) * 100
        percent.set(f"{int((x/100)*100)}%")
        windows.update_idletasks()  # to update, refresh the window


# windows=Tk()
percent = StringVar()
bar = ttk.Progressbar(windows, orient=HORIZONTAL, length=300)
# bar.pack(pady=10)
percentLbel = Label(windows, textvariable=percent).pack()
# button = Button(windows, text="Download",command=start).pack()
# windows.mainloop()

#!key event
def dosomething(event):
    print(f"you taped {event.keysym}")


# windows=Tk()
# *when tapping any key
# windows.bind("<Key>",dosomething)
# windows.mainloop()

#!Mouse events
def do_click(event):
    print("you left clicked ")


# windows=Tk()
# *when left click on a mouse button
# windows.bind("<Button-1>",do_click)
# *when clicked on the scroll wheel  of the mouse
# windows.bind("<Button-2>", do_click)
# *when right click on a mouse button
# windows.bind("<Button-3>", do_click)
# *when release a button on a mouse
# windows.bind("<ButtonRelease>", do_click)
# *when entering the window
# windows.bind("<Enter>", do_click)
# *when leaving the window
# windows.bind("<Leave>", do_click)
# *when moving the mouse
# windows.bind("<Motion>",do_click)
# windows.mainloop()

#!Drag and Drop
def drag_start(event):
    # *make the function compatible with any widget
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


# windows=Tk()
label = Label(windows, bg="red", width=18, height=5)
# label.place(x=0,y=0)

label2 = Label(windows, bg="blue", width=18, height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# *when holding the left mouse button and dragging
# label.bind("<B1-Motion>", drag_motion)

# label2.bind("<Button-1>", drag_start)
# *when holding the left mouse button and dragging
# label2.bind("<B1-Motion>", drag_motion)
# windows.mainloop()

#!moving image/widget with keys
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 1)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 1)


def move_left(event):
    label.place(x=label.winfo_x() - 1, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 1, y=label.winfo_y())


# windows=Tk()
# windows.geometry("500x500")
# windows.bind("<z>",move_up)
# windows.bind("<s>",move_down)
# windows.bind("<q>",move_left)
# windows.bind("<d>", move_right)
# label=Label(windows,bg="red",width=18,height=5)
# label.place(x=0,y=0)
# windows.mainloop()

#!multiple animation
# *we're going to create a class for simplicity in another file
# windows=Tk()
WIDTH = 500
HEIGHT = 500
"""
canvas=Canvas(windows,width=WIDTH,height=HEIGHT)
canvas.pack()
volley=Ball(canvas,0,0,100,1,1,"red")
tennis=Ball(canvas,0,0,50,4,3,"yellow")
basket=Ball(canvas,0,0,30,6,6,"blue")
yoyo=Ball(canvas,0,0,150,0.5,0.5,"green")
black=Ball(canvas,0,0,20,8,8,"black")
while True:
    volley.move()
    tennis.move()
    basket.move()
    yoyo.move()
    black.move()
    windows.update()
    time.sleep(0.01)
windows.mainloop()
"""
#!clock program
def update():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, update)


# windows=Tk()
time_label = Label(windows, font=("Arial,50"), fg="red", bg="black")
# time_label.pack()
# update()
# windows.mainloop()

#!py to exe
# *install pyinstaller: pip install pyinstaller
# *create a folder and add any relevant files you need to create the programm(.py files, images ...)
# *open a command prompt and navigate to that folder
# *execute this: pyinstaller -F -w -i (name of the image).ico (name of the python file.py)
# *the image must be in ico format when using -i option for icon

#!calculator
def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    try:
        global equation_text
        # *will evaluate our equation
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (ZeroDivisionError, SyntaxError):
        equation_label.set("Error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


# windows=Tk()
windows.title("Calculator")
windows.geometry("500x500")
equation_text = ""
equation_label = StringVar()
label = Label(
    windows,
    textvariable=equation_label,
    font=("consolas", 20),
    bg="white",
    width=24,
    height=2,
)
label.pack()
frame = Frame(windows)
frame.pack()

button1 = Button(
    frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1)
)
button1.grid(row=0, column=0)

button2 = Button(
    frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2)
)
button2.grid(row=0, column=1)

button3 = Button(
    frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3)
)
button3.grid(row=0, column=2)

button4 = Button(
    frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4)
)
button4.grid(row=1, column=0)

button5 = Button(
    frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5)
)
button5.grid(row=1, column=1)

button6 = Button(
    frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6)
)
button6.grid(row=1, column=2)

button7 = Button(
    frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7)
)
button7.grid(row=2, column=0)

button8 = Button(
    frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8)
)
button8.grid(row=2, column=1)

button9 = Button(
    frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9)
)
button9.grid(row=2, column=2)

button0 = Button(
    frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0)
)
button0.grid(row=3, column=0)

plus = Button(
    frame, text="+", height=4, width=9, font=35, command=lambda: button_press("+")
)
plus.grid(row=0, column=3)

minus = Button(
    frame, text="-", height=4, width=9, font=35, command=lambda: button_press("-")
)
minus.grid(row=1, column=3)

multiply = Button(
    frame, text="*", height=4, width=9, font=35, command=lambda: button_press("*")
)
multiply.grid(row=2, column=3)

divide = Button(
    frame, text="/", height=4, width=9, font=35, command=lambda: button_press("/")
)
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(
    frame, text=".", height=4, width=9, font=35, command=lambda: button_press(".")
)
decimal.grid(row=3, column=1)

clear = Button(windows, text="clear", height=4, width=9, font=35, command=clear)
clear.pack()

windows.mainloop()

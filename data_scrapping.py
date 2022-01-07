
from pyxlsb import open_workbook
from tkinter import *
from tkinter import filedialog,ttk
from collections import Counter

windows = Tk()
windows.geometry("800x800")

def scrapping():
    filepath = filedialog.askopenfilename(title="open a file",filetypes=(("xlsb files", "*.xlsb"), ("all files", "*.*")))
    with open_workbook(filepath) as wb:
     
        Prospect_list={}
        Week_list = []
        last_list = []
        Despatched_list = {}
        Assayed_list={}
        
        with wb.get_sheet("Samples Data") as sheet1:
            liste1=list(sheet1.rows())
            #!getting the list of prospect and the number of samples
            for col in range(len(liste1[0])):
                r,c,v=liste1[0][col]
                if v =="PROSPECT":
                    liste2 = liste1[1:]
                     #*despnum
                    i = c+6
                        #*assaymonth
                    s=c+16
                    for item in liste2:
                        v = item[c][2]
                        f = item[i][2]
                        g=item[s][2]
                        
                        if v is None:
                            continue
                        else:
                            v=v.upper()
                            Prospect_list[v] = Prospect_list.get(v, 0)+1
                        #!getting the number of samples per prospect in the samples data sheet
                        if f is None:
                                continue
                        else:
                            
                                Despatched_list[v] = Despatched_list.get(v, 0)+1
                        #!getting the number of sample assayed
                        if g=="":
                            
                            continue
                        else:
                        
                                Assayed_list[v] =Assayed_list.get(v, 0)+1
            print(Despatched_list)
            print()
            print(Assayed_list)

        var = StringVar(second_frame, value=Prospect_list[list(Prospect_list)[0]])   
        var2 = StringVar(second_frame, value=Despatched_list[list(Despatched_list)[0]])
        var3 = StringVar(second_frame, value=Assayed_list[list(Assayed_list)[0]])
        
           
        with wb.get_sheet("Setup") as sheet1:
            liste1 = list(sheet1.rows())
            
            for col in range(len(liste1[0])):
                    r, c, v = liste1[0][col]
                    if v == "Prospect_Name":
                        liste2=liste1[1:]
                        for item in liste2:
                            r, g, v = item[c]
                            if v is None:
                                continue
                            else:
                                last_list.append(v)
                    #!getting the week
                    if v == "Month":
                        for item in liste1:
                            r, g, v = item[c]
                            if v is None:
                                continue
                            else:
                                Week_list.append(v)

       
        for name in last_list:
            Prospect_list[name] = 0 if name not in list(Prospect_list) else Prospect_list[name]
            Despatched_list[name] = 0 if name not in list(Despatched_list) else Despatched_list[name]
            Assayed_list[name] = 0 if name not in list(Assayed_list) else Assayed_list[name]
   
        str = StringVar(second_frame, value=list(Prospect_list)[0])
        #!getting the number of sample despatched per prospect in the samples data sheet
        #for name in Prospect_list:
            #counts[name] = 0 if name not in counts else counts[name]
            
    #def update():
    def update(value):
              
        var.set(Prospect_list[value])
        var2.set(Despatched_list[value])
        if value not in Assayed_list:
            Assayed_list[value]=0
        var3.set(Assayed_list[value])

    
    combo = OptionMenu(second_frame,str,*list(Prospect_list),command=update)
   # combo = ttk.Combobox(second_frame, values=Prospect_list, state="readonly")
    combo1 = ttk.Combobox(second_frame, values=Week_list, state="readonly")
    #*put some default value
    #combo.set(Prospect_list[1])
    combo1.set(Week_list[1])
    #*place with grid
    combo.grid(row=300,column=300)
    combo1.grid(row=300,column=600,padx=30,pady=30)
    #str.set(counts[combo.get()])
    
         
    #to get the value of the combo: combo.get()

    sampleNumber_label = Label(second_frame,
                               text="Samples Number",
                               font=("Arial", 10, "bold"),
                               fg="red",  # fg stands for forground
                               bg="White",  # bg stands for background

                               bd=5,  # bd is for amount of border
                               # is for padding on the x axis(horizontal)
                               padx=5,
                               pady=5  # is for padding on the y axis(vetical)

                               )

    SamplesData_label = Label(second_frame,
                              textvariable=var,
                              font=("Arial", 10, "bold"),
                              fg="white",  # fg stands for forground
                              bg="red",  # bg stands for background

                              bd=5,  # bd is for amount of border
                              # is for padding on the x axis(horizontal)
                              padx=5,
                              pady=5  # is for padding on the y axis(vetical)
                              # image=photo1,
                              #compound="bottom",#compound will place the image a the bottom, top, left or right of the text
                              )
    

    sampleDespatched_label = Label(second_frame,
                               text="Samples Despatched",
                               font=("Arial", 10, "bold"),
                               fg="red",  # fg stands for forground
                               bg="White",  # bg stands for background

                               bd=5,  # bd is for amount of border
                               # is for padding on the x axis(horizontal)
                               padx=5,
                               pady=5  # is for padding on the y axis(vetical)
                              
                               )
    
    SamplesDespaNumber_label = Label(second_frame,
                              textvariable=# str,
                              var2,
                              font=("Arial", 10, "bold"),
                              fg="white",  # fg stands for forground
                              bg="red",  # bg stands for background

                              bd=5,  # bd is for amount of border
                              # is for padding on the x axis(horizontal)
                              padx=5,
                              pady=5  # is for padding on the y axis(vetical)
                              # image=photo1,
                              #compound="bottom",#compound will place the image a the bottom, top, left or right of the text
                              )
    sampleAssayed_label = Label(second_frame,
                                   text="SamplesAssayed",
                                   font=("Arial", 10, "bold"),
                                   fg="red",  # fg stands for forground
                                   bg="White",  # bg stands for background

                                   bd=5,  # bd is for amount of border
                                   # is for padding on the x axis(horizontal)
                                   padx=5,
                                   # is for padding on the y axis(vetical)
                                   pady=5

                                   )

    SamplesAssayNumber_label = Label(second_frame,
                                     textvariable=  # str,
                                     var3,
                                     font=("Arial", 10, "bold"),
                                     fg="white",  # fg stands for forground
                                     bg="red",  # bg stands for background

                                     bd=5,  # bd is for amount of border
                                     # is for padding on the x axis(horizontal)
                                     padx=5,
                                     # is for padding on the y axis(vetical)
                                     pady=5
                                     # image=photo1,
                                     #compound="bottom",#compound will place the image a the bottom, top, left or right of the text
                                     )
    
    week_label = Label(second_frame,
                   text="Weekly Stats",
                   font=("Arial", 10, "bold"),
                   fg="red",  # fg stands for forground
                   bg="White",  # bg stands for background

                   bd=5,  # bd is for amount of border
                   padx=5,  # is for padding on the x axis(horizontal)
                   pady=5  # is for padding on the y axis(vetical)
                   
                   )
    
    sampleNumber_label.grid(row=250,column=900,pady=50)
    SamplesData_label.grid(row=300,column=900,pady=50)
   # SamplesData_label.pack()
   
    sampleDespatched_label.grid(row=250,column=1080,padx=10,pady=50)
    SamplesDespaNumber_label.grid(row=300,column=1080,pady=50)
    
    sampleAssayed_label.grid(row=250, column=2080, padx=10, pady=50)
    SamplesAssayNumber_label.grid(row=300, column=2080, pady=50)
    
    week_label.grid(row=250,column=400,pady=50)
    #week_label.place(x=470, y=250)
    
    
    
#*main frame
frame = Frame(windows)

label = Label(frame,
              text="Data Scrapping",
              font=("Arial", 40, "bold"),
              fg="green",  # fg stands for forground
              bg="White",  # bg stands for background

              bd=10,  # bd is for amount of border
              padx=20,  # is for padding on the x axis(horizontal)
              pady=20,  # is for padding on the y axis(vetical)
              
              )
frame.pack(fill=BOTH,expand=1)
label.pack()
button = Button(frame, text="open a file for scrapping", command=scrapping)
button.pack()

#!scrollbar   
#canvas=Canvas(frame)
#canvas.pack(side=LEFT,fill=BOTH,expand=1)

#yscrollbar = Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
yscrollbar=Scrollbar(frame,orient=VERTICAL)
yscrollbar.pack(side=RIGHT,fill=Y)

#xscrollbar = Scrollbar(frame, orient=HORIZONTAL,command=canvas.xview)
xscrollbar=Scrollbar(frame,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM,fill=X)

#canvas.configure(yscrollcommand=yscrollbar.set)
#canvas.configure(xscrollcommand=xscrollbar.set)
#canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas=Canvas(frame,scrollregion=(0,0,1920,1080),xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
canvas.pack(side=LEFT,fill=BOTH,expand=1)

yscrollbar.config(command=canvas.yview)
xscrollbar.config(command=canvas.xview)

second_frame=Frame(canvas)

canvas.create_window((0,5),window=second_frame,anchor="nw")
text=Text(second_frame)


windows.mainloop()

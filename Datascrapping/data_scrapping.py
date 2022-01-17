from tkinter import *
from tkinter import filedialog, ttk
import threading
from pyxlsb import open_workbook
from datetime import date, timedelta

#itilscrum
windows = Tk()
windows.geometry("1300x800")


def scrapping():
    filepath = filedialog.askopenfilename(title="open a file", filetypes=(
        ("xlsb files", "*.xlsb"), ("all files", "*.*")))
    Prospect_list, Week_list, Despatched_list, Assayed_list, ASS_Pending_list, var, var2, var3, var4, str, str1 = Openexcelfile(
        filepath)

    # def update():

    def update(value):
        
        var.set(Prospect_list[value])
        var2.set(Despatched_list[value])
        if value not in Assayed_list:
            Assayed_list[value] = 0
            ASS_Pending_list[value] = Despatched_list[value] - Assayed_list[value]
        var3.set(Assayed_list[value])
        var4.set(ASS_Pending_list[value])
        create_table(prosp=str,weekly=str1,lw=Week_list[str1.get()])
        #windows.update()
    def update2(value):
       # windows.update()
        create_table(prosp=str,weekly=str1,lw=Week_list[str1.get()])
    
    x = threading.Thread(target=create_components, args=(var, var2, var3, var4, Prospect_list, update, str, str1, Week_list, update2))
    x.start()
    #create_components(var, var2, var3, var4, var5, Prospect_list, update, str, str1, Week_list, update2)
    

#!Auxiliary functions

def Openexcelfile(filepath):
    with open_workbook(filepath) as wb:
        Prospect_list = {}
        Week_list = {}
        last_list = []
        Despatched_list = {}
        Assayed_list = {}
        AssaysPen_toweek={}
        
        z = threading.Thread(target=scrapping_setup,
                             args=(wb, Week_list, last_list))
        z.start()
        z.join()
        
        str1 = StringVar(second_frame, value=list(Week_list)[0])
        listweek=list(Week_list)
        #print(listweek)
        scrapping_prospect(wb, Prospect_list, Despatched_list, Assayed_list,listweek,AssaysPen_toweek)
        
        #!getting assays pending
        ASS_Pending_list = { vv: (Despatched_list[vv]-Assayed_list[vv]) for vv in Assayed_list}
        
       # scrapping_setup(wb, Week_list, last_list)
       
        var = StringVar(
            second_frame, value=Prospect_list[list(Prospect_list)[0]])
        var2 = StringVar(
            second_frame, value=Despatched_list[list(Despatched_list)[0]])
        var3 = StringVar(
            second_frame, value=Assayed_list[list(Assayed_list)[0]])
        var4 = StringVar(
            second_frame, value=ASS_Pending_list[list(ASS_Pending_list)[0]])
    

        # Adding akkakro allekran cma
        y = threading.Thread(target=Adding_lefted_prospect, args=(
            Prospect_list, last_list, Despatched_list, Assayed_list, ASS_Pending_list))
        y.start()
        #Adding_lefted_prospect(Prospect_list, last_list, Despatched_list, Assayed_list, ASS_Pending_list)
    
        str = StringVar(second_frame, value=list(Prospect_list)[0])
        
    return Prospect_list, Week_list, Despatched_list, Assayed_list, ASS_Pending_list, var, var2, var3, var4, str, str1


def Adding_lefted_prospect(*args):
#def Adding_lefted_prospect(Prospect_list, last_list, Despatched_list, Assayed_list, ASS_Pending_list):
    '''
    for name in last_list:
        Prospect_list[name] = 0 if name not in list(
            Prospect_list) else Prospect_list[name]
        Despatched_list[name] = 0 if name not in list(
            Despatched_list) else Despatched_list[name]
        Assayed_list[name] = 0 if name not in list(
            Assayed_list) else Assayed_list[name]
        ASS_Pending_list[name] = 0 if name not in list(
            ASS_Pending_list) else ASS_Pending_list[name]
    ''' 
        
    for name in args[1]:
       args[0][name] = 0 if name not in list(
            args[0]) else args[0][name]
       args[2][name] = 0 if name not in list(
           args[2]) else args[2][name]
       args[3][name] = 0 if name not in list(
           args[3]) else args[3][name]
       args[4][name] = 0 if name not in list(
           args[4]) else args[4][name]


def scrapping_setup(wb, Week_list, last_list):
    with wb.get_sheet("Setup") as sheet1:
        liste1 = list(sheet1.rows())

        for col in range(len(liste1[0])):
            r, c, v = liste1[0][col]
            if v == "Prospect_Name":
                liste2 = liste1[1:]
                for item in liste2:
                    #  r, g, v = item[c][2]
                    if item[c][2] is None:
                        continue
                    last_list.append(item[c][2])
            #!getting the week
            if v == "Month":
                liste2 = liste1[1:]
                datefrom =  date(2020, 12, 27)
                dateto = datefrom+timedelta(days=6)
                Week_list[liste2[0][c][2]]={"Date From":str(datefrom),"Date To":str(dateto)}
                for item in liste2[1:]:
                   
                    if item[c][2] is None:
                        continue
                    datefrom = dateto+timedelta(days=1)
                    dateto = datefrom+timedelta(days=6)
                    Week_list[item[c][2]] = {"Date From": str(datefrom),
                                             "Date To": str(dateto)}

              
def scrapping_prospect(*args):
#def scrapping_prospect(wb, Prospect_list, Despatched_list, Assayed_list):
    with args[0].get_sheet("Samples Data") as sheet1:
        liste1 = list(sheet1.rows())
        #!getting the list of prospect and the number of samples
        for col in range(len(liste1[0])):
            r, c, v = liste1[0][col]
            if v == "PROSPECT":
                liste2 = liste1[1:]

                for item in liste2:
                    #*prospect column
                    v = item[c][2]
                    #*sample type column
                    g=item[c+4][2]
                    print(g)
                    #*samples despatched column
                    i = item[c+6][2]
                    #*Ass_week Numero column
                    r=item[c+15][2]
                   
                    #*sample assayed column
                    s = item[c+16][2]
                    #*Desp_week Numero column
                    x=item[c+21][2]
                    
                    if v is None:
                        continue
                    v = v.upper()
                    args[1][v] = args[1].get(v, 0)+1
                    #!getting the number of sample despatched per prospect in the samples data sheet
                    if i is None:
                        continue
                    args[2][v] = args[2].get(v, 0)+1
                        
                    #!getting the number of sample assayed
                    if s == "":
                        continue
                    args[3][v] = args[3].get(v, 0)+1 
                    
                    #!getting the number of assays pending per week 
                 
                    '''
                    AssaysPen_toweek={
                                        Govisou:
                                                 {AUG:{week 01:2, week 02:4},
                                                  DD:{week 01:2, week 02:7},
                                                  RC:{week 01:2, week 02:22}
                                                  },
                                        CMA:
                                                {RC:{week 01:2,week 02:8},
                                                 AUG:{week 01:2,week 02:},
                                                DD:{week 01:2,week 02:}
                                                },          
                                        Antoinette:
                                                    {
                                                        RC:{week 01:2,week 02:4},
                                                        DD:{week 01:2, week 02:1},
                                                        AUG:{week 01:2,week 02:5}
                                                    }
                    ''' 
                                                
                    #scrapping_prospect(wb, Prospect_list, Despatched_list, Assayed_list,listweek,AssaysPen_toweek)
                   # sumx={}
                   #sumr=0
                    #for i,nameweek in enumerate(args[4]) 
                             #if x == "":
                                #continue
                             #elif x< i+1:
                                #sumx[nameweek]=sumx.get(nameweek,0)+1
                                
                             #if r== "":
                                #continue
                             #elif r<i+1:
                               #sumr+=1                 
                        # args[5]={
                            # v:
                            # {g:{args[4][nameweek]:n}
                            # }
                            # }
        '''
        print(Despatched_list)
        print()
        print(Assayed_list)
        print()     
        print(ASS_Pending_list)
            '''


def create_table(**kwargs):
    f=list(kwargs.values())
    #!Create table
    Table = ttk.Treeview(second_frame)
    Table["columns"] = ("DrillType",
                        "WeekID",
                        "Date From",
                        "Date To",
                        "Holes Drilled",
                        "Samp Total",
                        "Depth Total",
                        "Samp Desp",
                        "Assays received",
                        f"Assays pending to {f[1].get()}")

    # *formate our columns
    Table.column("#0", width=0, stretch=NO)
    Table.column("DrillType", anchor=W, width=90, minwidth=25)
    Table.column("WeekID", anchor=W, width=90, minwidth=25)
    Table.column("Date From", anchor=W, width=90, minwidth=25)
    Table.column("Date To", anchor=W, width=90, minwidth=25)
    Table.column("Holes Drilled", anchor=W, width=90, minwidth=25)
    Table.column("Samp Total", anchor=W, width=90, minwidth=25)
    Table.column("Depth Total", anchor=W, width=90, minwidth=25)
    Table.column("Samp Desp", anchor=W, width=90, minwidth=25)
    Table.column("Assays received", anchor=W, width=90, minwidth=25)
    Table.column(f"Assays pending to {f[1].get()}",
                 anchor=W, width=170, minwidth=25)

    # *create heading
    Table.heading("#0", text="", anchor=W)
    Table.heading("DrillType", text="DrillType",
                  anchor=W)

    Table.heading("WeekID", text="WeekID",
                  anchor=W)

    Table.heading("Date From", text="Date From",
                  anchor=W)

    Table.heading("Date To", text="Date To", anchor=W)

    Table.heading("Holes Drilled", text="Holes Drilled",
                  anchor=W)

    Table.heading("Samp Total", text="Samp Total",
                  anchor=W)

    Table.heading("Depth Total", text="Depth Total",
                  anchor=W)

    Table.heading("Samp Desp", text="Samp Desp",
                  anchor=W)

    Table.heading("Assays received", text="Assays received",
                  anchor=W)

    Table.heading(f"Assays pending to {f[1].get()}",
                  text=f"Assays pending to {f[1].get()}", anchor=W)

    # *add data
    Table.insert(parent="", index="end", iid=0, text="", values=(
        "AC", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.insert(parent="", index="end", iid=1, text="", values=(
        "RAB", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.insert(parent="", index="end", iid=2, text="", values=(
        "AUG", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.insert(parent="", index="end", iid=3, text="", values=(
        "RC", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.insert(parent="", index="end", iid=4, text="", values=(
        "DD", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.insert(parent="", index="end", iid=5, text="", values=(
        "GEOCHEM", f[1].get(), f[2]["Date From"], f[2]["Date To"], "1", "1", "1", "1", "1", "1"))
    Table.grid(row=300, columnspan=4000, pady=50)
      

def create_components(var, var2, var3, var4, Prospect_list, update, str, str1, Week_list, update2):
 
    combo = OptionMenu(second_frame, str, *
                       list(Prospect_list), command=update)
  
    combo1 = OptionMenu(second_frame, str1, *list(Week_list), command=update2)
 
    week_label, SamplesAssayNumber_label, sampleAssayed_label, SamplesAssayNumberP_label, sampleAssayedP_label, SamplesDespaNumber_label, sampleDespatched_label, sampleNumber_label, SamplesData_label = create_labels(
        var, var2, var3, var4)

    place_labels(week_label, SamplesAssayNumber_label, sampleAssayed_label, SamplesAssayNumberP_label, sampleAssayedP_label, SamplesDespaNumber_label, sampleDespatched_label, sampleNumber_label, SamplesData_label,combo,combo1)

    create_table(prosp=str,weekly=str1,lw=Week_list[str1.get()])
    

def lab(frame, text):
    return Label(frame, text=text,
                 font=("Arial", 10, "bold"),
                 fg="red",
                 bg="White",
                 bd=5,
                 padx=5,
                 pady=5
                 )
    
def create_labels(var,var2,var3,var4):

    #!samples number
    sampleNumber_label = lab(second_frame,"Samples Number")

    SamplesData_label = Label(second_frame,
                              textvariable=var,
                              font=("Arial", 10, "bold"),
                              fg="white",
                              bg="red",
                              bd=5,
                              padx=5,
                              pady=5
                              )

    #!samples despatched
    sampleDespatched_label = lab(second_frame, "Samples Despatched")

    SamplesDespaNumber_label = Label(second_frame,
                                     textvariable=var2,
                                     font=("Arial", 10, "bold"),
                                     fg="white",
                                     bg="red",
                                     bd=5,
                                     padx=5,
                                     pady=5
                                     )
    #!samples assayed
    sampleAssayed_label = lab(second_frame, "Samples Assayed")

    SamplesAssayNumber_label = Label(second_frame,
                                     textvariable=var3,
                                     font=("Arial", 10, "bold"),
                                     fg="white",
                                     bg="red",
                                     bd=5,
                                     padx=5,
                                     pady=5
                                     )

    #!Assays pending
    sampleAssayedP_label = lab(second_frame, "Assays pending")
    SamplesAssayNumberP_label = Label(second_frame,
                                      textvariable=var4,
                                      font=("Arial", 10, "bold"),
                                      fg="white",
                                      bg="red",
                                      bd=5,
                                      padx=5,
                                      pady=5
                                      )
    #!weeks
    week_label = lab(second_frame, "Weekly Stats")
    return week_label,SamplesAssayNumber_label,sampleAssayed_label,SamplesAssayNumberP_label,sampleAssayedP_label,SamplesDespaNumber_label,sampleDespatched_label,sampleNumber_label,SamplesData_label


def place_labels(week_label, SamplesAssayNumber_label, sampleAssayed_label, SamplesAssayNumberP_label, sampleAssayedP_label, SamplesDespaNumber_label, sampleDespatched_label, sampleNumber_label, SamplesData_label, combo, combo1):
    week_label.grid(row=0, column=50)
    combo.grid(row=200, column=0)
    combo1.grid(row=200, column=100)

    sampleNumber_label.grid(row=0, column=1000, pady=50, padx=10)
    SamplesData_label.grid(row=200, column=1000)

    sampleDespatched_label.grid(row=0, column=1900, pady=50, padx=10)
    SamplesDespaNumber_label.grid(row=200, column=1900)

    sampleAssayed_label.grid(row=0, column=3500, pady=50, padx=10)
    SamplesAssayNumber_label.grid(row=200, column=3500)

    sampleAssayedP_label.grid(row=0, column=3900, pady=50, padx=10)
    SamplesAssayNumberP_label.grid(row=200, column=3900)
    
#!MAIN PROGRAM
# *main frame
frame = Frame(windows)

label = Label(frame,
              text="Data Scrapping",
              font=("Arial", 40, "bold"),
              fg="green",  
              bg="White",  
              bd=10,  
              padx=20,  
              pady=20,  
              )

frame.pack(fill=BOTH, expand=1)
label.pack()
button = Button(frame, text="open a file for scrapping", command=scrapping)
button.pack()

#!scrollbar
# canvas=Canvas(frame)
# canvas.pack(side=LEFT,fill=BOTH,expand=1)

#yscrollbar = Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
yscrollbar = Scrollbar(frame, orient=VERTICAL)
yscrollbar.pack(side=RIGHT, fill=Y)

#xscrollbar = Scrollbar(frame, orient=HORIZONTAL,command=canvas.xview)
xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

# canvas.configure(yscrollcommand=yscrollbar.set)
# canvas.configure(xscrollcommand=xscrollbar.set)
#canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas = Canvas(frame, scrollregion=(0, 0, 3920, 3080),
                xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

yscrollbar.config(command=canvas.yview)
xscrollbar.config(command=canvas.xview)

second_frame = Frame(canvas)

canvas.create_window((0, 5), window=second_frame, anchor="nw")

#IF((COUNTIFS('Samples Data'!X: X, "<=" & (DashBoard!N$1), 'Samples Data'!C: C, DashBoard!G$1, 'Samples Data'!G: G, DashBoard!B9)-COUNTIFS('Samples Data'!R: R, "<=" & (DashBoard!N$1), 'Samples Data'!C: C, DashBoard!G$1, 'Samples Data'!G: G, DashBoard!B9)) <= 0, "", COUNTIFS('Samples Data'!X: X, "<=" & (DashBoard!N$1), 'Samples Data'!C: C, DashBoard!G$1, 'Samples Data'!G: G, DashBoard!B9)-COUNTIFS('Samples Data'!R: R, "<=" & (DashBoard!N$1), 'Samples Data'!C: C, DashBoard!G$1, 'Samples Data'!G: G, DashBoard!B9))

windows.mainloop()

import threading
from collections import Counter
from datetime import date, timedelta
from tkinter import *
from tkinter import filedialog, ttk

from pyxlsb import open_workbook

windows = Tk()
windows.geometry("1300x800")


def scrapping():
    filepath = filedialog.askopenfilename(
        title="open a file", filetypes=(("xlsb files", "*.xlsb"), ("all files", "*.*"))
    )
    (
        Prospect_list,
        Week_list,
        Despatched_list,
        Assayed_list,
        ASS_Pending_list,
        var,
        var2,
        var3,
        var4,
        str2,
        str1,
        AssaysPen_toweek,
    ) = Openexcelfile(filepath)
    # listweek = list(Week_list)
    # def update():
    # listAPW=[]
    # traitement(filepath, listweek, str1,str2,listAPW)

    def update(value):

        var.set(Prospect_list[value])
        var2.set(Despatched_list[value])
        if value not in Assayed_list:
            Assayed_list[value] = 0
            ASS_Pending_list[value] = Despatched_list[value] - Assayed_list[value]
        var3.set(Assayed_list[value])
        var4.set(ASS_Pending_list[value])
        create_table(
            prosp=str2,
            weekly=str1,
            lw=Week_list[str1.get()],
            AssayedPW_list=AssaysPen_toweek,
        )

    def update2(value):

        # traitement(filepath, listweek, str1,str2,listAPW)
        # create_table(prosp=str2, weekly=str1,
        #             lw=Week_list[str1.get()], AssayedPW_list=AssaysPen_toweek)

        # with open_workbook(filepath) as wb:
        # print(AssPW_process(wb, "DD", "CMA UG DDIP",listweek.index(str1.get())+1 ))
        create_table(
            prosp=str2,
            weekly=str1,
            lw=Week_list[str1.get()],
            AssayedPW_list=AssaysPen_toweek,
        )

    x = threading.Thread(
        target=create_components,
        args=(
            var,
            var2,
            var3,
            var4,
            Prospect_list,
            update,
            str2,
            str1,
            Week_list,
            update2,
            AssaysPen_toweek,
        ),
    )
    x.start()


#!Auxiliary functions
def Openexcelfile(filepath):
    with open_workbook(filepath) as wb:
        Prospect_list = {}
        Week_list = {}
        last_list = []
        Despatched_list = {}
        Assayed_list = {}
        AssaysPen_toweek = {}

        z = threading.Thread(target=scrapping_setup, args=(wb, Week_list, last_list))
        z.start()
        z.join()

        str1 = StringVar(second_frame, value=list(Week_list)[0])
        # print(Week_list)
        # print()
        listweek = list(Week_list)
        # print(listweek)
        scrapping_prospect(
            wb, Prospect_list, Despatched_list, Assayed_list, listweek, AssaysPen_toweek
        )
        AssaysPen_toweek = dict(sorted(AssaysPen_toweek.items()))
        # print(AssaysPen_toweek[("GOVISOU", "RC", "Week 06")])
        #!getting assays pending
        ASS_Pending_list = {
            vv: (Despatched_list[vv] - Assayed_list[vv]) for vv in Assayed_list
        }

        var = StringVar(second_frame, value=Prospect_list[list(Prospect_list)[0]])
        var2 = StringVar(second_frame, value=Despatched_list[list(Despatched_list)[0]])
        var3 = StringVar(second_frame, value=Assayed_list[list(Assayed_list)[0]])
        var4 = StringVar(
            second_frame, value=ASS_Pending_list[list(ASS_Pending_list)[0]]
        )

        # Adding akkakro allekran cma
        y = threading.Thread(
            target=Adding_lefted_prospect,
            args=(
                Prospect_list,
                last_list,
                Despatched_list,
                Assayed_list,
                ASS_Pending_list,
            ),
        )
        y.start()
        
        str2 = StringVar(second_frame, value=list(Prospect_list)[0])

    return (
        Prospect_list,
        Week_list,
        Despatched_list,
        Assayed_list,
        ASS_Pending_list,
        var,
        var2,
        var3,
        var4,
        str2,
        str1,
        AssaysPen_toweek,
    )


def Adding_lefted_prospect(*args):
    # def Adding_lefted_prospect(Prospect_list, last_list, Despatched_list, Assayed_list, ASS_Pending_list):
    for name in args[1]:
        args[0][name] = 0 if name not in list(args[0]) else args[0][name]
        args[2][name] = 0 if name not in list(args[2]) else args[2][name]
        args[3][name] = 0 if name not in list(args[3]) else args[3][name]
        args[4][name] = 0 if name not in list(args[4]) else args[4][name]


def scrapping_setup(wb, Week_list, last_list):
    liste2, c = find_column(wb, "Prospect_Name", "Setup")
    for item in liste2:
        #  r, g, v = item[c][2]
        if item[c][2] is None:
            continue
        last_list.append(item[c][2])
        #!getting the week
    liste2, c = find_column(wb, "Month", "Setup")
    datefrom = date(2020, 12, 27)
    dateto = datefrom + timedelta(days=6)
    Week_list[liste2[0][c][2]] = {"Date From": str(datefrom), "Date To": str(dateto)}
    for item in liste2[1:]:
        if item[c][2] is None:
            continue
        datefrom = dateto + timedelta(days=1)
        dateto = datefrom + timedelta(days=6)
        Week_list[item[c][2]] = {"Date From": str(datefrom), "Date To": str(dateto)}

            
                    
def find_column(wb,name_column,sheet):
    with wb.get_sheet(sheet) as sheet1:
        liste1 = list(sheet1.rows())
        #!look for all columns for the first row
    for col in range(len(liste1[0])):
        r, c, v = liste1[0][col]
        if v == name_column:
            return liste1[1:], c


"""
def AssPW_process(wb,name_prospect,name_sample,name_week):
    q=0
    qq=0
    #!liste of prospect
    listeP, c = find_column(wb, "PROSPECT", "Samples Data")
    #!liste of sample type
    #listeS, g = find_column(wb, "SAMPLE_TYPE", "Samples Data")
    g=c+4
    #!liste of ass_weekNO
 #   listeA,r= find_column(wb, "ASS_WeekNO", "Samples Data")
    r=c+15
    #!liste of desp_weekNO
  #  listeD, x = find_column(wb, "DESP_WeekNO", "Samples Data")
    x=c+21
    for item in listeP:
        if isinstance(item[x][2], float) and item[g][2] is not None:
            d=(item[c][2],item[g][2],item[x][2])
            if (
                d[0] == name_prospect
                and d[1] == name_sample
                and d[2] <= name_week
            ):
                q+=1
    
        if isinstance(item[r][2], float) and item[g][2] is not None:
            d=(item[c][2],item[g][2],item[r][2])
            if (
                d[0] == name_prospect
                and d[1] == name_sample
                and d[2] <= name_week
            ):
                qq+=1
    return q-qq
"""

"""
def traitement(filepath,listweek,str1,str2,listAPW):
     with open_workbook(filepath) as wb:
            #["AC","RAB","AUG","RC","DD","GEOCHEM"]
           APW_AC = AssPW_process(wb, "AC", str2.get(),
                                  listweek.index(str1.get())+1)
           APW_RAB = AssPW_process(
               wb, "RAB", str2.get(), listweek.index(str1.get())+1)
           APW_AUG = AssPW_process(
               wb, "AUG", str2.get(), listweek.index(str1.get())+1)
           APW_RC = AssPW_process(wb, "RC", str2.get(),
                                  listweek.index(str1.get())+1)
           APW_DD = AssPW_process(wb, "DD", str2.get(),
                                  listweek.index(str1.get())+1)
           APW_GEOCHEM = AssPW_process(
               wb, "GEOCHEM", str2.get(), listweek.index(str1.get())+1)
     listAPW.append(APW_AC)
     listAPW.append(APW_RAB)
     listAPW.append(APW_AUG)
     listAPW.append(APW_RC)
     listAPW.append(APW_DD)
     listAPW.append(APW_GEOCHEM)
"""

def process(liste2,c,args1,Desp_weekNO,Ass_weekNo,args2,args3):
    #!getting the list of prospect and the number of samples
    for item in liste2:
        # *prospect column
        v = item[c][2]
        # *sample type column
        g = item[c + 4][2]

        # *samples despatched column
        i = item[c + 6][2]
        # *Ass_week Numero column
        r = item[c + 15][2]

        # *sample assayed column
        s = item[c + 16][2]
        # *Desp_week Numero column
        x = item[c + 21][2]

        if v is None:
            continue
        v = v.upper()
        args1[v] = args1.get(v, 0) + 1

        #!getting the number of assays pending per week
        if isinstance(x, float) and g is not None:
            Desp_weekNO.append((v, g, x))
        if isinstance(r, float) and g is not None:
            Ass_weekNo.append((v, g, r))
            #!getting the number of sample despatched per prospect in the samples data sheet
        if i is None:
            continue
        args2[v] = args2.get(v, 0) + 1

        #!getting the number of sample assayed
        if s == "":
            continue
        args3[v] = args3.get(v, 0) + 1


def scrapping_prospect(*args):
    Desp_week = {}
    Ass_week = {}
    Desp_weekNO = []
    Ass_weekNo = []

    liste2, c = find_column(args[0], "PROSPECT", "Samples Data")
    #!getting the list of prospect and the number of samples
    process(liste2, c, args[1], Desp_weekNO, Ass_weekNo, args[2], args[3])
    #!count of each week

    Desp_weekNO = dict(Counter(Desp_weekNO))
    Ass_weekNo = dict(Counter(Ass_weekNo))

    #!Cumul of each week

    cumulweek(Desp_weekNO, Desp_week)
    cumulweek(Ass_weekNo, Ass_week)

    Desp_week = dict(sorted(Desp_week.items()))
    Ass_week = dict(sorted(Ass_week.items()))

    # print(Desp_week)

    # print(Ass_week)
    # print(find_max(Desp_week, "GOVISOU", "RC", 6))

    # print(find_max(Ass_week, "GOVISOU", "RC", 6))

    #!finding the max of each week
    maxweek(args[4], Desp_week, Ass_week, args[5])

    # print(args[5][("GOVISOU","DD","Week 47")])
    #  print(dict(sorted(args[5].items())))


def maxweek(args4, dico, dico2, args5):
    for i, nameweek in enumerate(args4):
        for name in dico:
            a = find_max(dico, name[0], name[1], i + 1)
            b = find_max(dico2, name[0], name[1], i + 1)
            #  print(b)
            args5[(name[0], name[1], nameweek)] = 0 if b is None else a - b


def cumulweek(dico, dico2):
    for name in dico:
        for dd in dico:
            if name[0] == dd[0] and name[1] == dd[1] and dd[2] <= name[2]:
                dico2[(name[0], name[1], int(name[2]))] = (
                    dico2.get((name[0], name[1], int(name[2])), 0)
                    + dico[(dd[0], dd[1], dd[2])]
                )


def find_max(dico, prospect, sample_type, weeknum):
    dd = dico.copy()
    for name in dico:

        if name[0] == prospect and name[1] == sample_type:
            if name[2] <= weeknum:
                d = [
                    (x, y, z)
                    for x, y, z in dico
                    if x == prospect and y == sample_type and z <= weeknum
                ]
                return dico[max(d)]
            else:
                dd[(prospect, sample_type, weeknum)] = 0
                return dd[(prospect, sample_type, weeknum)]


def create_table(**kwargs):
    f = list(kwargs.values())
    #!Create table
    Table = ttk.Treeview(second_frame)
    Table["columns"] = (
        "DrillType",
        "WeekID",
        "Date From",
        "Date To",
        "Holes Drilled",
        "Samp Total",
        "Depth Total",
        "Samp Desp",
        "Assays received",
        f"Assays pending to {f[1].get()}",
    )

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
    Table.column(f"Assays pending to {f[1].get()}", anchor=W, width=170, minwidth=25)

    # *create heading
    Table.heading("#0", text="", anchor=W)
    Table.heading("DrillType", text="DrillType", anchor=W)

    Table.heading("WeekID", text="WeekID", anchor=W)

    Table.heading("Date From", text="Date From", anchor=W)

    Table.heading("Date To", text="Date To", anchor=W)

    Table.heading("Holes Drilled", text="Holes Drilled", anchor=W)

    Table.heading("Samp Total", text="Samp Total", anchor=W)

    Table.heading("Depth Total", text="Depth Total", anchor=W)

    Table.heading("Samp Desp", text="Samp Desp", anchor=W)

    Table.heading("Assays received", text="Assays received", anchor=W)

    Table.heading(
        f"Assays pending to {f[1].get()}",
        text=f"Assays pending to {f[1].get()}",
        anchor=W,
    )

    # *add data
    s = ["AC", "RAB", "AUG", "RC", "DD", "GEOCHEM"]
    for i, name in enumerate(s):
        w = (f[0].get(), name, f[1].get())
        Table.insert(
            parent="",
            index="end",
            iid=i,
            text="",
            values=(
                name,
                f[1].get(),
                f[2]["Date From"],
                f[2]["Date To"],
                "1",
                "1",
                "1",
                "1",
                "1",
                f[3][w] if w in f[3] else "0",
            ),
        )

    Table.grid(row=300, columnspan=4000, pady=50)


def create_components(
    var,
    var2,
    var3,
    var4,
    Prospect_list,
    update,
    str2,
    str1,
    Week_list,
    update2,
    AssaysPen_toweek,
):

    combo = OptionMenu(second_frame, str2, *list(Prospect_list), command=update)

    combo1 = OptionMenu(second_frame, str1, *list(Week_list), command=update2)

    (
        week_label,
        SamplesAssayNumber_label,
        sampleAssayed_label,
        SamplesAssayNumberP_label,
        sampleAssayedP_label,
        SamplesDespaNumber_label,
        sampleDespatched_label,
        sampleNumber_label,
        SamplesData_label,
    ) = create_labels(var, var2, var3, var4)

    place_labels(
        week_label,
        SamplesAssayNumber_label,
        sampleAssayed_label,
        SamplesAssayNumberP_label,
        sampleAssayedP_label,
        SamplesDespaNumber_label,
        sampleDespatched_label,
        sampleNumber_label,
        SamplesData_label,
        combo,
        combo1,
    )

    create_table(
        prosp=str2,
        weekly=str1,
        lw=Week_list[str1.get()],
        AssayedPW_list=AssaysPen_toweek,
    )


def lab(frame, text):
    return Label(
        frame,
        text=text,
        font=("Arial", 10, "bold"),
        fg="red",
        bg="White",
        bd=5,
        padx=5,
        pady=5,
    )


def create_labels(var, var2, var3, var4):

    #!samples number
    sampleNumber_label = lab(second_frame, "Samples Number")
    SamplesData_label = Label(
        second_frame,
        textvariable=var,
        font=("Arial", 10, "bold"),
        fg="white",
        bg="red",
        bd=5,
        padx=5,
        pady=5,
    )
    #!samples despatched
    sampleDespatched_label = lab(second_frame, "Samples Despatched")
    SamplesDespaNumber_label = Label(
        second_frame,
        textvariable=var2,
        font=("Arial", 10, "bold"),
        fg="white",
        bg="red",
        bd=5,
        padx=5,
        pady=5,
    )
    #!samples assayed
    sampleAssayed_label = lab(second_frame, "Samples Assayed")
    SamplesAssayNumber_label = Label(
        second_frame,
        textvariable=var3,
        font=("Arial", 10, "bold"),
        fg="white",
        bg="red",
        bd=5,
        padx=5,
        pady=5,
    )

    #!Assays pending
    sampleAssayedP_label = lab(second_frame, "Assays pending")
    SamplesAssayNumberP_label = Label(
        second_frame,
        textvariable=var4,
        font=("Arial", 10, "bold"),
        fg="white",
        bg="red",
        bd=5,
        padx=5,
        pady=5,
    )
    #!weeks
    week_label = lab(second_frame, "Weekly Stats")

    return (
        week_label,
        SamplesAssayNumber_label,
        sampleAssayed_label,
        SamplesAssayNumberP_label,
        sampleAssayedP_label,
        SamplesDespaNumber_label,
        sampleDespatched_label,
        sampleNumber_label,
        SamplesData_label,
    )


def place_labels(
    week_label,
    SamplesAssayNumber_label,
    sampleAssayed_label,
    SamplesAssayNumberP_label,
    sampleAssayedP_label,
    SamplesDespaNumber_label,
    sampleDespatched_label,
    sampleNumber_label,
    SamplesData_label,
    combo,
    combo1,
):
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

label = Label(
    frame,
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

# yscrollbar = Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
yscrollbar = Scrollbar(frame, orient=VERTICAL)
yscrollbar.pack(side=RIGHT, fill=Y)

# xscrollbar = Scrollbar(frame, orient=HORIZONTAL,command=canvas.xview)
xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

# canvas.configure(yscrollcommand=yscrollbar.set)
# canvas.configure(xscrollcommand=xscrollbar.set)
# canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas = Canvas(
    frame,
    scrollregion=(0, 0, 3920, 3080),
    xscrollcommand=xscrollbar.set,
    yscrollcommand=yscrollbar.set,
)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

yscrollbar.config(command=canvas.yview)
xscrollbar.config(command=canvas.xview)

second_frame = Frame(canvas)

canvas.create_window((0, 5), window=second_frame, anchor="nw")

windows.mainloop()

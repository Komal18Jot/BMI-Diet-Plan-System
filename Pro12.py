# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:54:55 2022

@author: Komal Jot
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:12:38 2022

@author: Komal Jot
"""


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root= Tk()
root.title("Get a Life full Of Warmth! ")
root.geometry("1270x1000")

main_frame= Frame(root)
main_frame.pack( fill=BOTH, expand=1)
mycan= Canvas(main_frame)
mycan.pack(side=LEFT, fill=BOTH, expand=1)


my_Sc= ttk.Scrollbar(main_frame, orient= VERTICAL, command=mycan.yview)
my_Sc.pack(side=RIGHT, fill=Y)
mycan.configure(yscrollcommand=my_Sc.set)
mycan.bind("<Configure>", lambda e: mycan.configure(scrollregion= mycan.bbox("all")) )
sec_frame= Frame(mycan)
mycan.create_window((0,0), window=sec_frame, anchor="nw")

ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\Cha.jpg")
ph_no = ph_n.resize((1250,800))
ph_non = ImageTk.PhotoImage(ph_no)
ph_non_L= Label(sec_frame, image = ph_non, compound = RIGHT)
ph_non_L.photo=ph_non
ph_non_L.place(x=0, y=0)


import pymysql as pm
conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
print(conobj)
mycur=conobj.cursor()

mycur.execute('CREATE DATABASE IF NOT EXISTS prac1')
mycur.execute('CREATE TABLE IF NOT EXISTS GLOW_D(C_ID int(5) Primary Key, C_NAME varchar(30), Height int(3), Weight int(3), BMI int(2), Category varchar(20), Food_P varchar(20), C_WL varchar(20))')
#sec_frame.configure(background='#FFFFE0')


def submit():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()
    mycur.execute('use prac1')
    i=C_ID.get()
    n=C_NAME.get()
    h=Height.get()
    w=Weight.get()
    f=Food_P.get()
    l=C_WL.get()
    wi=int(w)
    hi=int(h)
    bmi=(wi/((hi/100)**2))
    #bmi=str(bmi)
    cat=""
    if bmi>25:
        cat= "Over Weight"
    elif bmi<18.5:
        cat= "Under Weight"
    else:
        cat= "Good Health"
        
    mycur.execute("Insert into GLOW_D values (%s,%s,%s,%s,%s,%s,%s,%s)", (i,n,h,w, bmi, cat, f,l))
    
    
    conobj.commit()
    conobj.close()
    
    messagebox.showinfo("GLOW! ","Your data has been successfully added to database... You may check your BMI now! ") 
    #clear text box
    C_ID.delete(0,END)
    C_NAME.delete(0,END)
    Height.delete(0,END)
    Weight.delete(0,END)


def query():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()
    mycur.execute('select * from GLOW_D')
    rec=mycur.fetchall()
    print(rec)
    pri_rec=""
    for rec in rec:
        pri_rec+=str(rec)+"\n"   
    qu_lab= Label(sec_frame, text= pri_rec)
    qu_lab.grid(row= 31,column=0, columnspan=2 )
    conobj.commit()
    conobj.close()
    
def shw():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()
    mycur.execute('select * from GLOW_D where C_ID= '+ Shw_Box.get())
    rec=mycur.fetchall()
    lst=list(rec)
    pri_rec=""
    for re in rec:
        pri_rec+=str(re)+"\n"  
    qu_lab= Label(sec_frame, text= pri_rec)
    qu_lab.grid(row=11,column=0, columnspan=2 )
    
    mycur.execute('select BMI, Category from GLOW_D where C_ID= '+ Shw_Box.get())
    rec1=mycur.fetchall()
    pri_rec1="Your BMI is: "
    for r in rec1:
        pri_rec1+=str(r)+"\n"
    
    qu_lab1= Label(sec_frame, text= pri_rec1)
    qu_lab1.grid(row=12,column=0, columnspan=2 )
    
    

    conobj.commit()
    conobj.close()

def delete():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()
    mycur.execute('Delete from GLOW_D where C_ID= '+ Del_Box.get() )

    conobj.commit()
    conobj.close()


def food():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()

    f= Fo_P.get()
    if f == "Non-Veg":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\nonn.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=150)
    elif f == "Veg":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\vegg.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=150)
    elif f == "Vegan":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\vega.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=150)    
    else:
      pass
        
    conobj.commit()
    conobj.close()  

def exe():
    conobj=pm.connect(host= "localhost", user='root', passwd='root@1234', database='prac1')
    print(conobj)
    mycur=conobj.cursor()
    y= Cwl.get()
    if y == "Active":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\snaman.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=360)       
       oo= Label(sec_frame, text= "Surya Namaskar (Sun Salutation)!!").grid(row=24,column=1)
       ooo= Label(sec_frame, text= "Do this practice 6 times a day. ").grid(row=25,column=1)
                 
    elif y == "Sedentary":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\snaman.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=360)  
       oo= Label(sec_frame, text= "Surya Namaskar (Sun Salutation)!! ").grid(row=24,column=1)
       ooo= Label(sec_frame, text= "Do this practice 6 times a day (gradually increase it to 12)  ").grid(row=25,column=1)
       
    elif y == "Laborious":
       ph_n=Image.open(r"C:\Users\Arushi Srivastava\OneDrive\Pictures\pro12pics\snaman.jpg")
       ph_no = ph_n.resize((600,200))
       ph_non = ImageTk.PhotoImage(ph_no)
       ph_non_L= Label(root, image = ph_non, compound = RIGHT)
       ph_non_L.photo=ph_non
       ph_non_L.place(x=620, y=360)  
       oo= Label(sec_frame, text= "Surya Namaskar (Sun Salutation)!! ").grid(row=24,column=1)
       ooo= Label(sec_frame, text= "Do this practice 2 times a day. ").grid(row=5,column=1)
       
    else:
         pass

    conobj.commit()
    conobj.close()  
    

C_ID= Entry(sec_frame, width=30)
C_NAME= Entry(sec_frame, width=30)
Height= Entry(sec_frame, width=30)
Weight= Entry(sec_frame, width=30)
Shw_Box= Entry(sec_frame, width=30)
Del_Box= Entry(sec_frame, width=30)

C_ID.grid(row=2, column=1, padx=20)
C_NAME.grid(row=3, column=1)
Height.grid(row=4, column=1)
Weight.grid(row=5, column=1)
Shw_Box.grid(row=15, column=1)
Del_Box.grid(row=17, column=1)

Head= Label(sec_frame, text="GLOW", font=("@MingLiU-ExtB", 50, "italic"), borderwidth=5, relief="ridge", fg="#990000", bg="#ffdab3").grid(row=0, column=0, columnspan=5, rowspan=2, padx=10, pady=10, ipadx=538, ipady=20)
Hea2= Label(sec_frame, text="        Get a Life full Of Warmth !       ", font=("@MingLiU-ExtB", 15), borderwidth=3, relief="ridge", fg="#990000", bg="#ffdab3").place(x=400, y=105) #padx=5, pady=5, ipadx=200, ipady=0.2)
C_ID_L= Label(sec_frame, text="Enter Customer ID: ", bg='#FFFFE0')
C_NAME_L= Label(sec_frame, text="     Enter Name:      ", bg='#FFFFE0')
Height_L= Label(sec_frame, text="Enter Height (cm): ", bg='#FFFFE0')
Weight_L= Label(sec_frame, text="Enter Weight (kg): ", bg='#FFFFE0')
Food_P_L= Label(sec_frame, text="  Food Preference: ", bg='#FFFFE0')
C_WL_L= Label(sec_frame, text="   Work/Lifestyle:   ", bg='#FFFFE0')
Shw_L= Label(sec_frame, text="Show data for ID: ", bg='#FFFFE0').grid(row=15, column=0)
Del_L= Label(sec_frame, text="Delete record for ID: ", bg='#FFFFE0').grid(row=17, column=0)

C_ID_L.grid(row=2, column=0)
C_NAME_L.grid(row=3, column=0)
Height_L.grid(row=4, column=0)
Weight_L.grid(row=5, column=0)
Food_P_L.grid(row=6, column=0)
C_WL_L.grid(row=7, column=0)

Food_P = StringVar(sec_frame) 
fchoice = ["Options",'Vegan', 'Veg','Non-Veg'] 
Food_P.set(fchoice[0]) 
fu = OptionMenu(sec_frame, Food_P, *fchoice).grid(row=6, column=1)

C_WL = StringVar(sec_frame) 
wlchoice = ["Options",'Active', 'Sedentary','Laborious'] 
C_WL.set(wlchoice[0]) 
wl = OptionMenu(sec_frame, C_WL, *wlchoice).grid(row=7, column=1)

Fo_P = StringVar(sec_frame) 
fcho = ["Diet Chart",'Vegan', 'Veg','Non-Veg'] 
Fo_P.set(fcho[0]) 
fc = OptionMenu(sec_frame, Fo_P, *fcho).grid(row=22,column=0)
Cwl = StringVar(sec_frame) 
wlcho = ["Exercise Chart",'Active', 'Sedentary','Laborious'] 
Cwl.set(wlcho[0]) 
wlc = OptionMenu(sec_frame, Cwl, *wlcho).grid(row=22,column=1)



Sub_But= Button(sec_frame, text="Add this to Database", command=submit, bg="#FFDAB9")
Sub_But.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


Shw_But= Button(sec_frame, text="Show Data ", command=shw, bg="#FFDAB9")
Shw_But.grid(row=16, column=0, columnspan=2, padx=10, pady=10, ipadx=70)

Del_But= Button(sec_frame, text="Delete Record ", command=delete, bg="#FFDAB9")
Del_But.grid(row=18, column=0, columnspan=2, padx=10, pady=10, ipadx=60)

Q_But= Button(sec_frame, text="Show Database", command=query, bg="#FFDAB9")
Q_But.grid(row=30, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

F_But= Button(sec_frame, text="Diet Chart!!", command=food, bg="#FFDAB9")
F_But.grid(row=23, column=0, padx=10, pady=10, ipadx=27, ipady=22)

E_But= Button(sec_frame, text="Exercise Chart!!", command=exe, bg="#FFDAB9")
E_But.grid(row=23, column=1, padx=10, pady=10, ipadx=17, ipady=21.5)


conobj.close()
root.mainloop()


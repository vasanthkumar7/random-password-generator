from tkinter import *
from tkinter import messagebox
import re
import random


root=Tk()
root.title("Random password generator")

#global variables
uppercase=1
lowercase=0
number=0
symbol=0



#functions

def generate_password():
    global uppercase,lowercase,number,symbol
    global password
    global password_length
    lowercase_ch="abcdefghijklmnopqrstuvwxyz"
    uppercase_ch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="01234567890"
    symbols="!@#$%^&*()?{}[]+^;.,<>"

    if (lowercase or uppercase or number or symbol)==0:
        messagebox.showinfo("Password generator", "Select atleast one field")

    password_sample=""

    if uppercase:
        password_sample+=uppercase_ch
    if lowercase:
        password_sample+=lowercase_ch
    if number:
        password_sample+=numbers
    if symbol:
        password_sample+=symbols
    p =  "".join(random.sample(password_sample,int(password_length.get() )))
    if(len(p)>=8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',p))==True):
            password.config(fg="green")
        elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',p))==True):
            password.config(fg="red")
    else:
        password.config(fg="red")

    password.delete(0,END)
    password.insert(0,p)
    
    
def change_mode(what,color):
    global uc,lc,num,sym
    global uppercase,lowercase,number,symbol
    if what=="uc":
        if color:
            uc.config(bg="red")
            uppercase=0
        else:
            uc.config(bg="green")
            uppercase=1
    if what=="lc":
        if color:
            lc.config(bg="red")
            lowercase=0
        else:
            lc.config(bg="green")
            lowercase=1
    if what=="num":
        if color:
            num.config(bg="red")
            number=0
        else:
            num.config(bg="green")
            number=1

    if what=="sym":
        if color:
            sym.config(bg="red")
            symbol=0
        else:
            sym.config(bg="green")
            symbol=1

    


top=Frame(root)

uc=Button(top,text="Upper Case",font=("Comic Sans MS", 15, "bold"),bg="green",command=lambda: change_mode("uc",uppercase))
lc=Button(top,text="Lower Case",font=("Comic Sans MS",15, "bold"),bg="red",command=lambda: change_mode("lc",lowercase))
num=Button(top,text="Numbers",font=("Comic Sans MS", 15, "bold"),bg="red",command=lambda: change_mode("num",number))
sym=Button(top,text="Symbols",font=("Comic Sans MS", 15, "bold"),bg="red",command=lambda: change_mode("sym",symbol))

uc.grid(row=0,column=0,padx=5)
lc.grid(row=0,column=1,padx=5)
num.grid(row=0,column=2,padx=5)
sym.grid(row=0,column=3,padx=5)

top.grid(row=0,column=0)


middle=Frame(root)
password_length=Scale(middle, from_=0, to=30,length=350,width=20, orient=HORIZONTAL)
password=Entry(middle,font=("Comic Sans MS", 20, "bold"))
generate=Button(middle,text="Generate",font=("Comic Sans MS", 13, "bold"),bg="green",command=generate_password)


password_length.grid(row=0,column=0,pady=20)
password.grid(row=1,column=0,padx=10)
generate.grid(row=1,column=1)

middle.grid(row=1,column=0,pady=5)




root.mainloop()

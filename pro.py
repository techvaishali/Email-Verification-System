from tkinter import *
from tkinter import messagebox


def second_win():
    window=Tk()
    window.title('WELCOME TO NEW WINDOW')
    Label(window,text='VERIFICATION CODE',font=('arial',20,'italic','bold')).place(relx=0.5,rely=0.3,anchor=CENTER)
root= Tk()
username=StringVar()
password=StringVar()
def login():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("ERROR","ALL FIELS ARE REQUIRED")
    elif username.get()=="ADMIN" and password.get()=="VAISHALI":
        window = Tk()
        window.title("Welcome To New Window")
        window.geometry('1000x500+100+50')
        Label(window, text='EMail VERIFICATION CODE', relief='raised', font=('arial', 12, 'bold')).place(x=30, y=70)
        Entry(window,borderwidth=3,show='.',font=('arial',12,'bold')).pack()
        Button(window,text='SUBMIT',bg="darkblue",fg="white",relief="flat",font=('arial',10,'bold')).pack(ipadx=0,ipady=0,anchor=NW,side=LEFT)
    else:
         messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD")


Label(root,text="EMAIL VERIFICATION SYSTEM",relief ='raised',font=('arial',30,'italic','bold')).place(x=30,y=70)
Label(root,text="ADMIN LOGIN",relief='raised',font=('arial',50,'italic','bold')).place(relx=0.5,rely=0.3,anchor=CENTER)
Label_1= Label(root,text="username",font=('arial',30,'italic')).place(relx=0.32,rely=0.5,anchor=CENTER)
Entry_1= Entry(root,borderwidth=3,font=('Broadway',20)).place(relx=0.52,rely=0.53,anchor=SW,height=55,width=350)
Label_2= Label(root,text="password",font=('arial',30,'italic')).place(relx=0.32,rely=0.62,anchor=CENTER)
Entry_2= Entry(root,borderwidth=3,show='*',font=('Broadway',20)).place(relx=0.52,rely=0.65,anchor=SW,height=55,width=350)
Button(root,text='LOGIN',command=login ,font=('arial',20,'italic','bold')).place(relx=0.26,rely=0.74,anchor=CENTER)
root.mainloop()
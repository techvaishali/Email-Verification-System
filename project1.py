from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter .messagebox as box
def second_win():
    window = Tk()
    window.title("Welcome To New Window")
    Label(window,text='EMail VERIFICATION CODE',relief='raised',font=('arial', 12 ,'bold')).place(x=30,y=70)

root = Tk()
username=StringVar()
Password=StringVar()


def login():
    if username.get()=="" or Password.get()=="":
        messagebox.showerror("ERROR","ALL FIELS ARE REQUIRED")
    elif username.get()=="ADMIN" and Password.get()=="VAISHALI":
        window = Tk()
        window.title("Welcome To New Window")
        Label(window,text="Enter Code",relief='raised',font =('arial',12,'bold')).pack(fill=tk.X)
        Entry(window,borderwidth=3,show='.',font=('arial',12,'bold')).pack()
        Button(window,text='SUBMIT',bg="darkblue",fg="white",relief="flat",font=('arial',10,'bold')).pack(ipadx=0,ipady=0,anchor=NW,side=LEFT)
    else:
         messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD")
Filename = PhotoImage(file=r"C:\\Users\\hp\\Desktop\\joint-project-2161493_1280.png")
background_label = Label(root, image=Filename)
background_label.place(x=0.5, y=0.5, relwidth=1, relheight=1)

Label(root, text='ADMIN LOGIN', relief='flat', font=('Castellar', 50 , 'italic')).place(relx=0.5, rely=0.3,anchor=CENTER)
Label(root, text='EMAIL VERIFICATION SYSTEM ', background='chartreuse1', relief="raised", font=('Castellar',30,'bold','italic')).place(x=125,y=105)

lable_1 = Label(root, text=' username', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.5, anchor=CENTER)
Entry_1 = Entry(root,borderwidth=3,font=('Broadway', 20)).place(relx=0.52, rely=0.53, anchor=SW,height=55,width=350)
lable_2 = Label(root, text='Password', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.62, anchor=CENTER)
Entry_2 = Entry(root,borderwidth=3,show='*',font=('Broadway', 20)).place(relx=0.52, rely=0.65, anchor=SW,height=55,width=350)


Button(root, text="LOGIN",bg="black",fg="white",command=login ,font=('Castellar', 20,'italic','bold')).place(relx=0.26, rely=0.74, anchor=CENTER)
Button(root,text="RESET",bg="black",fg="white",font=('Castellar', 20,'italic','bold')).place(relx=0.5, rely=0.74, anchor=CENTER)
Button(root,text="EXIT",bg="black",fg="white",font=('Castellar', 20,'italic','bold'),command = root.quit).place(relx=0.72, rely=0.74, anchor=CENTER)





width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry('%dx%d+0+0'% (width_value, height_value))
root.mainloop()

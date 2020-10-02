from tkinter import*
import tkinter as tk
import tkinter .messagebox as box
from tkinter import messagebox


def second_win():
    window = Tk()
    window.title('welcome to new window')
    window.geometry('1000x500+100+50')
    Label(window, text='COURIER MANAGEMENT SYSTEM', relief="raised", font=('arial', 12, 'bold')).place(x=30,y=70)
master=Tk()
username=StringVar()
password=StringVar()
master.geometry("400x300")
def login():
    if username.get()=="" or password.get()=="":
       messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    elif username.get()=="ADMIN" and password.get()=="RAHUL":
        window = Tk()
        window.title('welcome to new window')
        window.geometry('1000x500+100+50')
        Label(window, text='ADMIN DASHBOARD', bg="blue", fg="white", relief="raised",font=('arial', 12, 'bold')).pack(fill=tk.X)
        Button(window, text="HOME", bg="darkblue", fg="white", relief="flat", font=('arial', 10, 'bold')).pack(ipadx=0,
                                                                                                               ipady=0,
                                                                                                               anchor=NW,
                                                                                                               side=LEFT)
        Button(window, text="DASHBOARD", bg="darkblue", fg="white", relief="flat", font=('arial', 10, 'bold')).pack(
            ipadx=0, ipady=0, anchor=NW, side=LEFT)
        Button(window, text="HUB", bg="darkblue", fg="white", relief="flat", font=('arial', 10, 'bold')).pack(ipadx=0,
                                                                                                              ipady=0,
                                                                                                              anchor=NW,
                                                                                                              side=LEFT)
        Button(window, text="PICKUP", bg="darkblue", fg="white", relief="flat", font=('arial', 10, 'bold')).pack(
            ipadx=0, ipady=0, anchor=NW, side=LEFT)
        Button(window, text="TRACK SHIPMENT", bg="darkblue", fg="white", relief="flat",
               font=('arial', 10, 'bold')).pack(ipadx=0, ipady=0, anchor=NW, side=LEFT)
        Button(window, text="COMPLAINT", bg="darkblue", fg="white", relief="flat", font=('arial', 10, 'bold')).pack(
            ipadx=0, ipady=0, anchor=NW, side=LEFT)
        Button(window, text="SCHEDULE DELIVERY", bg="darkblue", fg="white", relief="flat",
               font=('arial', 10, 'bold')).pack(ipadx=0, ipady=0, anchor=NW, side=LEFT)
    else:
        messagebox.showerror("ERROR", "INVALID USERNAME AND PASSWORD")

frame1=Frame(master,width=550, height=600, background="white")
frame1.place(relx=0.51, rely=0.5, anchor=CENTER)

Label(frame1, text='ADMIN LOGIN',bg='cyan',relief='flat',font=('Castellar',22,'italic')).place(relx=0.47,rely=0.27,anchor=CENTER)
Label(master, text='COURIER MANAGEMENT SYSTEM',background='white',relief="raised",font=('Castellar',30,'italic')).place(anchor=NW)
Button(frame1, text='LOGIN', bg="black", fg="white", command=login, height=2, width=10, font=('40')).place(
            relx=0.25, rely=0.64, anchor=CENTER)

Button(frame1, text="RESET",bg="black",fg="white",height=2,width=10,font=('40')).place(relx=0.52, rely=0.64, anchor=CENTER)
Button(frame1, text="EXIT",bg="black",fg="white",height=2,width=10,font=('40'),command =master.quit,).place(relx=0.79, rely=0.64, anchor=CENTER)

Label(frame1, text='USER NAME',bg="cyan",fg="black",compound=LEFT,font=('5')).place(relx=0.30, rely=0.4, anchor=CENTER,height=35,width=150)

Label(frame1, text='PASSWORD',bg="cyan",fg="black",compound=LEFT,font=('10')).place(relx=0.30, rely=0.51, anchor=CENTER,height=35,width=150)

Entry(frame1,font=('30'),textvariable=username).place(relx=0.64, rely=0.4, anchor=CENTER,height=30)

Entry(frame1,font=('30'),textvariable=password,show="*").place(relx=0.64, rely=0.51, anchor=CENTER,height=30)

width_value=master.winfo_screenwidth()
height_value=master.winfo_screenheight()
master.geometry('%dx%d+0+0'% (width_value, height_value))
master.mainloop()


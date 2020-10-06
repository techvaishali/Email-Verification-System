# importing modules
from tkinter import *
from tkinter import messagebox

# Functions 
def second_win():
    window = Tk()
    window.title("Welcome To New Window")
    window.geometry('1000x500+100+50')
    Label(window,text='WELCOME TO YOUR ACCOUNT',relief='raised',font=('arial', 12 ,'bold')).place(x=30,y=70)

def login():
    username = Entry_1.get()
    Password = Entry_2.get()
    username=str(username)
    Password=str(Password)
    print(username, Password)
    if username=="" or Password=="":
        messagebox.showerror("ERROR","ALL FIELS ARE REQUIRED")
    elif username=="ADMIN" and Password=="VAISHALI":
        window = Tk()
        window.title("Welcome To New Window")
        window.geometry('1000x500+100+50')
        Label(window, text='WELCOME TO YOUR ACCOUNT', relief='raised', font=('arial', 12, 'bold')).place(x=30, y=70)
        
    else:
         messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD")


# Initializing main window
master = Tk()
master.geometry("400x300")
Filename = PhotoImage(file=r"images\\bg.png")
background_label = Label(master, image=Filename)
background_label.place(x=0.5, y=0.5, relwidth=1, relheight=1)

# creating label & entry boxes
Label(master , text='ADMIN LOGIN', relief='flat', font=('Castellar', 50 , 'italic')).place(relx=0.5, rely=0.3,anchor=CENTER)
Label(master , text='EMAIL VERIFICATION SYSTEM ', background='chartreuse1', relief="raised", font=('Castellar',30,'bold','italic')).place(x=125,y=105)
lable_1 = Label(master , text=' username', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.5, anchor=CENTER)
Entry_1 = Entry(master ,borderwidth=3,font=('Broadway', 20))
Entry_1.place(relx=0.52, rely=0.53, anchor=SW,height=55,width=350)
lable_2 = Label(master , text='Password', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.62, anchor=CENTER)
Entry_2 = Entry(master ,borderwidth=3,show='*',font=('Broadway', 20))
Entry_2.place(relx=0.52, rely=0.65, anchor=SW,height=55,width=350)

# creating button 
Button(master, text="LOGIN",bg="black",fg="white",command=login ,font=('Castellar', 20,'italic','bold')).place(relx=0.26, rely=0.74, anchor=CENTER)
Button(master,text="CREATE NEW ACCOUNT",bg="black",fg="white",font=('Castellar', 20,'italic','bold')).place(relx=0.5, rely=0.74, anchor=CENTER)


width_value=master.winfo_screenwidth()
height_value=master.winfo_screenheight()
master.geometry('%dx%d+0+0'% (width_value, height_value))

# infinite loop
master.mainloop()

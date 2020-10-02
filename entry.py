from tkinter import *
from tkinter import messagebox, PhotoImage
root = Tk()
#master=Tk()
username=StringVar()
password=StringVar()
#master.geometry("400x300")
def login():
    if username.get() == "Admin" or password.get() == "Vaishali":
        print("login Successfully")
        messagebox.showinfo("login successfully")
    else:

        messagebox.showerror("ERROR", "INVALID USERNAME AND PASSWORD")


#Filename = PhotoImage(file=r"C:\\Users\\hp\\Desktop\\joint-project-2161493_1280.png")
#background_label = Label(root, image=Filename)
#background_label.place(x=0.5, y=0.5, relwidth=1, relheight=1)

Label(root, text='ADMIN LOGIN', relief='flat', font=('Castellar', 50 , 'italic')).place(relx=0.5, rely=0.3,anchor=CENTER)
Label(root, text='EMAIL VERIFICATION SYSTEM ', background='chartreuse1', relief="raised", font=('Castellar',30,'bold','italic')).place(x=125,y=105)

usernametext = Label(root, text=' username', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.5, anchor=CENTER)
usernameguess = Entry(root,borderwidth=3,font=('Broadway', 20)).place(relx=0.52, rely=0.53, anchor=SW,height=55,width=350)
passwordtext = Label(root, text='Password', font=('Castellar', 30,'italic')).place(relx=0.32, rely=0.62, anchor=CENTER)
passwordguess = Entry(root,borderwidth=3,show='*',font=('Broadway', 20)).place(relx=0.52, rely=0.65, anchor=SW,height=55,width=350)


Button(root, text="login",command=login,font=('Castellar', 20,'italic','bold')).place(relx=0.67, rely=0.7, anchor=NW)








root.mainloop()



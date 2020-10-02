from tkinter import *
root = Tk()
e= Entry(root,width=50)
e.pack()
def myclick():
      mylabel= Label(root,text=e.get())
      mylabel.pack()
mybutton=Button(root,text='click Me!',command=myclick)
mybutton.pack()

root.mainloop()
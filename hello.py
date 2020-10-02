from tkinter import *
root = Tk()
e= Entry(root,width=50)
e.pack()
e.insert(0,"Enter Your Name")
def myclick():
      hello="hello"+e.get()
      mylabel= Label(root,text=hello)
      mylabel.pack()
mybutton=Button(root,text='click Me!',command=myclick)
mybutton.pack()

root.mainloop()
from tkinter import *

#configure root
root  = Tk()
root.title('Otp')
root.geometry('300x200')

# functions 

# label, entry & buttons
otp_label = Label(root, text='Enter OTP', padx=5, pady=5)
otp_entry = Entry(root)
otp_submit = Button(root, text='submit', padx=15, pady=10)

# call label, entry & button
otp_label.grid(row=0, column=0, padx=5, pady=5)
otp_entry.grid(row=0, column=1, padx=5, pady=5)
otp_submit.grid(row=1, column=1, padx=5)


# infinite loop
root.mainloop()
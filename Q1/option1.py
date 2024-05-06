from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def texts(var1, var2):
    messagebox.showinfo(var1 + var2)
    
    
    

root = Tk()
root.title("Sales Records Management System")

option1 = ttk.Frame(root, padding = 10)
option1.grid(row=8, column=3)

subtitle = ttk.Label(option1, text="Select an option from below to get started").grid(row=0)

space1 = ttk.Label(option1, text="").grid(column=0, row=1)
label1 = ttk.Label(option1, text="Enter Customer Record Filename").grid(column=0, row=2, sticky="w")
var1 = ""
entry1 = ttk.Entry(option1, textvariable=var1).grid(column=1, row=2)

space2 = ttk.Label(option1, text="").grid(column=0, row=3)
label2 = ttk.Label(option1, text="Enter Sales Record Filename").grid(column=0, row=4, sticky="w")
var2 = ""
entry2 = ttk.Entry(option1, textvariable=var2).grid(column=1, row=4)

space3 = ttk.Label(option1, text="").grid(column=0, row=5)
label3 = ttk.Label(option1, text="When you are ready to load, click on submit").grid(column=0, row=6, sticky="w")
button3 = ttk.Button(option1, text="Submit", command=messagebox.showinfo(var1 + var2)).grid(column=1, row=6)

root.mainloop()




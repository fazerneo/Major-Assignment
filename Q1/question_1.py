from tkinter import *
from tkinter import ttk


option1_records = {}

while True
root = Tk()
root.title("Sales Records Management System")
window = ttk.Frame(root, padding = 10)
window.grid(row=8, column=3)

subtitle = ttk.Label(window, text="Select an option from below to get started").grid(row=0)
space1 = ttk.Label(window, text="").grid(column=0, row=1)
label1 = ttk.Label(window, text="1. Load Customer and Sales Records").grid(column=0, row=2, sticky="w")
button1 = ttk.Button(window, text="Select", command=option1).grid(column=1, row=2)
space2 = ttk.Label(window, text="").grid(column=0, row=3)
label2 = ttk.Label(window, text="2. Save Customer Records").grid(column=0, row=4, sticky="w")
button2 = ttk.Button(window, text="Select", command=root.destroy).grid(column=1, row=4)
space3 = ttk.Label(window, text="").grid(column=0, row=5)
label3 = ttk.Label(window, text="3. Save Sales Records").grid(column=0, row=6, sticky="w")
button3 = ttk.Button(window, text="Select", command=root.destroy).grid(column=1, row=6)
space4 = ttk.Label(window, text="").grid(column=0, row=7)
label4 = ttk.Label(window, text="4. Quit Program").grid(column=0, row=8, sticky="w")
Quit = ttk.Button(window, text="Select", command=root.destroy).grid(column=1, row=8)

option1 = ttk.frame(root, padding = 10)
option1.grid(row=8, column=3)

subtitle = ttk.Label(window, text="Select an option from below to get started").grid(row=0)
space1 = ttk.Label(window, text="").grid(column=0, row=1)
label1 = ttk.Label(window, text="1. Load Customer and Sales Records").grid(column=0, row=2, sticky="w")
button1 = ttk.Button(window, text="Select", command=root.destroy).grid(column=1, row=2)
    
root.mainloop()


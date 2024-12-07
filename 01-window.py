from tkinter import *
from tkinter import font
from mainfile import *

import os

# thiết lập tkinter
root = Tk()
root.title("change color")

# label
label = Label(root, text="hello", bg=COLOR__PURPLE, font=15, width=40, padx=10, pady=10)
label.pack(side=BOTTOM, fill=X)
label.pack()

label.place(x=50, y=100)


root.mainloop()

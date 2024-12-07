from tkinter import *
from app import App
from tkinter import font
from mainfile import *

window = Tk()
window.title("change color")
# label

font_title  = font.Font(family="Terminal", size=44, weight=font.BOLD)
font_text  = font.Font(family="Modern", size=20,weight=font.BOLD)

label_python = Label(window, text="python", font=font_title, bg=COLOR__PURPLE, fg=COLOR__RED, width=10, padx=10, pady=10)
label_python.pack(side=TOP, anchor=NE)

label_Tkinter = Label(window, text="Tkinter", font=font_title, bg=COLOR__PURPLE, fg=COLOR__RED, width=10, padx=10, pady=10)
label_Tkinter.pack(side=BOTTOM,  anchor=SE)


# my__button = Button (window, text='hello', cursor='exchange')
# my__button.pack(pady=20)

app = App(window)


window.mainloop()

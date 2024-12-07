from tkinter import *
from app import App
from tkinter import font
from mainfile import *
import random

window = Tk()
window.title("change color")

font_title = font.Font(family="Terminal", size=14, weight=font.BOLD)
font_text = font.Font(family="Modern", size=10, weight=font.BOLD)

def ramdom_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def show_Cour_info(background):
    label['background'] = background

def creact_button(name, background, index):
    Button(window, text=name,bg=background,fg=COLOR__BLACK , padx=30,pady=20,command=lambda:show_Cour_info(background)).grid(row=1, column=index, sticky=W + E, padx=30)

label = Label(window, text='Hello',bg=ramdom_color(), font= font_title, padx=20, pady=20,)
label.grid(row=0, column=0, columnspan=4, sticky="wse",padx=30 )
creact_button('Green', COLOR__GREEN, 0)
creact_button('Blue', COLOR__BLUE, 1)
creact_button('RED', COLOR__RED, 2)
creact_button('YEllow', COLOR__YELLOW, 3)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.minsize(100,200)
app = App(window)
window.mainloop()

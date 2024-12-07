from tkinter import *
from app import App
from mainfile import *
from tkinter import font
import random

window = Tk()
window.title("change color")

def ramdom_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

font__title = font.Font(family="Hind Mysuru", size=26, weight=font.BOLD)

label = Label(window, text="Hello", bg=ramdom_color(), padx=20, pady=20, font=font__title )
label.grid(row=0, column=0, columnspan=4, padx=30, sticky="WSE")

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

def show_Cour_info(background):
      label['background'] = background

def Create__button(name, background, index):
      Button(window, text=name, bg=background,fg=COLOR__BLACK, padx=30,pady=20,command=lambda:show_Cour_info(background)).grid(row=1, column=index, sticky= W + E, padx=30)

Create__button("Green",COLOR__GREEN, '0')
Create__button("Blue",COLOR__BLUE, '1')
Create__button("Red",COLOR__RED, '2')
Create__button("Yellow",COLOR__YELLOW, '3')

app = App(window)
window.mainloop()

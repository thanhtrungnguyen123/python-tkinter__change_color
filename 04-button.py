from tkinter import *
from app import App
from tkinter import font
from mainfile import *

window = Tk()
window.title("change color")
# label

font_title = font.Font(family="Terminal", size=14, weight=font.BOLD)
font_text = font.Font(family="Modern", size=10, weight=font.BOLD)

def show_hello():
    print('xin chào')

def show_Cour_info(name):
    print(' xin chao ' + name)

B = Button(window, text="Hello", bg=COLOR__YELLOW, activebackground= COLOR__GREEN,  fg=COLOR__RED, padx=30,pady=20,command=show_hello)
B.grid(row=0, column=0)

Button_python = Button(window, text="python", bg=COLOR__YELLOW, activebackground= COLOR__GREEN,  fg=COLOR__RED, padx=30,pady=20,command=lambda:show_Cour_info("python"))
Button_python.grid(row=0, column=1)

Button_tkinter = Button(window, text="tkinter", bg=COLOR__YELLOW, activebackground= COLOR__GREEN,  fg=COLOR__RED, padx=30,pady=20,command=lambda:show_Cour_info("tkinter"))
Button_tkinter.grid(row=0, column=2)



window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

app = App(window)
window.mainloop()

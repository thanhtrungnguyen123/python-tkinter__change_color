from tkinter import *
from app import App
from tkinter import font
from mainfile import *

window = Tk()
window.title("change color")
# label

font_title  = font.Font(family="Terminal", size=14, weight=font.BOLD)
font_text  = font.Font(family="Modern", size=10,weight=font.BOLD)

label_python = Label(window, text="python", font=font_title, bg=COLOR__PURPLE, fg=COLOR__RED, width=10, padx=0, pady=0)
label_python.grid(row=0, column=0,)

label_tkiter = Label(window, text="python", font=font_title, bg=COLOR__RED, fg=COLOR__PURPLE, width=10, padx=0, pady=0)
label_tkiter.grid(row=0, column=1,)

label_pygame = Label(window, text="pygmae", font=font_title, bg=COLOR__BLACK, fg=COLOR__BLUE, width=10, padx=0, pady=0)
label_pygame.grid(row=0, column=2,)

label_pygame = Label(window, text="pygmae", font=font_title, bg=COLOR__BLACK, fg=COLOR__BLUE, width=10, padx=0, pady=0)
label_pygame.grid(row=1, column=1,)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)



window.rowconfigure(0, weight=1)
# my__button = Button (window, text='hello', cursor='exchange')
# my__button.pack(pady=20)

app = App(window)


window.mainloop()

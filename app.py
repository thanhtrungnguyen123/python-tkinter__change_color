from mainfile import *
import os
class App:
    def __init__(self, window) -> None:
        pass
        window.geometry("500x500+0+0")
                
        window.iconbitmap(os.path.join(PATH__IMAGES, "icon.ico"))

        window["bg"] = COLOR__BACKGROUND

        # window.resizable(False, False)

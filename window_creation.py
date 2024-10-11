import tkinter as tk

class createBlock:
    def __init__(self):
        self.windowSize = (100,250)
        self.position = [0,0]
        self.size = "200x250"

        self.window = tk.Tk()
        self.window.title("block creation window")
        self.window.geometry(self.size)
        self.window.minsize(200,250)
        self.window.maxsize(200,250)
        self.window.mainloop()
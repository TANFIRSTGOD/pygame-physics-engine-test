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

        x_label = tk.Label(self.window, text="x", font=("Arial", 12))
        y_label = tk.Label(self.window, text="y", font=("Arial", 12))
        width_label = tk.Label(self.window, text="width", font=("Arial", 12))
        height_label = tk.Label(self.window, text="height", font=("Arial", 12))
        mass_label = tk.Label(self.window, text="mass", font=("Arial", 12))
        volume = tk.Label(self.window, text="volume", font=("Arial", 12))
        color = tk.Label(self.window, text="color", font=("Arial", 12))

        x_label.pack()
        y_label.pack()
        width_label.pack()
        height_label.pack()
        mass_label.pack()
        volume.pack()
        color.pack()

        self.window.mainloop()
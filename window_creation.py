import tkinter as tk

class createBlock:
    def __init__(self):
        self.windowSize = (100,250)
        self.position = [0,0]
        self.size = "200x350"

        self.window = tk.Tk()
        self.window.title("block creation window")
        self.window.geometry(self.size)
        self.window.minsize(200,350)
        self.window.maxsize(200,350)

        selected_option = tk.StringVar()

        x_label = tk.Label(self.window, text="x", font=("Arial", 12))
        self.x_box = tk.Entry(self.window)

        y_label = tk.Label(self.window, text="y", font=("Arial", 12))
        self.y_box = tk.Entry(self.window)

        width_label = tk.Label(self.window, text="width", font=("Arial", 12))
        self.width_box = tk.Entry(self.window)

        height_label = tk.Label(self.window, text="height", font=("Arial", 12))
        self.height_box = tk.Entry(self.window)
        
        mass_label = tk.Label(self.window, text="mass", font=("Arial", 12))
        self.mass_box = tk.Entry(self.window)

        volume = tk.Label(self.window, text="volume", font=("Arial", 12))
        self.volume_box = tk.Entry(self.window)

        color = tk.Label(self.window, text="color", font=("Arial", 12))
        self.color_drop_down = tk.OptionMenu(self.window, selected_option, "red", "green", "blue", "yellow", "purple", "white")

        self.confirm_button = tk.Button(self.window, text="confirm")

        x_label.pack()
        self.x_box.pack()

        y_label.pack()
        self.y_box.pack()

        width_label.pack()
        self.width_box.pack()

        height_label.pack()
        self.height_box.pack()

        mass_label.pack()
        self.mass_box.pack()

        volume.pack()
        self.volume_box.pack()

        color.pack()
        self.color_drop_down.pack()

        self.confirm_button.pack()

        self.window.mainloop()

    def return_x(self):
        return int(self.x_box.get())
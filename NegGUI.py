import tkinter as tk
import NegPix


class gui:
    appname = "Negarin Pixel"
    current_doc = NegPix
    current_images = NegPix
    image_frame = tk
    tools_frame = tk
    window = tk
    file_menu = []
    canvas_panel = tk
    img_addresses = {}

    def __init__(self):
        self.current_doc = NegPix.Document(256, 256, "Untitled")
        self.img_addresses = self.current_doc.return_layers()

        self.window = tk.Tk()
        self.window.title(self.appname + ": " + self.current_doc.return_doc_name())

        self.canvas_panel = tk.Frame(self.window).pack(side = "top")




    def create_image_canvas(self):
        images = []
        labels = []

        for key, value in self.img_addresses.items():
            images.append(tk.PhotoImage(file=value))

        for myImage in images:
            labels.append(tk.Label(self.canvas_panel, image = myImage))

        return labels


    def start_loop(self):
        labels = self.create_image_canvas()

        for label in labels:
            label.pack()


        self.window.mainloop()
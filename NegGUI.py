import tkinter as tk
import NegPix
from PIL import Image, ImageTk


class gui:
    appname = "Negarin Pixel"
    current_doc = NegPix
    current_images = NegPix
    image_frame = tk
    tools_frame = tk
    number_of_layers = 1
    window = tk
    red = 0
    green = 0
    blue = 0
    alpha = 0
    new_layer_name = "New Layer"
    file_menu = []
    canvas_panel = tk
    new_layer_frame = tk
    img_addresses = {}

    def __init__(self):
        self.current_doc = NegPix.Document(256, 256, "Untitled")
        self.img_addresses = self.current_doc.return_layers()

        self.window = tk.Tk()
        self.window.title(self.appname + ": " + self.current_doc.return_doc_name())

        self.canvas_panel = tk.Frame(self.window).grid()
        self.new_layer_frame = tk.Frame(self.window).grid()



    def create_image_canvas(self):
        comined_im = self.current_doc.return_display()
        name = "display" + self.current_doc.return_doc_name() + ".png"
        comined_im.save(name)
        im = Image.open(name)
        ph = ImageTk.PhotoImage(im)
        label = tk.Label(self.canvas_panel, image = ph)

        return label



    def start_loop(self):
        label = self.create_image_canvas()
        label.grid()


        red_e = tk.Entry(self.new_layer_frame, width=3)
        green_e = tk.Entry(self.new_layer_frame, width=3)
        blue_e = tk.Entry(self.new_layer_frame, width=3)
        alpha_e = tk.Entry(self.new_layer_frame, width=3)
        red_e.grid()
        green_e.grid()
        blue_e.grid()
        alpha_e.grid()
        red_e.insert(0, "255")
        green_e.insert(0, "255")
        blue_e.insert(0, "255")
        alpha_e.insert(0, "255")
        self.red = int(red_e.get())
        self.green = int(green_e.get())
        self.blue = int(blue_e.get())
        self.alpha = int(alpha_e.get())

        new_layer_button = tk.Button(self.new_layer_frame, text="New Layer", command=self.new_layer)

        new_layer_button.grid()

        self.window.mainloop()


    def new_layer(self):
        self.current_doc.create_layer(int(self.red), int(self.green), int(self.blue), int(self.alpha),
                                      self.new_layer_name + str(self.number_of_layers))
        self.create_image_canvas()
        self.window.update()
        self.number_of_layers += 1
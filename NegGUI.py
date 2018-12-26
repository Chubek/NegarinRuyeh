import tkinter as tk
import NegPix

class gui:
    appname = "Negarin Pixel"
    current_doc = NegPix
    current_images = NegPix
    image_frame = tk
    tools_frame = tk
    window = tk
    file_menu = tk

    def __init__(self):
        self.current_doc = NegPix.Document(2048, 2048, "Untitled")

        self.window = tk.Tk()
        self.window.title(self.appname + ": " + self.current_doc.return_doc_name())




    def start_loop(self):
        self.window.mainloop()
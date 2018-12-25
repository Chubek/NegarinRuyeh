from PIL import Image

class Document:
    width = 1024
    height = 1024
    img = {}
    pixels = {}
    layers = []
    current_layer = ""
    doc_name = "Untitled"

    def __init__(self, name):



    def create_layer(self, r, g, b, alpha, name):
        image = Image.new("RGBA", (1024, 1024), color=(r, g, b, alpha))
        pixel = image.load()

        self.img[name] = image
        self.pixels[name] = pixel

        self.image_save(name)


    def image_save(self, name):
        image = self.img[name]

        image.save(self.doc_name + "___" + name + "___.png")


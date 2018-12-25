from PIL import Image

class Document:
    width = 2048
    height = 2048
    img = {}
    pixels = {}
    layers = []
    images = []
    current_layer = ""
    doc_name = "Untitled"

    def __init__(self, name):
        self.doc_name = name
        self.create_layer(0, 0, 0, 0, "base")


    def create_layer(self, red, green, blue, alpha, name):
        image = Image.new("RGBA", (self.height, self.width), color=(red, green, blue, alpha))
        pixel = image.load()

        self.images.append(image)
        self.img[name] = image
        self.pixels[name] = pixel

        self.image_save(name)


    def create_layer_from_image(self, image, name):
        pixel = image.load()

        self.img[name] = image
        self.pixels[name] = pixel

        self.image_save(name)


    def image_save(self, name):
        image = self.img[name]
        self.layers.append(self.doc_name + "___" + name + "___.png")
        image.save(self.doc_name + "___" + name + "___.png")


    def merge_layers(self):
        combined_im = Image

        for i in range(1, len(self.images)):
            combined_im = Image.alpha_composite(self.images[i-1], self.images[i])

        self.create_layer_from_image(combined_im, "combined" )





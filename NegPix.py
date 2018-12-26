from PIL import Image
import os


class Document:
    width = 2048
    height = 2048
    pixels = {}
    layers = {}
    images = {}
    current_layer = ""
    doc_name = ""
    dirname = ""

    def __init__(self, width, height, name):
        self.doc_name = name
        self.width = width
        self.height = height
        self.create_layer(0, 0, 0, 0, "base")
        self.dirname =  "./" + self.doc_name + "//"
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)

    def create_layer(self, red, green, blue, alpha, name):
        image = Image.new("RGBA", (self.height, self.width), color=(red, green, blue, alpha))
        pixel = image.load()

        self.images[name] = image
        self.pixels[name] = pixel

        self.image_save(name)

    def create_layer_from_image(self, image, name):
        pixel = image.load()

        self.images[name] = image
        self.pixels[name] = pixel

        self.image_save(name)

    def image_save(self, name):
        image = self.images[name]
        self.layers[name] = f"{self.doc_name}/" + self.doc_name + "___" + name + "___.png"
        name = self.doc_name + "___" + name + "___.png"
        image.save(f"{self.doc_name}/" + name, "PNG")


    def merge_layers(self):
        combined_im = Image.new("RGBA", (self.height, self.width), color=(0, 0, 0, 0))
        img = []

        for key, value in self.images.items():
            img.append(value)

        for i in range(1, len(img)):
            combined_im = Image.alpha_composite(img[i-1], img[i])

        self.create_layer_from_image(combined_im, "combined_base" )

    def restart_document(self):
        self.pixels = {}
        self.images = []

        for key, value in self.layers.items():
            os.remove(key)

        self.layers = {}

    def delete_layer(self, name):
        to_remove = self.layers[name]
        os.remove(to_remove)

    def return_layers(self):
        return self.layers

    def return_doc_name(self):
        return self.doc_name

    def return_dimensions(self):
        return (self.width, self.height)

    def return_pixels(self):
        return self.pixels

    def return_images(self):
        return self.images

    def set_size(self, n_height, n_width):
        self.width = n_width
        self.height = n_height


    def return_display(self):
        combined_im = Image.new("RGBA", (self.height, self.width), color=(0, 0, 0, 0))
        img = []

        for key, value in self.images.items():
            img.append(value)

        for i in range(1, len(img)):
            combined_im = Image.alpha_composite(img[i-1], img[i])

        return combined_im
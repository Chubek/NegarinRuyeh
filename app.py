import NegPix

doc = NegPix.Document("myDocument")

doc.create_layer(25, 22, 100, 200, "Layer1")
doc.create_layer(54, 32, 11, 20, "Layer2")
doc.create_layer(225, 242, 0, 190, "layer3")
doc.merge_layers()
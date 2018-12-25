import tkinter as tk
from PIL import Image

def tinker(img, pos, color):
    pixels = img.load()
    x = pos[0]
    y = pos[1]

    if (x > 10 and y > 10) and (x < 246 and y < 246):
        for i in range(10):
            for j in range(10):
                pixels[x+i, y+j] = color

    elif x < 10 and y < 10:
        x = 10
        y = 10
    elif x > 253 and y > 253:
        x = 246
        y = 246


    img.save("image.png")


root = tk.Tk()

img = Image.new("RGB", (256, 256), color="white")
img.save("image.png")
openimg = tk.PhotoImage(file="image.png")
panel = tk.Label(root, image=openimg)
panel.pack(side="bottom", fill="both", expand="yes")


def callback(e):
    x, y = e.x, e.y
    print(f"({x}, {y})")
    tinker(img, pos=(x, y), color=(0, 0, 0))
    img2 = tk.PhotoImage(file="image.png")
    panel.configure(image=img2)
    panel.image = img2


root.bind("<B1-Motion>", callback)
root.mainloop()



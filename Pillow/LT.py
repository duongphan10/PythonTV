from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np


img = Image.open("Anh.jpg")
#img.show()
print(img.size)

draw = ImageDraw.Draw(img)
draw.ellipse((180, 320, 300, 450), outline=(255,255,255))
draw.ellipse((320, 320, 440, 450), outline=(255,255,255))

draw.line((300, 400, 325, 400), fill=(255, 255, 255), width=2)
img.show()
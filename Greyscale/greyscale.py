from PIL import Image
import math

#Open and load the image.
im = Image.open("birds.png")
im.load()

#Grab the width and the height.
width = im.size[0]
height = im.size[1]

#Iterate through each pixel in the image and calculate the grey to convert
#it to. Then change the color of the pixel to that grey. This uses the
#Luma algorithm.
for p_x in range(width):
    for p_y in range(height):
        p = (p_x, p_y)
        pixel = im.getpixel(p)
        grey = math.floor(pixel[0] * 0.2126 + pixel[1] * 0.7162 + pixel[2] * 0.0722)
        grey_pixel = (grey, grey, grey)
        im.putpixel(p, grey_pixel) 

#Saves greyscale image.
im.save("bird-grey.png", "PNG")

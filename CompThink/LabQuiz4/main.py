# -*- coding: utf-8 -*-
"""
Lab Quiz 4 Version E
Parker Sweeney 01389288
12/04/2023
main_mod.py

"""

from images import Image
from func_mod import half_change

'''# Comment this out once func_mod is connected. This wont need to be here after that
def half_change(image1, degree):
    """Lightens the left half of the image and darkens the right half by the given degree amount"""
    #degree = input("Give the degree which you will lighten the left half and darken the right half: ")
    for y in range(image1.getHeight()):
        for x in range(image1.getWidth()):
            (r, g, b) = image1.getPixel(x, y)
           # Right Hand Side 
            if x > image1.getWidth()//2:
               r = int(r - degree)
               if r < 0:
                   r = 0
               g = int(g - degree)
               if g < 0:
                   g = 0
               b = int(b - degree)
               if b < 0:
                   b = 0
               lum = r + g + b
               image1.setPixel(x, y, (lum, lum, lum))
           # Left Hand Side
            else:
                r = int(r + degree)
                if r > 255:
                    r = 255
                g = int(g + degree)
                if g > 255:
                    g = 255
                b = int(b + degree)
                if b > 255:
                    b = 255
                lum = r + g + b
                image1.setPixel(x, y, (lum, lum, lum))
    return image1
'''

def main():
    filename = input("Enter the image file name: ")
    degree = int(input("Give the degree which you will lighten the left half and darken the right half: "))
    image1 = Image(filename)
    #Invert image
    half_change(image1,degree)
    image1.save("newimage.gif")
    image1.draw()

if __name__ == "__main__":
   main()

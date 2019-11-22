"""ECOR 1051 - Fall 2019
Group L5_6 - Milestone 2, P4 
Submitted on: 17/11/2019"""

from Cimpl import *

def two_tone(filename: str, colour_1: str, colour_2: str) -> Image:
    """Function takes a filename of an image as a string, assuming the image is 
    saved in the same folder (same path) as the function, and two colours as 
    strings from the given list:
    black
    white
    red
    lime
    blue
    yellow
    cyan
    magenta
    gray
    
    Function returns an image in two tones as per the colours given in the 
    second and third function parameters, decided by an individual pixel's 
    brightness.
    -Function written by Nathan Gomes, 101143780
    
    >>> two_tone(image_1, "red", "gray")
    #Displays the original image first and then the image with only red and gray
    >>> two_tone(image_1, "black", "pink")
    #Error because colour passed ("pink") is not in the given list
    """
    image = load_image(filename)
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    L = [("black", black), ("white", white), ("red", red), ("lime", lime), 
         ("blue", blue), ("yellow", yellow), ("cyan", cyan), 
         ("magenta", magenta), ("gray", gray)]
    
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        average = (r+g+b)/3
        if (average >= 0) and (average < 128):
            for i in range(len(L)):
                if colour_1 == L[i][0]:
                    set_color(new_image, x, y, L[i][1])
        elif (average > 127) and (average < 256):
            for i in range(len(L)):
                if colour_2 == L[i][0]:
                    set_color(new_image, x, y, L[i][1])
    
    return show(image), show(new_image)

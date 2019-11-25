"""ECOR 1051 - Fall 2019

Group L5_6 - Milestone 2, P4 
File contains the three_tone filter.
Submitted on: 17/11/2019"""

from Cimpl import load_image, choose_file, create_color, copy,\
                  set_color, Image, show

def three_tone(image: Image, colour_1: str, colour_2: str, colour_3: str)\
    -> Image:
    """
    Function takes an image and three colours as strings from the given 
    list:
    black
    white
    red
    lime
    blue
    yellow
    cyan
    magenta
    gray
    
    Function returns an image in three tones as per the colours given in the 
    second, third and fourth function parameters, decided by an individual 
    pixel's brightness.
    -Function written by Nathan Gomes, 101143780
    
    >>> image_1 = load_image(choose_file())
    >>> three_tone_image = three_tone(image_1, "blue", "gray", "white")
    >>> show(three_tone_image)
    >>> three_tone(image_1, "yellow", "cyan", "purple")
    #Error because colour passed ("purple") is not in the given list
    """
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    colours = [("black", black), ("white", white), ("red", red), 
               ("lime", lime), ("blue", blue), ("yellow", yellow), 
               ("cyan", cyan), ("magenta", magenta), ("gray", gray)]
    
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        average = (r + g + b) / 3
        if (average >= 0) and (average < 85):
            for i in range(len(colours)):
                if colour_1 == colours[i][0]:
                    set_color(new_image, x, y, colours[i][1])
        elif (average > 84) and (average < 171):
            for i in range(len(colours)):
                if colour_2 == colours[i][0]:
                    set_color(new_image, x, y, colours[i][1])
        elif (average > 170) and (average < 256):
            for i in range(len(colours)):
                if colour_3 == colours[i][0]:
                    set_color(new_image, x, y, colours[i][1])        
                            
    return new_image

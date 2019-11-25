""" ECOR 1051 Fall 2019

Function for edge detection filter.
Last edited: Nov. 24, 2019
"""
from Cimpl import (create_color, get_color, Image, load_image, show,
                   choose_file, copy, set_color, get_height, get_width)

def detect_edges(original_image: Image, threshold: float) -> Image:
    """Takes an image, makes a copy of it and changes the color of the pixels
    to black or white, depending on their contrast.
    
    - Function written by Malak Abdou - 101139692
    
    >>> original_image = load_image(choose_file())
    >>> show(detect_edges(original_image, 15))
    # Returns image with detect_edges filter applied with a threshold of 15
    without modifying original.
    """
    
    original2 = copy(original_image)
    
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    
    for x in range(get_width(original2)):
        
        for y in range(get_height(original2) - 1):

            r, g, b = get_color(original2, x, y)
            r1, g1, b1 = get_color(original2, x, (y + 1))
                
            brightness = (r + g + b) / 3
            brightness1 = (r1 + g1 + b1) / 3
            
            if abs(brightness - brightness1) > threshold:
                set_color(original2, x, y, black) 
            else:
                set_color(original2, x, y, white)
                
    return original2
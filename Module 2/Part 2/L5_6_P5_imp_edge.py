""" ECOR 1051 Fall 2019

Milestone 2
L5_6_P5
Functions for improved edge detection.
Last edited: Nov. 20, 2019
"""

from Cimpl import *

file = choose_file()
original_image = load_image(file)

def imp_edge(origininal_image: Image, threshold :float) -> Image:
    """Returns an image that looks like a pencil sketch of the original image,
    changing the pixels' colors to black or white.
    - Function written by Leanne Matamoros - 101147405
    
    >>> imp_edge(original_image, 15)
    <Cimpl.Image object at 0x000002096DEEA148>
    """
    edges_copy = copy(original_image)
    
    width = get_width(edges_copy)
    height = get_height(edges_copy)

    for x in range(width):
        for y in range(height):

            r, g, b = get_color(edges_copy, x, y)
            brightness = (r + g + b) / 3
            
            if y != (height -1):
                r1, g1, b1 = get_color(edges_copy, x, (y+1))
                brightness1 = (r1 + g1 + b1) / 3
            
            if x != (width -1):
                r2, g2, b2 = get_color(edges_copy, (x+1), y)
                brightness2 = (r2 + g2 + b2) / 3

            black = create_color(0,0,0)
            white = create_color(255,255,255)

            if x == (width -1) and y == (height -1):
                set_color(edges_copy, x, y, white)
                
            elif x != (width -1) or y != (height -1):
                if abs(brightness - brightness1) > threshold or abs(brightness - brightness2) > threshold:
                    set_color(edges_copy, x, y, black)
            
                elif abs(brightness - brightness1) < threshold or abs(brightness - brightness2) < threshold:
                    set_color(edges_copy, x, y, white)
                    
            elif x == (width -1):
                if abs(brightness - brightness1) > threshold:
                    set_color(edges_copy, x, y, black)
    
                elif abs(brightness - brightness1) < threshold:
                    set_color(edges_copy, x, y, white)
                    
            elif y == (height -1):
                if abs(brightness - brightness2) > threshold:
                    set_color(edges_copy, x, y, black)
    
                elif abs(brightness - brightness2) < threshold:
                    set_color(edges_copy, x, y, white)

    return edges_copy
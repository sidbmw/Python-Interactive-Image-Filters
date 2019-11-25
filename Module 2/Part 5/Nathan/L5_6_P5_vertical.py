"""ECOR 1051 - Fall 2019

Group L5_6 - Milestone 2, P5
File contains the flip_vertical function.
Submitted on: 22/11/2019"""

from Cimpl import load_image, choose_file, create_color, copy,\
                  set_color, Image, show

def flip_vertical(image: Image) -> Image:
    """Function author : Nathan Gomes - 101143780
    Function takes an image and returns a copy of the image that has been
    flipped vertically (across the "y" axis in an x-y co-ordinate system).
    
    >>> original_image = load_image("filename")
    >>> flip_vertical(original_image)
    <Cimpl.Image object at 0x000001A90D7A7408>
    """
    
    new_image = copy(image)
    mid_pixel = get_width(new_image)//2
    width = get_width(new_image)
    height = get_height(new_image)
    
    for x in range(mid_pixel):  
        for y in range(height): 
            r, g, b = get_color(image, x, y)
            new_r, new_g, new_b = get_color(image, abs(width-x)-1, y)
            set_color(new_image, x, y, create_color(new_r, new_g, new_b))
            set_color(new_image, width-x-1, y, create_color(r, g, b))
            
    return new_image
#Group L5_6 - Milestone 2, P5 - Submitted on: 22/11/2019
from Cimpl import *
import Cimpl

def flip_vertical(image: Image) ->Image:
    """
    Author : Nathan Gomes - 101143780
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

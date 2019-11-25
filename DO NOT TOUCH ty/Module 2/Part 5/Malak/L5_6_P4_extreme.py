""" ECOR 1051 Fall 2019

Function for applying the extreme contrast filter.
Last edited: Nov. 24, 2019
"""
from Cimpl import (create_color, get_color, Image, load_image, show,
                   choose_file, copy, set_color)

def extreme_contrast(original_image: Image) -> Image:
    """Returns the 'extreme contrast' version of an image without having
    modified it.
    - Function written by Malak Abdou - 101139692
    
    >>> original_image = load_image(choose_file())
    >>> show(extreme_contrast(original_image))
    # Returns a copy of original_image with extreme_contrast filter on it.
    """
    extreme_copy = copy(original_image)
    for pixel in extreme_copy:
        x, y, (r, g, b) = pixel
        if r <= 127:
            r = 0
        else:
            r = 255
        if g <= 127:
            g = 0
        else:
            g = 255
        if b <= 127:
            b = 0
        else:
            b = 255
        extreme_color = create_color(r,g,b)
        set_color(extreme_copy, x, y, extreme_color) 
    return extreme_copy
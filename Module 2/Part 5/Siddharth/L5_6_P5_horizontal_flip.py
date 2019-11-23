"""
ECOR 1051 Fall 2019
Group Number: L5-6

Horizontal flip function
"""

from Cimpl import *

file = choose_file()
original_image = load_image(file)


def flip_horizontal(original_image: Image) -> Image:
    """ Author: Siddharth Natamai - 1011403016
        Date: Nov 19, 2019

    Returns a original_image after flipping along the x-axis (horizontal flip)
    >>> flip_horizontal(original_image)
    <Cimpl.original_image object at 0x7f7ba88dbd10>
    """

    new_image = copy(original_image)
    img_width = get_width(new_image)
    img_height = get_height(new_image)
    img_center = img_height // 2

    for x in range(img_width):
        for y in range(img_center):
            r, g, b = get_color(new_image, x, y)
            r2, g2, b2 = get_color(new_image, x, img_height - y - 1)
            set_color(new_image, x, y, create_color(r2, g2, b2))
            set_color(new_image, x, img_height - y - 1, create_color(r, g, b))

    return new_image


show(flip_horizontal(original_image))
# flip_horizontal(original_image)

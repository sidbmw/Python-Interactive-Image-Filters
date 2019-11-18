from Cimpl import *

file = choose_file()
original_image = load_image(file)


def posterize(original_image: original_image) -> original_image:
    """ Author: Siddharth Natamai - 1011403016
        Date: Nov 17, 2019

    Returns a image after applying a posterizing filter based on values from the _adjust_component function
    >>> posterize(original_image)
    <Cimpl.Image object at 0x7f7ba88dbd10>
    """
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        set_color(original_image, x, y, create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)))
    return new_image


def _adjust_component(original_val: int) -> int:
    """Determines where each pixel lies in the 4 quadrants (0 to 63, 64 to 127, 128 to 191, and 192 to 255)
    and sets the new pixel values to the midpoint of that specific quadrant.
    >>> _adjust_component(50)
    31
    >>> _adjust_component(90)
    95
    >>> _adjust_component(155)
    159
    """

    if original_val <= 63:
        new_val = 31
    elif original_val <= 127:
        new_val = 95
    elif original_val <= 191:
        new_val = 159
    elif original_val <= 255:
        new_val = 223
    return new_val

# print(_adjust_component(192))
#
# show(posterize(original_image))
# save(posterize(original_image))

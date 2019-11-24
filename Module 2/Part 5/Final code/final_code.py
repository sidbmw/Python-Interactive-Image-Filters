from Cimpl import copy, get_width, get_height, get_color, set_color, \
    create_color


def _adjust_component(original_val: int) -> int:
    """Author: Prof. Donald Bailey
    Determines where each pixel lies in the 4 quadrants (0 to 63, 64 to 127,
     128 to 191, and 192 to 255)
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


def combine(red_pic: Image, green_pic: Image, blue_pic: Image) -> Image:
    # Author: Siddharth Natamai - 101143016
    """Combines the inputted images and returns the final image
    >>> combine(image_1, image_2, image_3)
    <Cimpl.Image object at 0x7fab575d3ad0>
    """
    final_image = copy(red_pic)
    for pixel in final_image:
        x, y, (r, g, b) = pixel
        blue_colour = get_color(blue_pic, x, y)
        green_colour = get_color(green_pic, x, y)
        new_colours = create_color(r, green_colour[1], blue_colour[2])
        set_color(final_image, x, y, new_colours)

    return final_image


def posterize(original_image: Image) -> Image:
    """ Author: Siddharth Natamai - 1011403016
        Date: Nov 17, 2019

    Returns a image after applying a posterizing filter based on values from
    the_adjust_component function
    >>> posterize(original_image)
    <Cimpl.Image object at 0x7f7ba88dbd10>
    """
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        set_color(original_image, x, y, create_color(_adjust_component(r),
                                                     _adjust_component(g),
                                                     _adjust_component(b)))
    return new_image


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

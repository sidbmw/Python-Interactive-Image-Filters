"""ECOR 1051 - Milestone 3
Group: L5_6
Date of Submission: Dec 1, 2019
Authors: Siddharth Natamai - 101143016
        Leanne Matamoros - 101147405
        Malak Abdou - 101139692
        Nathan Gomes - 101143780

Version: 1.0.0
"""

from Cimpl import get_height, get_width, choose_file, load_image, copy, \
    set_color, create_color, \
    get_color, Image, show


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


def check_equal(description: str, outcome, expected) -> None:
    """
    Author: Prof. Donald L. Bailey
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected,
                     str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def grayscale(image: Image) -> Image:
    """Author: Prof. Donald Bailey
    Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    return new_image


# def combine(red_pic: Image, green_pic: Image, blue_pic: Image) -> Image:
#     # Author: Siddharth Natamai - 101143016
#     """Combines the inputted images and returns the final image
#     >>> combine(image_1, image_2, image_3)
#     <Cimpl.Image object at 0x7fab575d3ad0>
#     """
#     final_image = copy(red_pic)
#     for pixel in final_image:
#         x, y, (r, g, b) = pixel
#         blue_colour = get_color(blue_pic, x, y)
#         green_colour = get_color(green_pic, x, y)
#         new_colours = create_color(r, green_colour[1], blue_colour[2])
#         set_color(final_image, x, y, new_colours)
#
#     return final_image


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
        set_color(new_image, x, y, create_color(_adjust_component(r),
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


def sepia(original_image: Image) -> Image:
    """Returns a black and white image which has been tinted yellow.
    - Function written by Leanne Matamoros - 101147405
    >>> original_image = load_image(choose_file())
    >>> sepia(original_image)
    <Cimpl.Image object at 0x00000212C566DD88>

    """
    new_image = copy(original_image)
    sepia_filter = grayscale(new_image)

    for pixel in sepia_filter:
        x, y, (r, g, b) = pixel
        if r < 63:
            r *= 1.1
            b *= 0.9

        if 63 <= r <= 191:
            r *= 1.15
            b *= 0.85

        if r > 191:
            r *= 1.08
            b *= 0.93

        new_color = create_color(r, g, b)
        set_color(sepia_filter, x, y, new_color)

    return sepia_filter


def detect_edges_better(original_image: Image, threshold: float) -> Image:
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

            if y != (height - 1):
                r1, g1, b1 = get_color(edges_copy, x, (y + 1))
                brightness1 = (r1 + g1 + b1) / 3

            if x != (width - 1):
                r2, g2, b2 = get_color(edges_copy, (x + 1), y)
                brightness2 = (r2 + g2 + b2) / 3

            black = create_color(0, 0, 0)
            white = create_color(255, 255, 255)

            if x == (width - 1) and y == (height - 1):
                set_color(edges_copy, x, y, white)

            elif x != (width - 1) or y != (height - 1):
                if abs(brightness - brightness1) > threshold or abs(
                        brightness - brightness2) > threshold:
                    set_color(edges_copy, x, y, black)

                elif abs(brightness - brightness1) < threshold or abs(
                        brightness
                        - brightness2) < threshold:
                    set_color(edges_copy, x, y, white)

            elif x == (width - 1):
                if abs(brightness - brightness1) > threshold:
                    set_color(edges_copy, x, y, black)

                elif abs(brightness - brightness1) < threshold:
                    set_color(edges_copy, x, y, white)

            elif y == (height - 1):
                if abs(brightness - brightness2) > threshold:
                    set_color(edges_copy, x, y, black)

                elif abs(brightness - brightness2) < threshold:
                    set_color(edges_copy, x, y, white)

    return edges_copy


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
        extreme_color = create_color(r, g, b)
        set_color(extreme_copy, x, y, extreme_color)
    return extreme_copy


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

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

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


# def blue_channel(image: Image) -> Image:
#     """Function takes an image and applies a blue channel filter over the image
#     without affecting the original image and returns a filtered new image.
#     -Function written by Nathan Gomes - 101143780
#
#     >>> original_image = load_image(choose_file())
#     >>> blue_image = blue_channel(original_image)
#     >>> show(blue_image)
#     """
#
#     new_image = copy(image)
#     for pixel in image:
#         x, y, (r, g, b) = pixel
#         blue_increased = create_color(r - r, g - g, b)
#         set_color(new_image, x, y, blue_increased)
#
#     return new_image


# def red_channel(original_image: Image) -> Image:
#     """Returns the red channel of image without having modified it.
#     - Function written by Malak Abdou - 101139692
#
#     >>> red_channel(original_image)
#     <Cimpl.Image object at 0x000001C447BDFAC8>
#     """
#     red_filter = copy(original_image)
#     for pixel in original_image:
#         x, y, (r, g, b) = pixel
#         red = create_color(r, 0, 0)
#         set_color(red_filter, x, y, red)
#     return red_filter


# def green_channel() -> Image:
#     """Returns the green chanel of the initial image without having modified it.
#     -Function written by Leanne Matamoros - 101147405
#
#     >>> green_channel(original_image)
#     <Cimpl.Image object at 0x0000028A06CD6D88>
#     """
#     file = choose_file()
#     original_image = load_image(file)
#     green_filter = copy(original_image)
#
#     for pixel in original_image:
#         x, y, (r, g, b) = pixel
#         green_coloration = create_color(0, g, 0)
#         set_color(green_filter, x, y, green_coloration)
#
#     return green_filter


def three_tone(image: Image, colour_1: str, colour_2: str, colour_3: str) \
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


def two_tone(image: Image, colour_1: str, colour_2: str) -> Image:
    """Function an image and two colours as strings from the given list:
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

    >>> image = load_image(choose_file())
    >>> two_tone_image = two_tone(image, "red", "gray")
    >>> show(two_tone_image)
    >>> two_tone(image, "black", "pink")
    #Error because colour passed ("pink") is not in the given list
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

        if (average >= 0) and (average < 128):
            for i in range(len(colours)):
                if colour_1 == colours[i][0]:
                    set_color(new_image, x, y, colours[i][1])

        elif (average > 127) and (average < 256):
            for i in range(len(colours)):
                if colour_2 == colours[i][0]:
                    set_color(new_image, x, y, colours[i][1])

    return new_image


def flip_vertical(image: Image) -> Image:
    """Function author : Nathan Gomes - 101143780
    Function takes an image and returns a copy of the image that has been
    flipped vertically (across the "y" axis in an x-y co-ordinate system).

    >>> original_image = load_image("filename")
    >>> flip_vertical(original_image)
    <Cimpl.Image object at 0x000001A90D7A7408>
    """

    new_image = copy(image)
    mid_pixel = get_width(new_image) // 2
    width = get_width(new_image)
    height = get_height(new_image)

    for x in range(mid_pixel):
        for y in range(height):
            r, g, b = get_color(image, x, y)
            new_r, new_g, new_b = get_color(image, abs(width - x) - 1, y)
            set_color(new_image, x, y, create_color(new_r, new_g, new_b))
            set_color(new_image, width - x - 1, y, create_color(r, g, b))

    return new_image

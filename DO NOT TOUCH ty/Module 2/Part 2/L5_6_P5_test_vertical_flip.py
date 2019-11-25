"""
ECOR 1051 Fall 2019
Group: L5-6

Test function for the flip_vertical function.

Program prints whether the test passed or failed along with which pixels failed/passed.
"""

from Cimpl import *


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
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def flip_vertical(image: Image) -> Image:
    # """Function author : Nathan Gomes - 101143780
    # Function takes an image and returns a copy of the image that has been
    # flipped vertically (across the "y" axis in an x-y co-ordinate system).
    #
    # >>> original_image = load_image("filename")
    # >>> flip_vertical(original_image)
    # <Cimpl.Image object at 0x000001A90D7A7408>
    # """

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


def test_vertical_flip():
    """
    Author: Siddharth Natamai - 101143016
    Tests the flip_vertical function.

    >>> test_vertical_flip()
    """

    # Create a image with a resolution of 4x2 (8 pixels in total)
    original = create_image(4, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 0))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 3, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(0, 0, 0))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(255, 255, 255))
    set_color(original, 3, 1, create_color(255, 255, 255))

    # Expected image after passing into the flip_vertical function.
    expected = create_image(4, 2)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 2, 1, create_color(0, 0, 0))
    set_color(expected, 3, 1, create_color(0, 0, 0))

    flipped_image = flip_vertical(original)

    # Checks each pixel and prints 'PASSED' or 'FAILED' based on expected image values and image passed into flip_vertical
    for x, y, col in flipped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


test_vertical_flip()

from Cimpl import set_color, create_color, get_color, create_image, Image
from final_code import _adjust_component, posterize, flip_horizontal, sepia, \
    detect_edges_better, extreme_contrast, detect_edges, blue_channel, \
    three_tone, flip_vertical, check_equal

from final_code import two_tone as tt


def test_detect_edge() -> None:
    """Returns whether the edge detection filter works and if it didn't,\
    indicates where it wasn't applied.
    -Test function written by Leanne Matamoros - 101147405

    >>> test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------

    >>> test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) FAILED: expected Color(red=255, green=255,\
    blue=255), got Color(red=0, green=0, blue=0)
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------
    """
    original = create_image(5, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 10, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))

    set_color(original, 0, 1, create_color(10, 30, 3))
    set_color(original, 1, 1, create_color(67, 90, 1))
    set_color(original, 2, 1, create_color(0, 2, 20))
    set_color(original, 3, 1, create_color(189, 53, 222))
    set_color(original, 4, 1, create_color(145, 136, 198))

    expected = create_image(5, 2)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))

    # The last row's value stay the same do to the criterias of the edge
    # detection filter.

    set_color(expected, 0, 1, create_color(10, 30, 3))
    set_color(expected, 1, 1, create_color(67, 90, 1))
    set_color(expected, 2, 1, create_color(0, 2, 20))
    set_color(expected, 3, 1, create_color(189, 53, 222))
    set_color(expected, 4, 1, create_color(145, 136, 198))

    # threshold is assigned 15 for this test

    image_edge = detect_edges(original, 15)

    for x, y, col in image_edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_extreme() -> None:
    """A test function for extreme contrast.
    -Test function written by Leanne Matamoros - 101147405

    >>> test_extreme()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------

    >>> test_extreme()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) FAILED: expected Color(red=0, green=0, blue=255),\
    got Color(red=0, green=0, blue=25)
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------
    """
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(255, 255, 255))
    set_color(expected, 5, 0, create_color(255, 255, 255))

    extreme_image = extreme_contrast(original)
    for x, y, col in extreme_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


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

    # Checks each pixel and prints 'PASSED' or 'FAILED' based on expected
    # image values and image passed into flip_vertical
    for x, y, col in flipped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_three_tone(original_image: Image):
    """ Author: Siddharth Natamai - 101143016
        Date: Nov 17, 2019

        Returns a bool depending on whether the the function is working
        properly or not
        >>> test_three_tone()
        True
        >>> test_three_tone()
        False
    """
    filtered_image = three_tone(original_image, "black", "white", "lime")
    test_state = True

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] +
                         color_original[2]) // 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)
        colour_3 = create_color(0, 255, 0)

        test_state = bool(
            (color_average <= 84 and color_filtered == colour_1)
            or ((84 < color_average <= 170) and color_filtered == colour_2)
            or (color_average >= 171 and color_filtered == colour_3))

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


def test_two_tone(original_image: Image):
    """ Author: Siddharth Natamai - 101143016
        Date: Nov 17, 2019

        Returns a bool depending on whether the the function is working
        properly or not.
        >>> test_two_tone()
        True
        >>> test_two_tone()
        False
        """
    filtered_image = tt(original_image, "black", "white")
    test_state = True

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] +
                         color_original[2]) // 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)

        if color_average <= 127 and color_filtered == colour_1 \
                or color_average >= 128 and color_filtered == colour_2:
            test_state = True
        else:
            test_state = False

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


def test_sepia() -> None:
    """Returns the information on whether or not the sepia filter works
    properly or not. The function returns the pixels that have passed the
    test. All pixels have to pass in order to confirm the success of the
    sepia filter. Otherwise, the filter does not work properly.

    - Function written by Malak Abdou - 101139692

    >>> test_sepia()
    (0,0) PASSED
    (1,0) PASSED
    (2,0) PASSED
    (3,0) PASSED
    (0,1) PASSED
    (1,1) PASSED
    (2,1) PASSED
    (3,1) PASSED

    References: check_equal function from fib2.py, provided by ECOR 1051
    staff.
    """
    original = create_image(4, 2)

    set_color(original, 0, 0, create_color(15, 250, 8))
    set_color(original, 1, 0, create_color(8, 20, 11))
    set_color(original, 2, 0, create_color(5, 55, 15))
    set_color(original, 3, 0, create_color(32, 206, 56))

    set_color(original, 0, 1, create_color(93, 51, 240))
    set_color(original, 1, 1, create_color(11, 23, 41))
    set_color(original, 2, 1, create_color(54, 26, 190))
    set_color(original, 3, 1, create_color(21, 68, 49))

    expected = create_image(4, 2)

    set_color(expected, 0, 0, create_color(104.65, 91, 77.35))
    set_color(expected, 1, 0, create_color(14.3, 13, 11.7))
    set_color(expected, 2, 0, create_color(27.5, 25, 22.5))
    set_color(expected, 3, 0, create_color(112.7, 98, 83.3))

    set_color(expected, 0, 1, create_color(147.2, 128, 108.8))
    set_color(expected, 1, 1, create_color(27.5, 25, 22.5))
    set_color(expected, 2, 1, create_color(103.5, 90, 76.5))
    set_color(expected, 3, 1, create_color(50.6, 46, 41.4))

    sepia_image = sepia(original)

    for x, y, color in sepia_image:
        check_equal('(' + str(x) + ',' + str(y) + ')', color,
                    get_color(expected, x, y))

    def test_detect_edges_better() -> None:
        """Returns the information on whether or not the filter
        detect_edges_better works properly or not. The function returns the
        pixels that have passed the test. All pixels have to pass in order to
        confirm the success of the detect_edges_better filter. Otherwise, the
        filter does not work properly.

        -Function written by Malak Abdou - 101139692

        >>> test_detect_edges_better()
        (0,0) PASSED
        (1,0) PASSED
        (2,0) PASSED
        (3,0) PASSED
        (0,1) PASSED
        (1,1) PASSED
        (2,1) PASSED
        (3,1) PASSED

        References: check_equal function from fib2.py, provided by ECOR 1051
        staff.
        """

        black = create_color(0, 0, 0)
        white = create_color(255, 255, 255)

        original = create_image(4, 2)

        set_color(original, 0, 0, create_color(15, 250, 7))
        set_color(original, 1, 0, create_color(8, 19, 10))
        set_color(original, 2, 0, create_color(5, 55, 15))
        set_color(original, 3, 0, create_color(32, 206, 56))

        set_color(original, 0, 1, create_color(43, 50, 21))
        set_color(original, 1, 1, create_color(11, 23, 40))
        set_color(original, 2, 1, create_color(54, 26, 190))
        set_color(original, 3, 1, create_color(21, 68, 48))

        expected = create_image(4, 2)

        set_color(expected, 0, 0, create_color(0, 0, 0))
        set_color(expected, 1, 0, create_color(255, 255, 255))
        set_color(expected, 2, 0, create_color(0, 0, 0))
        set_color(expected, 3, 0, create_color(0, 0, 0))

        set_color(expected, 0, 1, create_color(255, 255, 255))
        set_color(expected, 1, 1, create_color(0, 0, 0))
        set_color(expected, 2, 1, create_color(0, 0, 0))
        set_color(expected, 3, 1, create_color(255, 255, 255))

        threshold = 15  # Assume threshold chosen is 15.

        edges_image = detect_edges_better(original, threshold)

        for x, y, color in edges_image:
            check_equal('(' + str(x) + ',' + str(y) + ')', color,
                        get_color(expected, x, y))


def test_red() -> None:
    """Tests the red_channel function. Returns PASS if all pixels in red_image
    have 0 green and blue components.
    - Function written by Malak Abdou - 101139692

    >>> test_red()
    PASS
    """

    show(red_image)
    r, g, b = get_color(red_image, 0, 0)
    if g == 0 and b == 0:
        print('PASS')
    else:
        print('FAIL')


def test_blue_channel() -> None:
    """Function tests the blue_channel filter.
    -Function written by Nathan Gomes - 101143780

    >>> blue_channel_test()
    (0, 0) PASSED
    ------
    (1, 0) PASSED
    ------
    (2, 0) PASSED
    ------
    >>> blue_channel_test()
    (0, 0) PASSED
    ------
    (1, 0) FAILED: expected Color(red=0, green=0, blue=202), got Color(red=0, green=0, blue=201)
    ------
    (2, 0) PASSED
    ------
    """

    original_image = create_image(3, 1)
    set_color(original_image, 0, 0, create_color(255, 255, 255))
    set_color(original_image, 1, 0, create_color(78, 146, 201))
    set_color(original_image, 2, 0, create_color(167, 64, 29))

    expected_image = create_image(3, 1)
    set_color(expected_image, 0, 0, create_color(0, 0, 255))
    set_color(expected_image, 1, 0, create_color(0, 0, 201))
    set_color(expected_image, 2, 0, create_color(0, 0, 29))

    blue_image = blue_channel(original_image)

    for x, y, col in blue_image:
        check_equal("(" + str(x) + ", " + str(y) + ")", col,
                    get_color(expected_image, x, y))


def test_posterize() -> None:
    """Function is called without any arguments, calls the posterize filter
    within the function body on a preset image and tests it.
    Function Author: Nathan Gomes - 101143780

    >>> test_posterize()
    (0, 0) PASSED
    ------
    (1, 0) PASSED
    ------
    (2, 0) PASSED
    ------
    >>> test_posterize()
    (0, 0) PASSED
    ------
    (1, 0) FAILED: expected Color(red=31, green=31, blue=32), got Color(red=31, green=31, blue=31)
    ------
    (2, 0) PASSED
    ------
    """

    original_image = create_image(3, 1)
    set_color(original_image, 0, 0, create_color(255, 255, 255))
    set_color(original_image, 1, 0, create_color(0, 0, 0))
    set_color(original_image, 2, 0, create_color(167, 97, 29))
    # These pixels represent two boundary cases and one in which each
    # component represents a different quadrant.

    expected_image = create_image(3, 1)
    set_color(expected_image, 0, 0, create_color(223, 223, 223))
    set_color(expected_image, 1, 0, create_color(31, 31, 31))
    set_color(expected_image, 2, 0, create_color(159, 95, 31))

    poster_image = posterize(original_image)

    for x, y, col in poster_image:
        check_equal("(" + str(x) + ", " + str(y) + ")", col,
                    get_color(expected_image, x, y))


def flip_horizontal_test() -> None:
    """Function Author: Nathan Gomes - 101143780
    A test function for flip_horizontal filter.

    >>> flip_horizontal_test()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(0, 3) PASSED
    ------
    Checking pixel @(1, 3) PASSED
    ------
    """

    original_image = create_image(2, 4)
    set_color(original_image, 0, 0, create_color(0, 0, 0))
    set_color(original_image, 0, 1, create_color(255, 255, 255))
    set_color(original_image, 0, 2, create_color(0, 0, 0))
    set_color(original_image, 0, 3, create_color(255, 255, 255))
    set_color(original_image, 1, 0, create_color(255, 255, 255))
    set_color(original_image, 1, 1, create_color(0, 0, 0))
    set_color(original_image, 1, 2, create_color(255, 255, 255))
    set_color(original_image, 1, 3, create_color(0, 0, 0))

    # I only used two colours in my pixels because the positions of those two
    # colours will be more than enough to demonstrate rotation.

    expected_image = create_image(2, 4)
    set_color(expected_image, 0, 0, create_color(255, 255, 255))
    set_color(expected_image, 0, 1, create_color(0, 0, 0))
    set_color(expected_image, 0, 2, create_color(255, 255, 255))
    set_color(expected_image, 0, 3, create_color(0, 0, 0))
    set_color(expected_image, 1, 0, create_color(0, 0, 0))
    set_color(expected_image, 1, 1, create_color(255, 255, 255))
    set_color(expected_image, 1, 2, create_color(0, 0, 0))
    set_color(expected_image, 1, 3, create_color(255, 255, 255))

    horizontal_image = flip_horizontal(original_image)

    for x, y, col in horizontal_image:
        check_equal("Checking pixel @(" + str(x) + ', ' + str(y) + ')', col,
                    get_color(expected_image, x, y))


def test_adjust_component() -> None:
    """Function tests the helper function "_adjust_component."
    -Written by Nathan Gomes, 101143780

    >>> test_adjust_component()
    (0, 0) PASSED
    ------
    >>> test_adjust_component()
    (0, 0) FAILED: expected Color(red=31, green=95, blue=158), got Color(red=31, green=95, blue=159)
    ------

    """

    original_image = create_image(1, 1)
    set_color(original_image, 0, 0, create_color(50, 90, 155))

    expected_image = create_image(1, 1)
    set_color(expected_image, 0, 0, create_color(31, 95, 159))

    r, g, b = get_color(original_image, 0, 0)
    adjusted_image = create_image(1, 1)
    set_color(adjusted_image, 0, 0,
              create_color(_adjust_component(r),
                           _adjust_component(g),
                           _adjust_component(b)))

    for x, y, col in adjusted_image:
        check_equal("(" + str(x) + ", " + str(y) + ")", col,
                    get_color(expected_image, x, y))


def test_green():
    """Returns whether or not the green filter is applied to the whole image. If
    the filter isn't applied everywhere, it indicates where it isn't.

    >>> test_green()
    Test passed
    >>> test_green()
    Test failed at:  (325, 232) (r,g,b) (1, 40, 0)
    """
    green = green_channel()
    for pixel in green:
        x, y, (r, g, b) = pixel
        if (r, g, b) != (r - r, g, b - b):
            print("Test failed at: ", (x, y), "(r,g,b)", (r, g, b))
    if (r, g, b) == (r - r, g, b - b):
        print("Test passed")

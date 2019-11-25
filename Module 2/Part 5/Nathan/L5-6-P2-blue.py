"""ECOR 1051 - Fall 2019

Group L5_6 - Milestone 1, P2 
File contains the function blue_channel and its test function.
Submitted on: 10/11/2019"""

from Cimpl import choose_file, load_image, copy, set_color, create_color,\
                  get_color, create_image, Image, show


def blue_channel(image: Image) -> Image:
    """Function takes an image and applies a blue channel filter over the image 
    without affecting the original image and returns a filtered new image.
    -Function written by Nathan Gomes - 101143780
    
    >>> original_image = load_image(choose_file()) 
    >>> blue_image = blue_channel(original_image)
    >>> show(blue_image)
    """
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel 
        blue_increased = create_color(r - r, g - g, b)  
        set_color(new_image, x, y, blue_increased)
        
    return new_image


def check_equal(description: str, outcome, expected) -> None:
    """Funtion Author: Prof. Donald L. Bailey
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
                                                                    
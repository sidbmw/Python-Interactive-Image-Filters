"""ECOR 1051 - Fall 2019

Group L5_6 - Milestone 2, P4 
Test function for the posterize function and the helper function check_equal.
Submitted on: 17/11/2019"""

from Cimpl import choose_file, load_image, copy, set_color, create_color,\
                  get_color, create_image
from L5_6_P4_posterize import posterize


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

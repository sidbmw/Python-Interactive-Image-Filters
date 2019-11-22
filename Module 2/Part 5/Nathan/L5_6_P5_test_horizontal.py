#Group L5_6 - Milestone 2, P5 - Submitted on: 22/11/2019
from Cimpl import *
from L5_6_P5_horizontal import *

def check_equal(description: str, outcome, expected) -> None:
    """ Function Author : Prof. Donald L. Bailey
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
        print(col)
    for x, y, col in horizontal_image:
        check_equal("Checking pixel @(" + str(x) + ', ' + str(y) + ')', col, 
                    get_color(expected_image, x, y))

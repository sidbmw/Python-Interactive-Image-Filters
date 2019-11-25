"""ECOR 1051 - Fall 2019

Group L5_6 - Milestone 2, P4 
Test function for the _adjust_component helper function and the helper 
function check_equal.
Submitted on: 17/11/2019"""

from Cimpl import choose_file, load_image, copy, set_color, create_color,\
                  get_color, create_image, Image, show
from L5_6_P4_posterize import _adjust_component


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
    
    
def test_adjust_component() -> None :
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
            
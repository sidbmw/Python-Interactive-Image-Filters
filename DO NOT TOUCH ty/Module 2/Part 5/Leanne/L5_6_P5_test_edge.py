"""ECOR 1051 - Fall 2019
Group L5_6 - Milestone 2, P5 
Submitted on: 22/11/2019
"""

from L5_6_P5_edge import detect_edges
from Cimpl import choose_file, create_color, create_image, get_color,\
                  set_color, load_image, Image

def check_equal(description: str, outcome, expected) -> None:
    """
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

    -Donald Bailey
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

def test_detect_edge() ->None:
    """ Returns wether the edge detection filter works and if not where it didn't.
    -Test function written by Leanne Matamoros - 10114740 
    
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
    Checking pixel @(1, 0) FAILED: expected Color(red=255, green=255, blue=255), got Color(red=0, green=0, blue=0)
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
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 10, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    
    set_color(original, 0, 1,  create_color(10, 30, 3))
    set_color(original, 1, 1,  create_color(67, 90, 1))
    set_color(original, 2, 1,  create_color(0, 2, 20))
    set_color(original, 3, 1,  create_color(189, 53, 222))
    set_color(original, 4, 1,  create_color(145, 136, 198))   
   
    expected = create_image(5, 2)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(255, 255, 255))
    set_color(expected, 4, 0,  create_color(0, 0, 0))
    
    #The last row's value stay the same do to the criterias of the edge 
    #detection filter.
    set_color(expected, 0, 1,  create_color(10, 30, 3))
    set_color(expected, 1, 1,  create_color(67, 90, 1))
    set_color(expected, 2, 1,  create_color(0, 2, 20))
    set_color(expected, 3, 1,  create_color(189, 53, 222))
    set_color(expected, 4, 1,  create_color(145, 136, 198))

    image_edge = detect_edges(original, 15) # threshold is assigned 15 for this test
    
    for x, y, col in image_edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

from Cimpl import choose_file, create_color, create_image, get_color,\
                  set_color, load_image, Image

from extreme_contrast import *

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
    -Test function written by Donald Bailey
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
    
def test_extreme() ->None:  
    '''A test function for extreme contrast.
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
    Checking pixel @(3, 0) FAILED: expected Color(red=0, green=0, blue=25), got Color(red=0, green=0, blue=255)
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------
    '''
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(0, 0, 25))
    set_color(expected, 4, 0,  create_color(255, 255, 255))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    extreme_image = extreme_contrast(original)   
    for x, y, col in extreme_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

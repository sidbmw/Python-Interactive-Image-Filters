""" ECOR 1051 Fall 2019

Function for testing the sepia filter function.
Last edited: Nov. 24, 2019
"""
from Cimpl import create_color, create_image, get_color, show, set_color
from L5_6_P4_sepia import sepia

def check_equal(pixel: str, outcome, expected) -> None:
        if type(outcome) != type(expected):

                print("{0} FAILED: expected ({1}) has type {2}, " \
                "but outcome ({3}) has type {4}".format(pixel, expected, \
                str(type(expected)).strip('<class> '), \
                outcome, str(type(outcome)).strip('<class> ')))
        elif outcome != expected:
                print("{0} FAILED: expected {1}, got {2}".format(pixel, \
                expected, outcome))
        else:
                print("{0} PASSED".format(pixel))
                
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
        original = create_image(4,2)
        
        set_color(original, 0, 0, create_color(15, 250, 8))
        set_color(original, 1, 0, create_color(8, 20, 11))
        set_color(original, 2, 0, create_color(5, 55, 15))
        set_color(original, 3, 0, create_color(32, 206, 56))
        
        set_color(original, 0, 1, create_color(93, 51, 240))
        set_color(original, 1, 1, create_color(11, 23, 41))
        set_color(original, 2, 1, create_color(54, 26, 190))
        set_color(original, 3, 1, create_color(21, 68, 49))
        
        expected = create_image(4,2)
        
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
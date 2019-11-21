""" ECOR 1051 Fall 2019

Function for testing the improved edge detection filter.
Last edited: Nov. 21, 2019
"""

from Cimpl import *
from L5_6_P5_imp_edge import *

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
                
def test_detect_edges_better():
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
        
        original = create_image(4,2)
        
        set_color(original, 0, 0, create_color(15,250,7))
        set_color(original, 1, 0, create_color(8,19,10))
        set_color(original, 2, 0, create_color(5,55,15))
        set_color(original, 3, 0, create_color(32,206,56))
        
        set_color(original, 0, 1, create_color(43,50,21))
        set_color(original, 1, 1, create_color(11,23,40))
        set_color(original, 2, 1, create_color(54,26,190))
        set_color(original, 3, 1, create_color(21,68,48))
        
        expected = create_image(4,2)
        
        set_color(expected, 0, 0, create_color(0,0,0))
        set_color(expected, 1, 0, create_color(255,255,255))
        set_color(expected, 2, 0, create_color(0,0,0))
        set_color(expected, 3, 0, create_color(0,0,0))
        
        set_color(expected, 0, 1, create_color(255,255,255))
        set_color(expected, 1, 1, create_color(0,0,0))
        set_color(expected, 2, 1, create_color(0,0,0))
        set_color(expected, 3, 1, create_color(255,255,255))    
        
        threshold = 15 #Assume threshold chosen is 15. 
        
        edges_image =  detect_edges_better(original, threshold)  
    
        for x, y, color in edges_image:
        
                check_equal('(' + str(x) + ',' + str(y) + ')', color,
                            get_color(expected, x, y))
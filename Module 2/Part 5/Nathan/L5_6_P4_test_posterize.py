"""ECOR 1051 - Fall 2019
Group L5_6 - Milestone 2, P4 
Submitted on: 17/11/2019"""

from Cimpl import *
import Cimpl
from L5_6_P4_posterize import *

def test_posterize() -> None:
    """Function is called without any arguments, calls the posterize filter 
    within the function body on a preset image and returns a string stating 
    if the filter passes or fails.
    -Function written by Nathan Gomes, 101143780
    
    >>> test_posterize()
    FILTER PASSED
    """
    file = load_image("riveter.jpg")
    new_image = posterize(file)
    
    test_1 = ""
    test_2 = ""
   
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        if (r == 31) or (r == 95) or (r == 159) or (r == 223) or (g == 31) \
           or (g == 95) or (g == 159) or (g == 223) or (b == 31) or (b == 95) \
           or (b == 159) or (b == 223):
            test_1 = "Pass"
        else:
            test_2 = "Fail"
           
    if  test_2 == "Fail":
        print("FILTER FAILED")
    elif test_1 == "Pass":
        print("FILTER PASSED")  

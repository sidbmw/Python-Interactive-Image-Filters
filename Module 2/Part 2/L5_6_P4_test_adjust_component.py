from Cimpl import *
import Cimpl
from L5_6_P4_posterize import _adjust_component

def test_adjust_component() ->None :
    """Function tests the helper function "_adjust_component."
    -Written by Nathan Gomes, 101143780
    
    >>>test_adjust_component
    Helper function passes.
    """
    
    L = [28, 120, 169, 207]
    adjust_pass = 0
    adjust_fail = 0
    
    for i in L:
        if L[i] == 31 or L[i] == 95 or L[i] == 159 or L[i] == 223:
            adjust_pass += 1
        else:
            adjust_fail += 1
            
    if adjust_fail > 0:
        print("Helper function fails.")
    
    else:
        print("Helper function passes.")
            
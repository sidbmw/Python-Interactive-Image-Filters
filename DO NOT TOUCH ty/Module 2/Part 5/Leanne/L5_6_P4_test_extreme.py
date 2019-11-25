from Cimpl import choose_file, create_color, create_image, get_color,\
                  set_color, load_image, Image

from L5_6_P4_extreme import extreme_contrast
from test_grayscale import check_equal
    
def test_extreme() ->None:  
    """A test function for extreme contrast.
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
    Checking pixel @(3, 0) FAILED: expected Color(red=0, green=0, blue=255), got Color(red=0, green=0, blue=25)
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 255, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(0, 0, 255))
    set_color(expected, 4, 0,  create_color(255, 255, 255))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    extreme_image = extreme_contrast(original)   
    for x, y, col in extreme_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
#forgot to add it when sent
test_extreme()
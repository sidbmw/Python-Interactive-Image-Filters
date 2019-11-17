from Cimpl import *
from extreme_contrast import *

def test_extreme(original_image: Image):
    """Returns the place where the extreme filter was not applied and the number
    of times it happenned for one image. If the filter was applied for everywhere
    on the image inputed returns a statement saying the function worked.
    -Test function written by Leanne Matamoros - 101147405
    
    >>> test_extreme(original_image)
    Function worked.
    >>> test_extreme(original_image)
    Function didn't work at 15 different pixels.
    """     
    new_extreme = extreme_contrast(original_image)
    failed = 0
        
    for pixel in new_extreme:
        x, y, (r, g, b) = pixel
        if r == 0 or r == 255:
            failed += 0
        elif 0< r <=127:
            print("Test failed at: ", (x, y), (r, g, b),"expected 0 but got", r,".")
            failed += 1
        elif 127< r <=255:
            print("Test failed at: ", (x, y), (r, g, b),"expected 255 but got", r,".")
            failed += 1 
            
        if g == 0 or g == 255:
            failed += 0
        elif 0< g <=127:
            print("Test failed at: ", (x, y), (r, g, b),"expected 0 but got", g,".")
            failed += 1
        elif 127< g <255:
            print("Test failed at: ", (x, y), (r, g, b),"expected 255 but got", g,".")
            failed += 1
            
        if b==0 or b ==255:
            failed += 0
        elif 0< b <=127:
            print("Test failed at: ", (x, y), (r, g, b),"expected 0 but got", b,".")
            failed += 1
        elif 127 < g <255:
            print("Test failed at: ", (x, y), (r, g, b),"expected 255 but got", b,".") 
            failed += 1
            
    if failed != 0:
        print("Function didn't work for", failed, "different pixels.")
    else:
        print("Function worked.")                                

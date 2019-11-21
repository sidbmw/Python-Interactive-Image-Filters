from Cimpl import *
from L5_6_P4_sepia import *

new_image = load_image(choose_file())
sepia_image = sepia(new_image)

def test_sepia(sepia_image: Image) -> str:
    """The function takes the image which has a sepia filter and returns a
    string that states whether the function sepia was successful or not.
    - Function written by Malak Abdou - 101139692
    
    >>> test_sepia(sepia_image)
    Test passed; filter works properly.
    """
    grayscale_image = grayscale(new_image)
    for pixel in sepia_image:
        x, y, (r, g, b) = pixel
        (red,green,blue) = get_color(grayscale_image, x, y)
        fail = 0
        
        if green<63:
            if (b != blue * 0.9) or (r != red * 1.1):
                fail += 1
                
        elif 63 <= green <= 191:
            if (b == blue * 0.85) and (r == red * 1.15):
                fail += 1
                
        elif green>191:
            if (b == blue * 0.93) and (r == red * 1.08):
                fail += 1
                
    if fail > 0:
        print('Test failed; filter does not work.')
    elif fail == 0:
        print('Test passed; filter works properly.')
from simple_Cimpl_filters import *
from Cimpl import *

file = choose_file()
original_image = load_image(file)

def sepia_channel(original_image: Image):
    """Return an image a black and white image which as been tinted yellow.\
    -Function written by Leanne Matamoros - 101147405
    
    >>> sepia_channel() 
    #function will return a sepia tinted image
    
    """
    new_image = copy(original_image)
    sepia_filter = grayscale(new_image)
    
    for pixel in sepia_filter:
        x, y, (r, g, b) = pixel
        if r < 63:
            sepia_tinted = create_color((r * 1.1), g, (b * 0.9))
            set_color (sepia_filter, x, y, sepia_tinted)
            
        if (63 <= r <= 191):
            sepia_tinted = create_color((r * 1.15), g, (b * 0.85))
            set_color (sepia_filter, x, y, sepia_tinted)
            
        if (r > 191):
            sepia_tinted = create_color((r * 1.08), g, (b * 0.93))
            set_color (sepia_filter, x, y, sepia_tinted)
        
    return sepia_filter
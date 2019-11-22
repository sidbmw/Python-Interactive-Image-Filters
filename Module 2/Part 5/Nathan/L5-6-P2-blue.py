"""ECOR 1051 - Fall 2019
Group L5_6 - Milestone 1, P2 
Submitted on: 10/11/2019"""

from Cimpl import *
import Cimpl

file = choose_file()
original_image = load_image(file)

def blue_channel(image: Cimpl.Image) ->Cimpl.Image:
    """Function takes an image and applies a blue channel filter over the image 
    without affecting the original image and returns a filtered new image.
    -Function written by Nathan Gomes - 101143780
    
    >>>blue_channel(original_image)
    <Cimpl.Image object at 0x000001E675499108>
    """
    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel 
        blue_increased = create_color(r-r, g-g ,b)  
        set_color(new_image, x, y, blue_increased)
        
    return new_image

def blue_channel_test(image: Cimpl.Image) ->str:
    """Function accepts an image and calls blue_channel function on the image
    and checks whether the filter has been properly applied for each pixel, 
    printing the result and showing the picture.
    -Function written by Nathan Gomes - 101143780
    
    >>>blue_channel_test(original_image)
    Test passed. blue_channel filter works as expected.
    """
    test = blue_channel(image)
    red_or_green = 0
    for pixel in test:
        x, y, (r, g, b) = pixel
        if r > 0 or g > 0:
            red_or_green += 1
    if red_or_green > 0:
        show(test)
        print("Test failed. Filter does not work properly.")
    else:
        show(test)
        print("Test passed. Channel filter works as expected.")
        
blue_image = blue_channel(original_image)

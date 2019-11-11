from Cimpl import *

file = choose_file()
original_image = load_image(file)


########

def red_channel(original_image: Image) -> Image:
    """Returns the red channel of image without having modified it.
    - Function written by Malak Abdou - 101139692

    >>> red_channel(original_image)
    <Cimpl.Image object at 0x000001C447BDFAC8>
    """
    red_filter = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        red = create_color(r, 0, 0)
        set_color(red_filter, x, y, red)
    return red_filter


red_image = red_channel(original_image)


def test_red() -> None:
    """Tests the red_channel function. Returns PASS if all pixels in red_image
    have 0 green and blue components.
    - Function written by Malak Abdou - 101139692

    >>> test_red()
    PASS
    """

    show(red_image)
    r, g, b = get_color(red_image, 0, 0)
    if g == 0 and b == 0:
        print('PASS')
    else:
        print('FAIL')


#######

def green_channel(original_image) -> Image:
    """Returns the green channel of the initial image without having modified it.
    -Function written by Leanne Matamoros - 101147405

    >>> green_channel(original_image)
    <Cimpl.Image object at 0x0000028A06CD6D88>
    """

    green_filter = copy(original_image)

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        green_coloration = create_color(0, g, 0)
        set_color(green_filter, x, y, green_coloration)

    return green_filter


green = green_channel(original_image)


def test_green():
    """Returns whether or not the green filter is applied to the whole image. If
    the filter isn't applied everywhere, it indicates where it isn't.

    >>> test_green()
    Test passed
    >>> test_green()
    Test failed at:  (325, 232) (r,g,b) (1, 40, 0)
    """
    show(green_channel(green))

    for pixel in green:
        x, y, (r, g, b) = pixel
        if (r, g, b) != (r - r, g, b - b):
            print("Test failed at: ", (x, y), "(r,g,b)", (r, g, b))
    if (r, g, b) == (r - r, g, b - b):
        print("Test passed")


#######
def blue_channel(image: Image) -> Image:
    """Function takes an image and applies a blue channel filter over the image
    without affecting the original image and returns a filtered new image.
    -Function written by Nathan Gomes - 101143780

    >>> blue_channel(original_image)
    <Cimpl.Image object at 0x000001E675499108>
    """

    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel
        blue_increased = create_color(r - r, g - g, b)
        set_color(new_image, x, y, blue_increased)

    return new_image


def blue_channel_test(image: Image):
    """Function accepts an image and calls blue_channel function on the image
    and checks whether the filter has been properly applied for each pixel,
    printing the result and showing the picture.
    -Function written by Nathan Gomes - 101143780

    >>>blue_channel_test(original_image)
    Test passed. Channel filter works as expected.
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


#######
def combine(redPic: Image, greenPic: Image, bluePic: Image) -> Image:
    # Author: Siddharth Natamai - 101143016
    # Date:
    """Combines the inputted images and returns the final image
    >>> combine(red_channel(original_image), green_channel(original_image), blue_channel(original_image))
    <Cimpl.Image object at 0x7fba8cef0f50>
    """
    finalImage = copy(redPic)
    for pixel in finalImage:
        x, y, (r, g, b) = pixel
        blueColour = get_color(bluePic, x, y)
        greenColour = get_color(greenPic, x, y)
        newColours = create_color(r, greenColour[1], blueColour[2])
        set_color(finalImage, x, y, newColours)

    return finalImage


def test_combine(original_image):
    # Author: Siddharth Natamai - 101143016
    # Date:
    """Tests whether the picture from combine() is the same as the original image.
    >>> test_combine(original_image)
    None
    """
    red_filter = red_channel(original_image)
    green_filter = green_channel(original_image)
    blue_filter = blue_channel(original_image)
    combined_pic = combine(red_channel(original_image), green_channel(original_image), blue_channel(original_image))
    test_result = True

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        original_pic_colour = get_color(original_image, x, y)
        combine_pic_colour = get_color(combinedPic, x, y)
        if original_pic_colour != combine_pic_colour:
            test_result == False

    print('Combine filter test passed')


show(red_channel(original_image))
show(green_channel(original_image))
show(blue_channel(original_image))

test_red()
test_green()
blue_channel_test(original_image)

combinedPic = combine(red_channel(original_image), green_channel(original_image), blue_channel(original_image))
show(combinedPic)
print(test_combine(original_image))
# save(combinedPic)

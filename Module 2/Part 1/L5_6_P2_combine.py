from Cimpl import *

image_1 = load_image(choose_file())
image_2 = load_image(choose_file())
image_3 = load_image(choose_file())

original_image = load_image(choose_file())


def combine(redPic: Image, greenPic: Image, bluePic: Image) -> Image:
    # Author: Siddharth Natamai - 101143016
    """Combines the inputted images and returns the final image
    >>> combine(image_1, image_2, image_3)
    <Cimpl.Image object at 0x7fab575d3ad0>
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
    """Tests whether the picture from combine() is the same as the original image.
    >>> test_combine(original_image)
    None
    """
    red_filter = red_channel(original_image)
    green_filter = green_channel(original_image)
    blue_filter = blue_channel(original_image)
    combined_pic = combine(red_channel(original_image), green_channel(original_image), blue_channel(original_image))
    red_filter = image_1
    green_filter = image_2
    blue_filter = image_3
    combined_pic = combine(image_1, image_2, image_3)
    test_result = True

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        original_pic_colour = get_color(original_image, x, y)
        combine_pic_colour = get_color(combinedPic, x, y)
        if original_pic_colour != combine_pic_colour:
            test_result == False

    print('Combine filter test passed')


combinedPic = combine(image_1, image_2, image_3)
show(combinedPic)
test_combine(original_image)

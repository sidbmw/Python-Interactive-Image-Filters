from Cimpl import *
import math

file = choose_file()

image = load_image(file)


def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        # show (new_image)
    return new_image


def Sepia_channel():
    """
    The funcion returns the selected image in a sepia filter, however it does not alter the original image.

    Ahmed Shakir - 101143951

    """
    sepia_picture = grayscale(image)

    for x, y, (r, g, b) in sepia_picture:
        if g < 63:
            b *= 0.9
            r *= 1.1
            b = round(b)
            r = round(r)
        elif 63 <= g <= 191:
            r *= 1.15
            b *= 0.85
            r = round(r)
            b = round(b)
        elif g > 191:
            b *= 0.93
            r *= 1.08
            b = round(b)
            r = round(r)
        sepia = create_color(r, g, b)
        set_color(sepia_picture, x, y, sepia)

    show(sepia_picture)
    return sepia_picture


def test_filter_grayscale(image):
    gray_picture = grayscale(image)

    for x, y, (r, g, b) in gray_picture:

        r, g, b = get_color(gray_picture, x, y)
        red, green, blue = get_color(image, x, y)
        brightness = (red + green + blue) // 3
        if brightness == r and brightness == g and brightness == b:
            continue
        else:
            return False
    return True


def test_filter_sepia(image):
    filtered_picture = Sepia_channel()
    graypic = grayscale(image)

    graytest = test_filter_grayscale(image)

    if graytest == False:
        return False

    for x, y, (r, g, b) in filtered_picture:

        r, g, b = get_color(filtered_picture, x, y)
        red, green, blue = get_color(graypic, x, y)
        if red < 63 and r == round(red * 1.1):
            print("before else 1")
            continue
        elif (red >= 63 and red <= 191) and r == round(red * 1.15):
            print("before else 2")
            continue
        elif red > 191 and r == round(red * 1.08):
            continue
            print("before else 3")
        # else:
        #     print("I failed here")
        #     issue = True
        #
        # print("here now")
        elif blue < 63 and b == round(blue * 0.9):
            print("I can get here too!")
            continue
        elif (63 <= blue <= 191) and b == round(blue * 0.85):
            continue
        elif blue > 191 and b == round(blue * 0.93):
            continue
        else:
            return False
    return True


print(test_filter_sepia(image))

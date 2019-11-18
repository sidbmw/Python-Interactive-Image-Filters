from Cimpl import *
import Cimpl

file = choose_file()
original_image = load_image(file)


def three_tone(image: Image, colour_1: str, colour_2: str, colour_3: str) -> Image:
    """Function takes an image file and three colours as strings from the given
    list:
    black
    white
    red
    lime
    blue
    yellow
    cyan
    magenta
    gray
    Function returns an image in three tones (as per the colours given in the
    second, third and fourth function parameters) decided by an individual
    pixel's brightness.
    -Function written by Nathan Gomes, 101143780

    >>> three_tone(image_1, "blue", "gray", "white")
    #Gives the image in only blue, gray and white tones.
    >>> three_tone(image_1, "yellow", "cyan", "purple")
    #Error because colour passed ("purple") is not in the given list
    """

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)

    L = [("black", black), ("white", white), ("red", red), ("lime", lime),
         ("blue", blue), ("yellow", yellow), ("cyan", cyan),
         ("magenta", magenta), ("gray", gray)]

    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        average = (r + g + b) / 3
        if (average >= 0) and (average < 85):
            for i in range(len(L)):
                if colour_1 == L[i][0]:
                    set_color(new_image, x, y, L[i][1])
        elif (average > 84) and (average < 171):
            for i in range(len(L)):
                if colour_2 == L[i][0]:
                    set_color(new_image, x, y, L[i][1])
        elif (average > 170) and (average < 256):
            for i in range(len(L)):
                if colour_3 == L[i][0]:
                    set_color(new_image, x, y, L[i][1])

    return new_image


def test_three_tone():
    filtered_image = three_tone(original_image, "black", "white", "lime")
    test_state = False

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] + color_original[2]) // 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)
        colour_3 = create_color(0, 255, 0)

        test_state = bool((color_average <= 84 and color_filtered == colour_1) or ((84 < color_average <= 170) and color_filtered == colour_2) or (
                color_average >= 171 and color_filtered == colour_3))

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


# show(three_t(original_image, "black", "white", "lime"))

print(test_three_tone())

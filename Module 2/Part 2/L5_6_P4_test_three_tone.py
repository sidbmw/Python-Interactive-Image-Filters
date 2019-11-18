from Cimpl import *
from L5_6_P4_three_tone import three_tone

file = choose_file()
original_image = load_image(file)


def test_three_tone():
    """ Author: Siddharth Natamai - 101143016
            Date: Nov 17, 2019

        Returns a bool depending on whether the the function is working properly or not
        >>> test_three_tone()
        True
        >>> test_three_tone()
        False
        """
    filtered_image = three_tone(original_image, "black", "white", "lime")
    test_state = True

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

# print(test_three_tone())

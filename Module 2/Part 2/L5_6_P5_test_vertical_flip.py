from Cimpl import *
from L8_6_P5_vertical import *

file = choose_file()
original_image = load_image(file)


def flip_vertical_test(original_image: Image, test_image: Image) -> None:
    test_case = True
    for x in range(0, get_width(test_image)):
        for y in range(0, get_height(test_image)):
            r, g, b = get_color(test_image, x, y)
            color_original= get_color(test_image, x, y)
            print(r, g, b)
            r2, g2, b2 = get_color(original_image, x, y)
            if r == r2 and g == g2 and b == b2:
                test_case = True
            else:
                test_case = False


flip_vertical_test(copy, test_image)

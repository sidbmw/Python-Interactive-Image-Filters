from Cimpl import *
from L5_6_P4_three_tone import three_tone as three_t

file = choose_file()
original_image = load_image(file)


# two_tone(original_image, "black", "white")


def test_three_tone():
    filtered_image = three_t(original_image, "black", "white", "lime")
    test_state = True

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] + color_original[2]) / 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)
        colour_3 = create_color(0, 255, 0)

        if (color_average <= 84 and color_filtered == colour_1) or ((84 < color_average < 171) and color_filtered == colour_2) or (
                color_average > 170 and color_filtered == colour_3):
            test_state = True
        else:
            test_state = False

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


# show(three_t(original_image, "black", "white", "lime"))

test_three_tone()

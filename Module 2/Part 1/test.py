from Cimpl import *

file_one = choose_file()
file_two = choose_file()
file_three = choose_file()


def combine_colours(red_image, green_image, blue_image):
    combined_image = copy(red_image)
    for pixel in combined_image:
        x, y, (r, g, b) = pixel
        g = get_color(green_image, x, y)
        b = get_color(blue_image, x, y)
        combined_colours = create_color(r, g, b)
        set_color(combined_image, x, y, combined_colours)
    return combined_image


combine_colours(file_one, file_two, file_three)

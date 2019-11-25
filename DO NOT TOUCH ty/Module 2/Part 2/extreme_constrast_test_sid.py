from Cimpl import *

file = choose_file()
original_image = load_image(file)


def extreme_contrast(original_image: Image) -> Image:
    red_filter = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        if r < 127:
            r = 0
        else:
            r = 255
        if g < 127:
            g = 0
        else:
            g = 255
        if b < 127:
            b = 0
        else:
            b = 255

        # red = create_color(r, 0, 0)
        newColours = create_color(r, g, b)
        # set_color(finalImage, x, y, newColours)
        set_color(red_filter, x, y, newColours)
    return red_filter


show(extreme_contrast(original_image))
# save(extreme_contrast(original_image))

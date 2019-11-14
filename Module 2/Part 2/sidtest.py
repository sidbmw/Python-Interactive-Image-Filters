from Cimpl import *

file = choose_file()
original_image = load_image(file)


def red_channel(original_image: Image) -> Image:
    red_filter = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        if r >= 128:
            r += 15
        if r < 127:
            r -= 15

        if g >= 127:
            g += 15
        if g < 127:
            g -= 15

        if b >= 127:
            b += 15
        if b < 127:
            b -= 15

        # red = create_color(r, 0, 0)
        newColours = create_color(r, g, b)
        # set_color(finalImage, x, y, newColours)
        set_color(red_filter, x, y, newColours)
    return red_filter


show(red_channel(original_image))

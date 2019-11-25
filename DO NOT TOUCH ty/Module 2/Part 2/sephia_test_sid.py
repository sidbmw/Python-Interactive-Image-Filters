from Cimpl import *

file = choose_file()
original_image = load_image(file)


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
    return new_image


def sepia(image):
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel
        if r < 63:
            r = r * 1.1
            b = b * 0.9
        elif r <= 191:
            r = r * 1.15
            b = b * 0.85
        else:
            r = r * 1.08
            b = b * 0.93

        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour)

    return new_image


show(sepia(grayscale(original_image)))
# save(sepia(grayscale(original_image)))



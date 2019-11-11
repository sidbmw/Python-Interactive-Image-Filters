from Cimpl import *


def green_channel() -> Image:
    """Returns the green chanel of the initial image without having modified it.
    -Function written by Leanne Matamoros - 101147405

    >>> green_channel(original_image)
    <Cimpl.Image object at 0x0000028A06CD6D88>
    """
    file = choose_file()
    original_image = load_image(file)
    green_filter = copy(original_image)

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        green_coloration = create_color(0, g, 0)
        set_color(green_filter, x, y, green_coloration)

    return green_filter


def test_green():
    """Returns whether or not the green filter is applied to the whole image. If
    the filter isn't applied everywhere, it indicates where it isn't.

    >>> test_green()
    Test passed
    >>> test_green()
    Test failed at:  (325, 232) (r,g,b) (1, 40, 0)
    """
    green = green_channel()
    for pixel in green:
        x, y, (r, g, b) = pixel
        if (r, g, b) != (r - r, g, b - b):
            print("Test failed at: ", (x, y), "(r,g,b)", (r, g, b))
    if (r, g, b) == (r - r, g, b - b):
        print("Test passed")
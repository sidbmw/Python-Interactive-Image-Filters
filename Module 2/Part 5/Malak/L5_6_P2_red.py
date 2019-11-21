from Cimpl import *

file = choose_file()
original_image = load_image(file)


def red_channel(original_image: Image) -> Image:
    """Returns the red channel of image without having modified it.
    - Function written by Malak Abdou - 101139692
    
    >>> red_channel(original_image)
    <Cimpl.Image object at 0x000001C447BDFAC8>
    """
    red_filter = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        red = create_color(r, 0, 0)
        set_color(red_filter, x, y, red)
    return red_filter


red_image = red_channel(original_image)


def test_red() -> None:
    """Tests the red_channel function. Returns PASS if all pixels in red_image
    have 0 green and blue components.
    - Function written by Malak Abdou - 101139692

    >>> test_red()
    PASS
    """

    show(red_image)
    r, g, b = get_color(red_image, 0, 0)
    if g == 0 and b == 0:
        print('PASS')
    else:
        print('FAIL')




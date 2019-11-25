from Cimpl import *

file = choose_file()
original_image = load_image(file)


def extreme_contrast(original_image: Image) -> Image:
    """Returns the 'extreme contrast' version of an image without having modified it.
    - Function written by Malak Abdou - 101139692
    
    >>> extreme_contrast(original_image)
    <Cimpl.Image object at 0x00000212B29BD948>
    """
    extreme_copy = copy(original_image)
    r, g, b = get_color(extreme_copy, 0, 0)
    for pixel in extreme_copy:
        x, y, (r, g, b) = pixel
        if r <= 127:
            r = 0
        else:
            r = 255
        if g <= 127:
            g = 0
        else:
            g = 255
        if b <= 127:
            b = 0
        else:
            b = 255
        extreme_color = create_color(r, g, b)
        set_color(extreme_copy, x, y, extreme_color)
    return extreme_copy


show(extreme_contrast(original_image))

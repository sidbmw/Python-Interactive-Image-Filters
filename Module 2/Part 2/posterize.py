from Cimpl import *

file = choose_file()
original_image = load_image(file)


def _adjust_component(original_val: int) -> int:
    """Determines where each pixel lies in the 4 quadrants (0 to 63, 64 to 127, 128 to 191, and 192 to 255)
    and sets the new pixel values to the midpoint of that specific quadrant.
    >>> _adjust_component(50)
    31
    >>> _adjust_component(90)
    95
    >>> _adjust_component(155)
    159
    """


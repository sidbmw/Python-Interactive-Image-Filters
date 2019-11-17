from Cimpl import *
import Cimpl

file_1 = choose_file()
original_image = load_image(file_1)

def posterize(original_image: original_image) -> original_image:
    new_image = copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)

        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour)
        # print(r, g, b)

    return new_image


def _adjust_component(original_val: int) -> int:
    # """Determines where each pixel lies in the 4 quadrants (0 to 63, 64 to 127, 128 to 191, and 192 to 255)
    # and sets the new pixel values to the midpoint of that specific quadrant.
    # >>> _adjust_component(50)
    # 31
    # >>> _adjust_component(90)
    # 95
    # >>> _adjust_component(155)
    # 159
    # """

    if original_val <= 63:
        new_val = 31
    elif original_val <= 127:
        new_val = 95
    elif original_val <= 191:
        new_val = 159
    elif original_val <= 255:
        new_val = 223
    return new_val

# print(_adjust_component(192))

# save(posterize(original_image))

def posterize_test() -> None:
    """
    
    """
    file = load_image("riveter.jpg")
    new_image = posterize(file)
    show(new_image)
    
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        if ((r != 31) or (r != 95) or (r != 159) or (r != 223)) and ((g != 31) or (g != 95) or (g != 159) or (g != 223)) and ((b != 31) or (b != 95) or (b != 159) or (b != 223)):
            print("FILTER FAILED")
        
        else:
            print("FILTER PASSED")
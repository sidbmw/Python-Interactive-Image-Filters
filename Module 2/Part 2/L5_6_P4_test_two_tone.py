from Cimpl import *
from two_tone import *

file = choose_file()
original_image = load_image(file)


def testThreeTone(test_image):

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)

    for pixel in test_image:
        x, y, (r, g, b) = pixel
        


print(testThreeTone(original_image))

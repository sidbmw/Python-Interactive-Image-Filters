from Cimpl import *
from two_tone import *

file = choose_file()
original_image = load_image(file)


def test_two_tone(img):
    img = create_image(3, 1)  # creates image
    set_color(img, 0, 0, create_color(0, 0, 0))
    set_color(img, 1, 0, create_color(128, 128, 128))
    set_color(img, 2, 0, create_color(255, 255, 255))
    test_img = copy(img)

    for col in colours:
        print('\n testing', col)
        test_img = threeTone(test_img, col, col, col)
        for x, y, (r, g, b) in test_img:
            if (r, g, b) == col:
                print('pass ', end='')
            else:
                print('fails at', col, r, g, b)

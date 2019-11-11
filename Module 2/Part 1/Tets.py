from Cimpl import *

# Assumption: There is a image stored in the same folder as this script
#  with the given name
FILENAME = choose_file()

original_image = load_image(FILENAME)
for pixel in original_image:
    x, y, (r, g, b) = pixel
    print(x, y, ":", r, g, b)

new_image = copy(original_image)
for pixel in original_image:
    x, y, (r, g, b) = pixel
    new_colour = create_color(b, g, b)  # Mix up the colours ad hoc
    set_color(new_image, x, y, new_colour)

show(original_image)
show(new_image)



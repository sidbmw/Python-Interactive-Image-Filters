"""ECOR 1051 - Milestone 3
L5-6
Date of submission: Dec. 01 2019
Authors: Siddharth Natamai, Malak Abdou, Nathan Gomes, Leanne Matamoros
"""

from Cimpl import load_image, choose_file, save_as, show
from L5_6_image_filters import posterize, flip_horizontal, sepia, \
     detect_edges_better, extreme_contrast, detect_edges, three_tone, \
     flip_vertical
from L5_6_image_filters import two_tone as tt

inputted_task = "2"
image = None
while inputted_task != "Q":
    inputted_task = input(
        "L)oad image\tS)ave-as\n2)-tone\t3)-tone\tX)treme contrast\tT)int "
        "sepia\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical "
        "flip\tH)orizontal Flip\nQ)uit\n\n: ")
    inputted_task = inputted_task.upper()
    if inputted_task == "L":
        image = load_image(choose_file())
        show(image)
    elif inputted_task == "2":
        if not (image is None):
            image = tt(image, "yellow", "cyan")
            show(image)
        else:
            print("No image loaded.")
    elif inputted_task == "3":
        if not (image is None):
            image = three_tone(image, "yellow", "magenta", "cyan")
            show(image)
        else:
            print("No image loaded.")
    elif inputted_task == "X":
        if not (image is None):
            image = extreme_contrast(image)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "T":
        if not (image is None):
            image = sepia(image)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "P":
        if not (image is None):
            image = posterize(image)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "E":
        if not (image is None):
            threshold = float(input("Input a threshold value: "))
            image = detect_edges(image, threshold)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "I":
        if not (image is None):
            threshold = float(input("Input a threshold value: "))
            image = detect_edges_better(image, threshold)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "V":
        if not (image is None):
            image = flip_vertical(image)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "H":
        if not (image is None):
            image = flip_horizontal(image)
            show(image)
        else:
            print("No image loaded")
    elif inputted_task == "S":
        if not (image is None):
            filename = input(
                "Input the filename with file extension "
                "(e.g. new_image.jpg): ")
            print("test")
            show(image)
            save_as(image, filename)
        else:
            print("No image loaded")
    elif inputted_task == "Q":
        pass
    else:
        print("No such command")
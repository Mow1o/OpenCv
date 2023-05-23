import cv2 as cv
import numpy as np

from read import load_images_from_folder

# 1. Draw a Rectangle
def draw_rectangle(img, start, end, color, thickness):
    return cv.rectangle(img, start, end, color, thickness)


# 2. Draw a Circle
def draw_circle(img, center, radius, color, thickness):
    return cv.circle(img, center, radius, color, thickness)


# 3. Draw a Line
def draw_line(img, start, end, color, thickness):
    return cv.line(img, start, end, color, thickness)

# 4. Write text
def write_text(img, text, position, font, scale, color, thickness):
    return cv.putText(img, text, position, font, scale, color, thickness)





import cv2 as cv
import numpy as np
import os
from read import load_images_from_folder

folder = "../photos/"


# 1. Turn to grey
def turn_to_grey(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 2. Blur
def blur(img):
    return cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)


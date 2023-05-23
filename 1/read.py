import cv2 as cv
import numpy as np
import os
from rescale import rescaleFrame

# Path: 1\read.py
folder = "../photos/"

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images



resized_image = rescaleFrame(load_images_from_folder(folder)[0], 0.5)
cv.imshow('Image', resized_image)
cv.waitKey(0)
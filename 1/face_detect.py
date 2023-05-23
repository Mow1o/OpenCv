import cv2 as cv


from read import *
from basic import *

folder = "../photos/"


img = load_images_from_folder(folder)[3]
#img = turn_to_grey(img)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=12)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('show', img)
cv.waitKey(0)
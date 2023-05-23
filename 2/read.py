import cv2 as cv
import numpy as np
import os

from rescale import rescaleFrame

# Path: 1\read.py
folder = "../videos/"

def load_videos_from_folder(folder):
    videos = []
    for filename in os.listdir(folder):
        video = cv.VideoCapture(os.path.join(folder,filename))
        if video is not None:
            videos.append(video)
    return videos


#Reading Videos
def read_video(video):
    while True:
        isTrue, frame = video.read()
        #cv.imshow('Video', frame)
        cv.imshow('Video', rescaleFrame(frame, 0.3))

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    video.release()
    cv.destroyAllWindows()

#
capture = load_videos_from_folder(folder)[0]
read_video(capture)




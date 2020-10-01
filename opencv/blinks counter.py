#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:39:34 2020

@author: alberttenigin
"""

from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2

def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	C = dist.euclidean(eye[0], eye[3])

	ear = (A + B) / (2.0 * C)

	return ear
 
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=False, 
    default="/home/alberttenigin/projects/cv/shape_predictor_68_face_landmarks.dat",
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default='/home/alberttenigin/projects/cv/opencv/blinks_eyeglasses.mp4',
	help="path to input video file")
args = vars(ap.parse_args())
 

EYE_AR_THRESHOLD = 0.3
EYE_AR_CONSEC_FRAMES = 2

COUNTER = 0
TOTAL = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vs = FileVideoStream(args['video']).start()
#fileStream = True
vs = VideoStream(src=2).start()
#vs = VideoStream(usePiCamera=True).start()
fileStream = False
time.sleep(1.0)

while True:
    if fileStream and not vs.more():
        break

    frame = vs.read()
    
    #frame = imutils.rotate(frame, -90)
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESHOLD:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1

            COUNTER = 0

        cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 20),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
		#cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
		#	cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
 
    cv2.imshow("Blinks detection", frame)
 
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
vs.stop()
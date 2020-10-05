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
import dlib
import cv2
import threading
import time
     
def printit(num):
  print('The number of blinks: ', num)

def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	C = dist.euclidean(eye[0], eye[3])

	ear = (A + B) / (2.0 * C)

	return ear

# classifier_body = cv2.CascadeClassifier('/home/alberttenigin/projects/cv/model_data/haarcascade_upperbody.xml')
# classifier_face = cv2.CascadeClassifier('/home/alberttenigin/projects/cv/model_data/haarcascade_frontalface_alt.xml')

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=False, 
    default="/home/alberttenigin/projects/cv/shape_predictor_68_face_landmarks.dat",
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default='/home/alberttenigin/projects/cv/opencv/blinks_eyeglasses.mp4',
	help="path to input video file")
args = vars(ap.parse_args())
 
#LAST_BLINK = time.time()
LAST_TIME_PRESENT = 0
TIME_ABSCENT = 0
LAST_TIME_ABSCENT = 0
TIMEST = time.time()

EYE_AR_THRESHOLD = 0.2
EYE_AR_CONSEC_FRAMES = 2
SLEEPING_CONSEC_FRAMES = 125

COUNTER = 0
COUNTER_OPEN = 0
TOTAL = 0
TOTALS = []
LMB = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

#vs = FileVideoStream(args['video'])
#fileStream = True
vs = VideoStream(src=3).start()
#vs = VideoStream(usePiCamera=True)
#vs.start()
fileStream = False
#time.sleep(1.0)
#threading.Timer(1.0, printit, TOTAL).start()

while True:
    if fileStream and not vs.more():
        break

    frame = vs.read()
    
    #frame = imutils.rotate(frame, -90)
   # frame = imutils.resize(frame, width=900)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # persons_detected = classifier_body.detectMultiScale(gray, 1.3, 5)
    # faces_detected = classifier_face.detectMultiScale(gray, 1.3, 5)

    rects = detector(gray, 0)
    rects_count = 0
    
    # try:
    #     man_rects_count = persons_detected.shape[0]
    # except TypeError:
    #     man_rects_count = 0
    # except AttributeError:
    #     man_rects_count = 0
    # else:
    #     man_rects_count = 0
        
    for rect in rects:
        TIMEST += TIME_ABSCENT
        LAST_TIME_PRESENT = time.time()
        TIME_ABSCENT = 0
        rects_count += 1
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

        if ear < EYE_AR_THRESHOLD:# and time.time() > LAST_BLINK + 0.5:
            COUNTER_OPEN = 0
            COUNTER += 1
            #LAST_BLINK = time.time()
            if COUNTER >= SLEEPING_CONSEC_FRAMES:
                   cv2.putText(frame, "OPERATOR IS SLEEPING", (200, 200),
                               cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 255), 2)
        else:
            COUNTER_OPEN += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES and COUNTER_OPEN > 2:                
                TOTAL += 1
                COUNTER = 0  
        
        if time.time() > TIMEST + 60:
            TIMEST = time.time()
            LMB = TOTAL
            print('For the last minute there were made ', TOTAL, ' blinks, time: ', TIMEST)
            TOTALS.append(TOTAL)
            cv2.putText(frame, "Last minute blinks: {}".format(TOTAL), (300, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
            TOTAL = 0
        cv2.putText(frame, "Operator is working", (10, 30),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 60),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
        cv2.putText(frame, "Last minute blinks: {}".format(LMB), (300, 30),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
        
        if len(TOTALS) > 0:
            cv2.putText(frame, "Avg minute blinks: {}".format(sum(TOTALS)/len(TOTALS)), (300, 60),  
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
            
    if rects_count == 0:
        TIME_ABSCENT += time.time() - LAST_TIME_ABSCENT
        LAST_TIME_ABSCENT = time.time()
        cv2.putText(frame, "Operator is distracted!", (10, 30),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
#     if len(persons_detected) == 0 and len(faces_detected) == 0:
#         cv2.putText(frame, "Operator is abscent!", (10, 30),
# 			cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
#     else:
#         cv2.putText(frame, "Operator is present!", (10, 30),
# 			cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
    cv2.putText(frame, "LTPresent {}".format(time.strftime("%H:%M:%S", time.localtime(LAST_TIME_PRESENT))), (10, 120),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (100, 255, 100), 1)
    cv2.putText(frame, "LTAbscent {}".format(time.strftime("%H:%M:%S", time.localtime(LAST_TIME_ABSCENT))), (10, 180),
			cv2.FONT_HERSHEY_DUPLEX, 0.5, (100, 100, 255), 1)
    cv2.imshow("Blinks detection", frame)
 
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
vs.stream.release()

if len(TOTALS) > 0:
    print('Average number per minute is: ', (sum(TOTALS)/len(TOTALS)))

#vs.stop()
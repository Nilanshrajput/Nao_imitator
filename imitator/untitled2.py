# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:39:55 2018

@author: Nilansh
"""

import time
import cv2
import numpy as np


def detect_ball_clr(frame, color):

    image = frame

    frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = [20, 100, 100, 179, 255, 255]

    thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.medianBlur(image,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    '''circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
    '''
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:

        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 5:

            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(image, center, 3, (0, 0, 255), -1)
            cv2.putText(image, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            cv2.putText(image, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    return image, thresh, mask, center


cam = cv2.VideoCapture(0)
while (cam.isOpened()):
    _, frame = cam.read()
    if _:

        image1, thresh1, mask1, center1 = detect_ball_clr(frame, "blue")
       # image2,thresh2,mask2,center2=detect_ball_clr(frame,red)
       # image3,thresh3,mask3,center3=detect_ball_clr(frame,green)

        print(center1[0], center1[1])
       # print(center1[0]+10,center2[1])
       # print(center1[0]+10,center3[1])

        # time.sleep(4)

       # image=cv2.addWeighted(image1,1.0,image2,1.0,image3,1.0,0)
        cv2.imshow("image", image1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
cam.release()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
knopen=np.ones((5,5))
knclose=np.ones((20,20))
knopen2=np.ones((2,2))
knclose2=np.ones((10,10))

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret:  
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        lower_red_upper_hue = np.array([160,100,100])
        upper_red_upper_hue = np.array([179,255,255])
        lower_red_lower_hue = np.array([0,100,100])
        upper_red_lower_hue = np.array([10,255,255])
        
        mask_up = cv2.inRange(hsv, lower_red_upper_hue, upper_red_upper_hue)
        mask_low = cv2.inRange(hsv, lower_red_lower_hue, upper_red_lower_hue)
        red=cv2.addWeighted(mask_up,1,mask_low,1,0)
        maskopen=cv2.morphologyEx(red,cv2.MORPH_OPEN,knopen)
        maskclose=cv2.morphologyEx(red,cv2.MORPH_CLOSE,knclose)
        maskopen2=cv2.morphologyEx(red,cv2.MORPH_OPEN,knopen2)
        maskclose2=cv2.morphologyEx(red,cv2.MORPH_CLOSE,knclose2)
        maskfinal=maskclose
        res = cv2.bitwise_and(frame,frame, mask= maskfinal)
        res2 = cv2.bitwise_and(frame,frame, mask= maskclose2)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',maskfinal)
        cv2.imshow('res',res)
        cv2.imshow('res2',res2)
        if cv2.waitKey(5) & 0xFF==ord('q'):
            break

cv2.destroyAllWindows()
cap.release()
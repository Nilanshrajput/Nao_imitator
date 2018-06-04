import cv2
import numpy as num
cam = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cas.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        cv2.rectange(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cam.release()
    cv2.destroyAllWindows()

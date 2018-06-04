import cv2
import math
import naoqi
import argparse
from naoqi import ALProxy
import time


def nao_motion(robotIP, port, angle):
    proxy = ALProxy("ALVideoDevice", "ip", 9599)
    motion_proxy = ALProxy("ALMotion", robotIP, port)

    motion_proxy.setStiffnesses("Head", 1.0)

    target_angle = angle
    maxspeed = 0.1  # using 10%of maximum joint speed
    motion_proxy.setAngle(name, target_angle, maxspeed)
    motion_proxy.setStiffnesses(name, 0.0)


parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, default="127.0.0.1", help="Robot ip address")
parser.add_argument("--port", type=int, default=9559, help="Robot port number")

args = parser.parse_args()


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:

    ret, frame = video_capture.read()
    width, height = cv2.GetSize(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    angle = math.atan2((x + w / 2 - width / 2) / math.fabs(y + h / 2 - height / 2))
    if math.degrees(angle) <= 100 & math.degrees(angle) >= -100:
        nao_motion(args.ip, args.port, angle)

    elif math.degrees(angle) > 100:
        angle = math.radians(100)
        nao_motion(args.ip, args.port, angle)
    elif math.degrees(angle) < -100:
        angle = math.radians(-100)
        nao_motion(args.ip, args.port, angle)

        time.sleep(3)

    out.write(frame)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
out.release()

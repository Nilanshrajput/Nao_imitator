import naoqi
import cv2
import  sys
from naoqi import ALProxy

def head(robotIP,port,angle)
    proxy=ALProxy("ALVideoDevice","ip",9599)
    motion_proxy=ALProxy("ALMotion",robotIP,port)

    motion_proxy.setStiffnesses("Head",1.0)

    name="Head"
    target_angle=angle
    maxspeed=0.1 #using 10%of maximum joint speed
    motion_proxy.setAngle(name, target_angle, maxspeed)
    motion_proxy.setStiffnesses("Head", 0.0)

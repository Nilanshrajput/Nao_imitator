import cv2
import sys



from naoqi import ALProxy
import vision_definitions
import time

IP = "192.168.43.73"  # Replace here with your NAOqi's IP address.
PORT = 9559

####
# Create proxy on ALVideoDevice

print "Creating ALVideoDevice proxy to ", IP

camProxy = ALProxy("ALVideoDevice", IP, PORT)


resolution = vision_definitions.kQQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 20

nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

  
  

camProxy.unsubscribe(nameId)







cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
   
    #ret, frame = video_capture.read()
    frame=camProxy.getImageRemote(nameId)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(30, 30),
	flags=cv2.CASCADE_SCALE_IMAGE
    )

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camProxy.unsubscribe(nameId)



video_capture.release()
cv2.destroyAllWindows()

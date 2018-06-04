import cv2

faceCas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
fourcc=cv2.cv.CV_FOURCC(*'XVID')
out=cv2.VideoWriter('face_detect',fourcc,20.0,(640,480))

while True:
   
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCas.detectMultiScale(gray,1.3,5)
       
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (60, 50, 255), 2)
    out.write(frame)
    cv2.imshow('Face_detect', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
out.release()
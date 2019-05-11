import cv2
import numpy as np
import playsound

face_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
cap = cv2.VideoCapture(0)
scaling_factor=0.5
w = 0


def termina():
	print "Alerta Intruso"
	playsound.playsound('alarma.mp3',True)
	cap.release()
	cv2.destroyAllWindows()


while w == 0:
	ret, frame =cap.read()
	frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,interpolation=cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3 ,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
		if w > 0:
			w=True
	cv2.imshow('Upperbody Detector', frame)
	c=cv2.waitKey(1)
	if c == 27:
		break	


termina()

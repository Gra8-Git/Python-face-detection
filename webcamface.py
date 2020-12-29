import numpy as np
from time import sleep
import cv2

CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
CV_CAP_PROP_FPS = 5
CV_CAP_PROP_FOURCC = 6
CV_CAP_PROP_FRAME_COUNT = 7
CV_CAP_PROP_MODE = 9
CV_CAP_PROP_BRIGHTNESS = 10
CV_CAP_PROP_CONTRAST = 11
CV_CAP_PROP_SATURATION = 12
CV_CAP_PROP_HUE = 13
CV_CAP_PROP_GAIN = 14
CV_CAP_PROP_EXPOSURE = 15
CV_CAP_PROP_SHARPNESS = 20
CV_CAP_PROP_AUTO_EXPOSURE = 21
CV_CAP_PROP_GAMMA = 22
CV_CAP_PROP_TEMPERATURE = 23
CV_CAP_PROP_TRIGGER = 24
CV_CAP_PROP_TRIGGER_DELAY = 25
CV_CAP_PROP_WHITE_BALANCE_RED_V = 26
CV_CAP_PROP_ZOOM = 27
CV_CAP_PROP_FOCUS = 28
CV_CAP_PROP_GUID = 29
CV_CAP_PROP_ISO_SPEED = 30
CV_CAP_PROP_BACKLIGHT = 32
CV_CAP_PROP_PAN = 33
CV_CAP_PROP_TILT = 34
CV_CAP_PROP_ROLL = 35
CV_CAP_PROP_IRIS = 36
CV_CAP_PROP_SETTINGS = 37
CV_CAP_PROP_BITRATE = 47
CV_CAP_PROP_XI_LED_SELECTOR = 411
def draw_border(vface, p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    line_l = 10
	
    cv2.line(vface, (x1, y1), (x1 , y1 + line_l), (255, 255, 0), 1)  # t left
    cv2.line(vface, (x1, y1), (x1 + line_l , y1), (255, 255, 0), 1)
    cv2.line(vface, (x2, y2), (x2 , y2 - line_l), (255, 255, 0), 1)  # b left
    cv2.line(vface, (x2, y2), (x2 + line_l , y2), (255, 255, 0), 1)
    cv2.line(vface, (x3, y3), (x3 - line_l, y3), (255, 255, 0), 1)   # t right
    cv2.line(vface, (x3, y3), (x3, y3 + line_l), (255, 255, 0), 1)
    cv2.line(vface, (x4, y4), (x4 , y4 - line_l), (255, 255, 0), 1)  # b right
    cv2.line(vface, (x4, y4), (x4 - line_l , y4), (255, 255, 0), 1)
    return vface

def videowebcamrun(videosource = 0):
    #user = 'admin'
    #password = '123456'
    #ip_address = '172.16.18.171'
    #port = '7070'
    #stream = 'stream1'
    #rtsp = "rtsp://{}:{}@{}:{}/{}".format(user, password, ip_address, port, stream)
    #VideoCapture(rtsp)
    sleep(1)
    videostream = cv2.VideoCapture(videosource)
    return videostream

def mouseevent(event, x, y, flags,param):
	        if event == cv2.EVENT_LBUTTONDOWN:
	                print("left click")

def camresolution(cap, width = 300, height = 300):
	for x in cap:
	 retnum = x.set(3,width);
	 retnum = x.set(4,height);
	 return retnum

fcascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
videocap = []
videocap.append(videowebcamrun())
videocap[0].set(CV_CAP_PROP_SETTINGS,1)
videocap[0].set(CV_CAP_PROP_XI_LED_SELECTOR,0) 
#ret, lastframe = videocap.read()
ret = camresolution(videocap)
while(True):
	ret, frame = videocap[0].read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = fcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
	for (x, y, w, h) in faces:
		end_cord_x= x + w	#t left
		end_cord_y = y + h	#t left
		bleft_cord_x = x	#b left
		bleft_cord_y = y + h	#b left
		tright_cord_x = x + w	#t right
		tright_cord_y = y	#t right
		frame = draw_border(frame, (x,y), (bleft_cord_x,bleft_cord_y), (tright_cord_x, tright_cord_y), (end_cord_x,end_cord_y))
	cv2.imshow('frame',frame)
	cv2.setMouseCallback("frame",mouseevent)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
videocap[0].release()
sleep(0.5)
cv2.destroyAllWindows()

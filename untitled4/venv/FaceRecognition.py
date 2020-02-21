import cv2
import numpy as np
import os
video_address='http://192.168.1.104:4747/mjpegfeed'
pic_no=0
cap=cv2.VideoCapture(video_address)
ret=True
fa=cv2.CascadeClassifier('faces.xml')
print(fa.load('faces.xml'))
while ret:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=fa.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cropped=frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
        pic_no=pic_no+1
        cv2.imwrite("Jason"+'/'+str(pic_no)+'.jpg',cropped)
    cv2.imshow('frame',frame)
    cv2.waitKey(100)
    #if(pic_no):
    	#break


cap.release()
cv2.destroyAllWindows()


class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
        self.x=None
        self.y=None
        self.w=None
        self.h=None

    def detectFace(self,img):
        cropped=None
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        for (self.x,self.y,self.w,self.h) in faces:
            cropped=img[self.y:self.y+self.h,self.x:self.x+self.w]
        return cropped,self.x,self.y,self.w,self.h
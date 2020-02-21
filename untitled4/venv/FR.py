import cv2
import numpy as np
import os
class FaceRecogition():
    def faceRecogition(self,frame,fa):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=fa.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cropped=frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
        return frame
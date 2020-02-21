
import sys
import time
import cv2
from FR import FaceRecogition
from keras.models import load_model
from MainSYS import Ui_IDrecognitionSYS
#from embedding import emb
import os
from keras.optimizers import RMSprop
from PyQt5 import QtCore, QtGui, QtWidgets
from keras import backend as K
#from PyQt5.QPushButton import QFileDialog,QPushButton

from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt

from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtWidgets import QLabel,QWidget



def contrastive_loss(y_true, y_pred):
    '''Contrastive loss from Hadsell-et-al.'06
    http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    '''
    margin = 1
    sqaure_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * sqaure_pred + (1 - y_true) * margin_square)

def accuracy(y_true, y_pred): # Tensor上的操作
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))

model = load_model('face_reco2.MODEL', {'contrastive_loss': contrastive_loss})
frame1=cv2.imread('Photo/Jason_15071103.jpg',0)
frame2=cv2.imread('Photo/Zee_S20186104W.jpg',0)
frame1=cv2.resize(frame1,(28,28))
frame2=cv2.resize(frame2,(28,28))
ifsame=model.predict([[frame1],[frame2]])
print(ifsame < 0.5)

x_data = []
photo_name = []
class mywindow(QtWidgets.QMainWindow,Ui_IDrecognitionSYS): #这个窗口继承了用QtDesignner 绘制的窗口
    Photo = ''
    TextBrowser_3 = ''
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        rms = RMSprop()
        Photo=os.listdir('Photo')
        for x in Photo:
            frame1 = cv2.imread('Photo/' + x, 0)
            frame1 = frame1.astype('float') / 255.0
            x_data.append(frame1)
            photo_name.append(x)



    def videoprocessing(self):
        #print("gogo")
        #global videoName #在这里设置全局变量以便在线程中使用
        #videoName,videoType= QFileDialog.getOpenFileName(self,# ==#返回路径下视频的全名称==
                                   # "打开视频",
                                    #"",
                                    #" *.jpg;;*.png;;*.jpeg;;*.bmp")
                                    #" *.mp4;;*.avi;;All Files (*)")
        #cap = cv2.VideoCapture(str(videoName))

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

    def setImage(self, image):
        self.label_3.setPixmap(QPixmap.fromImage(image))
        self.label_4.setPixmap(QPixmap.fromImage(image))

class Thread(QThread):#采用线程来播放视频
    changePixmap = pyqtSignal(QtGui.QImage)
    def run(self):
        global  video_address
        cap = cv2.VideoCapture('http://192.168.1.104:4747/mjpegfeed')
        fa = cv2.CascadeClassifier('faces.xml')
        print(cap.isOpened())
        fr=FaceRecogition()

        while (cap.isOpened()==True):
            ret, frame = cap.read()
            if ret:

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgbImage=fr.faceRecogition(rgbImage,fa)
                frame2 = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2GRAY)
                frame2 = frame2.astype('float') / 255.0
                frame2 = cv2.resize(frame2, (28, 28))
                for index in range(len(x_data)):
                    frame1 = cv2.resize(x_data[index], (28, 28))
                    ifsame=model.predict([[frame1],[frame2]])
                    if ifsame < 0.5:
                        print(photo_name[index])
                    time.sleep(0.01)

                Ui_IDrecognitionSYS.setFaceImg(frame[70:70+381,150:150+331])
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)#在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                time.sleep(0.01) #控制视频播放的速度
            else:
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())


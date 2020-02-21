import cv2
import sys
import cv2
import time
from FR import FaceRecogition
from keras.models import load_model
from MainSYS import Ui_IDrecognitionSYS
#from embedding import emb
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

model = load_model('face_reco2.MODEL', {'contrastive_loss': contrastive_loss})
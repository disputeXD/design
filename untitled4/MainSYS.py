# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainSYS.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class Ui_IDrecognitionSYS(object):
    faceImg = ''  # 预存人脸图像
    ifture = False
    name = ''
    def setFaceImg(image):
        Ui_IDrecognitionSYS.faceImg = image
        Ui_IDrecognitionSYS.ifture = True

    def setText(text):
        name = text
        #Ui_IDrecognitionSYS.textBrowser_3.setText(text)

    def setupUi(self, IDrecognitionSYS):
        self.videoprocessing()
        IDrecognitionSYS.setObjectName("IDrecognitionSYS")
        IDrecognitionSYS.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(IDrecognitionSYS)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(480, 60, 101, 31))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        #self.textBrowser.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textBrowser.setFont(font)

        self.textBrowser.setReadOnly(False)

        self.textBrowser.setGeometry(QtCore.QRect(480, 100, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(480, 160, 131, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        #self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 190, 161, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setReadOnly(False)
        self.textBrowser_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 331, 381))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(480, 340, 161, 71))
        self.pushButton.setObjectName("pushButton")
        IDrecognitionSYS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IDrecognitionSYS)
        self.statusbar.setObjectName("statusbar")
        IDrecognitionSYS.setStatusBar(self.statusbar)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 70, 331, 381))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setEnabled(True)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 120, 251, 241))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.tabWidget.addTab(self.tab_2, "")
        self.retranslateUi(IDrecognitionSYS)
        self.pushButton.clicked.connect(IDrecognitionSYS.pushButton_click)
        QtCore.QMetaObject.connectSlotsByName(IDrecognitionSYS)



    def retranslateUi(self, IDrecognitionSYS):
        _translate = QtCore.QCoreApplication.translate
        IDrecognitionSYS.setWindowTitle(_translate("IDrecognitionSYS", "MainWindow"))
        self.label.setText(_translate("IDrecognitionSYS", "<html><head/><body><p><span style=\" font-size:22pt;\">姓名</span></p></body></html>"))
        self.label_2.setText(_translate("IDrecognitionSYS", "<html><head/><body><p><span style=\" font-size:20pt;\">学号</span></p></body></html>"))
        self.pushButton.setText(_translate("IDrecognitionSYS", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("IDrecognitionSYS", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("IDrecognitionSYS", "签到"))

    def pushButton_click(self):
        if self.ifture:
            cv2.imwrite("Photo"+'/'+self.textBrowser.toPlainText()+'_'+self.textBrowser_2.toPlainText()+'.jpg', Ui_IDrecognitionSYS.faceImg);
        if self.name:
            self.textBrowser_3.setPlainText(u"Jason")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainSYS2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IDrecognitionSYS(object):
    def setupUi(self, IDrecognitionSYS):
        IDrecognitionSYS.setObjectName("IDrecognitionSYS")
        IDrecognitionSYS.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(IDrecognitionSYS)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.label_3 = QtWidgets.QLabel(self.Register)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 331, 381))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.Register)
        self.label.setGeometry(QtCore.QRect(510, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.Register)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(510, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Register)
        self.textBrowser_2.setEnabled(True)
        self.textBrowser_2.setGeometry(QtCore.QRect(510, 180, 161, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.Register)
        self.label_2.setGeometry(QtCore.QRect(510, 150, 131, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.Register)
        self.pushButton.setGeometry(QtCore.QRect(510, 310, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.Register, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 70, 331, 381))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setEnabled(True)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 120, 251, 241))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        IDrecognitionSYS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IDrecognitionSYS)
        self.statusbar.setObjectName("statusbar")
        IDrecognitionSYS.setStatusBar(self.statusbar)

        self.retranslateUi(IDrecognitionSYS)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(IDrecognitionSYS.pushButton_click)
        QtCore.QMetaObject.connectSlotsByName(IDrecognitionSYS)

    def retranslateUi(self, IDrecognitionSYS):
        _translate = QtCore.QCoreApplication.translate
        IDrecognitionSYS.setWindowTitle(_translate("IDrecognitionSYS", "MainWindow"))
        self.label.setText(_translate("IDrecognitionSYS", "姓名"))
        self.textBrowser.setHtml(_translate("IDrecognitionSYS", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">q</p></body></html>"))
        self.label_2.setText(_translate("IDrecognitionSYS", "<html><head/><body><p><span style=\" font-size:20pt;\">签到次数</span></p></body></html>"))
        self.pushButton.setText(_translate("IDrecognitionSYS", "签到"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Register), _translate("IDrecognitionSYS", "Register"))
        self.textBrowser_3.setHtml(_translate("IDrecognitionSYS", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jason</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("IDrecognitionSYS", "Tab 2"))



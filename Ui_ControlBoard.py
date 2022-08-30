# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'Ui_ControlBoard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtWidgets
 
class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(360, 600)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    screen = self.frameGeometry()
    center = QtWidgets.QDesktopWidget().availableGeometry().center()
    screen.moveCenter(center)
    self.move(screen.topLeft())


#倒计时总时间设置
    self.QLabel_Time01 = QtWidgets.QLabel(self.centralwidget)
    self.QLabel_Time01.setGeometry(QtCore.QRect(10,10,150,30))
    self.QLineEdit_Time01 = QtWidgets.QLineEdit(self.centralwidget)
    
#倒计时获取总时间
    self.QLineEdit_Time01.setGeometry(QtCore.QRect(130,10,120,30))
    self.QLineEdit_Time01.setPlaceholderText("请输入分钟数")

#倒计时结束前是否播放声音
    self.checkBox01 = QtWidgets.QCheckBox(self.centralwidget)
    self.checkBox01.setGeometry(QtCore.QRect(10,50,115,30))
    self.checkBox01.setObjectName("checkBox01")
    
#倒计时结束读秒
    self.QLineEdit_Time02 = QtWidgets.QLineEdit(self.centralwidget)
    self.QLineEdit_Time02.setGeometry(QtCore.QRect(130,50,90,30))
    self.QLineEdit_Time02.setPlaceholderText("多少分钟")
    
#倒计时获取总时间
    self.QLabel_Time02 = QtWidgets.QLabel(self.centralwidget)
    self.QLabel_Time02.setGeometry(QtCore.QRect(225,50,300,30))
    
#倒计时获取总时间
    self.QLineEdit_Time03 = QtWidgets.QLineEdit(self.centralwidget)
    self.QLineEdit_Time03.setGeometry(QtCore.QRect(10,90,70,30))
    self.QLineEdit_Time03.setPlaceholderText("多少秒")
    
#倒计时获取总时间
    self.QLabel_Time03 = QtWidgets.QLabel(self.centralwidget)
    self.QLabel_Time03.setGeometry(QtCore.QRect(85,90,300,30))

#倒计时结束计时勾选
    self.checkBox02 = QtWidgets.QCheckBox(self.centralwidget)
    self.checkBox02.setGeometry(QtCore.QRect(10,130,300,30))
    self.checkBox02.setObjectName("checkBox02")

#倒计时结束后执行
    self.QLabel_cb = QtWidgets.QLabel(self.centralwidget)
    self.QLabel_cb.setGeometry(QtCore.QRect(10,170,300,30))

#倒计时结束后动作执行 播放PPT 退出播放PPT
    self.comboBox = QtWidgets.QComboBox(self.centralwidget)
    self.comboBox.setGeometry(QtCore.QRect(10,210,340,30))
    self.comboBox.addItems(['保持播放PPT','退出播放PPT'])
    self.comboBox.setObjectName("QComboBox")

#倒计时结束后是否继续计时
    self.checkBox03 = QtWidgets.QCheckBox(self.centralwidget)
    self.checkBox03.setGeometry(QtCore.QRect(10,250,300,30))
    self.checkBox03.setObjectName("checkBox03")

#添加PPT按钮
    self.pushButton_choose = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton_choose.setGeometry(QtCore.QRect(10,290,340,30))
    #self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
    #self.pushButton_delete.setGeometry(QtCore.QRect(185,290,165,30))

    self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
    self.textBrowser.setGeometry(QtCore.QRect(10, 330, 340, 200))
    self.textBrowser.setObjectName("textBrowser")


#开始PPT倒计时按钮
    self.pushButton_enter = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton_enter.setGeometry(QtCore.QRect(10,550,340,30))

    #self.pushButton_cancle = QtWidgets.QPushButton(self.centralwidget)
    #self.pushButton_cancle.setGeometry(QtCore.QRect(185,550,165,30))

    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(100, 0, 0, 100))
    self.menubar.setObjectName("menubar")
    MainWindow.setMenuBar(self.menubar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    
    MainWindow.setWindowTitle(_translate("MainWindow","PPT计时器"))
    self.QLabel_Time01.setText(_translate("MainWindow","倒计时总时间设置"))
    self.checkBox01.setText(_translate("MainWindow","倒计时结束前"))
    self.QLabel_Time02.setText(_translate("MainWindow","分钟播放一次提示音"))
    self.QLabel_Time03.setText(_translate("MainWindow","秒后开始倒计时"))
    self.checkBox02.setText(_translate("MainWindow","倒计时结束时是否播放提示音"))
    self.QLabel_cb.setText(_translate("MainWindow","倒计时结束后执行"))
    self.checkBox03.setText(_translate("MainWindow","倒计时结束后是否继续计时"))
    self.pushButton_choose.setText(_translate("MainWindow","添加PPT"))
#    self.pushButton_delete.setText(_translate("MainWindow","删除PPT"))
    self.pushButton_enter.setText(_translate("MainWindow","开始PPT倒计时"))
#    self.pushButton_cancle.setText(_translate("MainWindow","重置"))

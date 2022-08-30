import sys
import os
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog:

    def setupUi(self,Dialog,num01,num02,num03,tip_end,tip_before,time_continue):
        Dialog.setWindowTitle("PTT倒计时中")
        Dialog.resize(150,80)
        #Dialog.setWindowOpacity(0.3)
##在右上角位置
        screen = QDesktopWidget().screenGeometry() 
        size = Dialog.geometry()  
        Dialog.move(screen.width() - size.width(),0)  

#        Dialog.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.Tool)
#        Dialog.setWindowFlags(Dialog.windowFlags()|Qt.WindowStaysOnTopHint|Qt.Tool)
##取消标题栏及画面置顶
        Dialog.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.Tool)
        layout = QGridLayout(Dialog)
        Dialog.setLayout(layout)
        #with open("coner.qss", "r", encoding="utf-8") as f:
        #    style = f.read()
        #    Dialog.setStyleSheet(style)


##圆角样式
        rect = QRectF(0, 0, Dialog.width(), Dialog.height())
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        Dialog.setMask(region)
        
##右键关闭功能创建
        Dialog.setContextMenuPolicy(Qt.CustomContextMenu)
        Dialog.customContextMenuRequested.connect(Dialog.create_rightmenu)

##从self中传递参数到Dialog中
        Dialog.tip_end=tip_end
        Dialog.tip_before=tip_before
        Dialog.time_continue=time_continue
        num02=int(num02)
        Dialog.num02=num02*60
        num03=int(num03)
        Dialog.num03=num03
        Dialog.show()
        Dialog.time=int(num01)
        
##倒计时器功能
        Dialog.label = QLabel("<font color=red size=5 > <b>倒计时%s分钟</b>" % (Dialog.time))
        Dialog.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(Dialog.label, 0, 0, 1, 2)
        Dialog.time_before=Dialog.time*60
        Dialog.time=Dialog.time*60+Dialog.num03+1
        Dialog.time_continue_num=0
        Dialog.timer = QTimer()
        Dialog.timer.timeout.connect(Dialog.showtime)
        Dialog.starttimer()


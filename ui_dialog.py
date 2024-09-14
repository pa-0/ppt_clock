import sys
import os
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog:

    def setupUi(self,Dialog,num01,num02,num03,tip_end,tip_before,time_continue):
        Dialog.setWindowTitle("PowerPoint Clock")
        Dialog.resize(150,80)
        #Dialog.setWindowOpacity(0.3)
# In the upper right corner
        screen = QDesktopWidget().screenGeometry() 
        size = Dialog.geometry()  
        Dialog.move(screen.width() - size.width(),0)  

#        Dialog.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.Tool)
#        Dialog.setWindowFlags(Dialog.windowFlags()|Qt.WindowStaysOnTopHint|Qt.Tool)
# Cancel title bar and screen top
        Dialog.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.Tool)
        layout = QGridLayout(Dialog)
        Dialog.setLayout(layout)
        #with open("coner.qss", "r", encoding="utf-8") as f:
        #    style = f.read()
        #    Dialog.setStyleSheet(style)


## rounded corner style
        rect = QRectF(0, 0, Dialog.width(), Dialog.height())
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        Dialog.setMask(region)
        
# Right click to close function creation
        Dialog.setContextMenuPolicy(Qt.CustomContextMenu)
        Dialog.customContextMenuRequested.connect(Dialog.create_rightmenu)

# Pass parameters from self to dialog
        Dialog.tip_end=tip_end
        Dialog.tip_before=tip_before
        Dialog.time_continue=time_continue
        num02=int(num02)
        Dialog.num02=num02*60
        num03=int(num03)
        Dialog.num03=num03
        Dialog.show()
        Dialog.time=int(num01)
        
# Countdown timer function
        Dialog.label = QLabel("<font color=red size=5 > <b>Countdown %s minutes</b>" % (Dialog.time))
        Dialog.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(Dialog.label, 0, 0, 1, 2)
        Dialog.time_before=Dialog.time*60
        Dialog.time=Dialog.time*60+Dialog.num03+1
        Dialog.time_continue_num=0
        Dialog.timer = QTimer()
        Dialog.timer.timeout.connect(Dialog.showtime)
        Dialog.starttimer()


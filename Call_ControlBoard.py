#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui
import sys
import os
import subprocess
import time
from PyQt5.QtCore import QEventLoop, QTimer,QPoint
from PyQt5.QtGui import QCursor, QIcon, QFont,QPixmap,QPalette
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit, QCheckBox, QComboBox, QDesktopWidget, QMenu, QAction, QFileDialog
from ui_dialog import Ui_Dialog
from Ui_ControlBoard import Ui_MainWindow


class MyThread(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, param=None, parent=None):
        super(MyThread, self).__init__(parent)
        # 如果有参数，可以封装在类里面
        self.param = param

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

##多线程信号发送
    def run(self):        
        p = subprocess.Popen(self.param, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)       
        i=0
        while True:
            result = p.stdout.readline()
            if result != b'':
                print(result.decode('utf-8').strip('\r\n')) 
                self.write(result.decode('utf-8').strip('\r\n'))
            else:
                break
        while True:
            result = p.stderr.readline()
            if result != b'':
                print(result.decode('utf-8').strip('\r\n')) 
                self.write(result.decode('utf-8').strip('\r\n'))
            else:
                break
        p.stdout.close()
        p.stderr.close()
        p.wait()

#主进程入口
class ControlBoard(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(ControlBoard, self).__init__()
    self.setupUi(self)
    self.pushButton_choose.clicked.connect(self.realtime_display1)
    self.pushButton_enter.clicked.connect(self.pptTime)


######-----------------------------------------按钮“添加PPT”命令行修改处-------------------------------------
  def realtime_display1(self): 
    
    reply=QMessageBox.information(self,'提示','是否要添加PPT?',QMessageBox.Yes,QMessageBox.No)
    if reply==QMessageBox.Yes:
      openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'All Files(*)')
      index="echo {a}".format(a=openfile_name[0].rsplit('/',1)[1])
      try:
          self.t = MyThread(index)
          self.t.signalForText.connect(self.outputWritten) 
          self.t.start()
      except Exception as e:
          raise e
      loop = QEventLoop()
      QTimer.singleShot(2000, loop.quit)
      loop.exec_()
    else:
      pass

######-----------------------------------------按钮“开始计时”命令行修改处-------------------------------------  
  def pptTime(self):
    reply=QMessageBox.information(self,'提示','确定开始倒计时吗?',QMessageBox.Yes,QMessageBox.No)
    if reply==QMessageBox.Yes:
        tip_before = self.checkBox01.isChecked()
        tip_end = self.checkBox02.isChecked()
        time_continue = self.checkBox03.isChecked()
        num01="{time01}".format(time01=self.QLineEdit_Time01.text())
        num02="{time02}".format(time02=self.QLineEdit_Time02.text())
        num03="{time03}".format(time03=self.QLineEdit_Time03.text())
        if len(num02) == 0:
            num02 = 0
        if len(num03) == 0:
            num03 = 0
        self.hide()
        dialog = PreferencesDialog(num01,num02,num03,tip_end,tip_before,time_continue,parent = self)
        if dialog.exec():
            pass
        else:
            self.show()
            if self.comboBox.currentIndex()==0:
                os.system("echo continue")
            if self.comboBox.currentIndex()==1:
                os.system("killall wpp")
    else:
        pass


  def outputWritten(self, text):
    cursor = self.textBrowser.textCursor()
    cursor.movePosition(QtGui.QTextCursor.End)
    self.textBrowser.append(text)
    self.textBrowser.setTextCursor(cursor)
    self.textBrowser.ensureCursorVisible()


###右键确认关闭弹出----------------
  def closeEvent(self,event):
      reply=QMessageBox.question(self,'Message','确定要退出吗?',QMessageBox.Yes,QMessageBox.No)
      self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
      if reply==QMessageBox.Yes:
          event.accept()
      else:
          event.ignore()


###右键功能的类----------------
class PreferencesDialog(QDialog):
    def __init__(self,num01,num02,num03,tip_end,tip_before,time_continue,parent=None):
        super(PreferencesDialog,self).__init__(parent)
        self.ui =Ui_Dialog()
        self.ui.setupUi(self,num01,num02,num03,tip_end,tip_before,time_continue)

    def create_rightmenu(self):
        self.groupBox_menu = QMenu(self)
#        self.actionA = QAction(u'移动',self)
#        self.groupBox_menu.addAction(self.actionA)
        self.actionB = QAction(u'关闭',self)
        self.groupBox_menu.addAction(self.actionB)
#        self.actionA.triggered.connect(self.button_move)
        self.actionB.triggered.connect(self.button_close)
        self.groupBox_menu.popup(QCursor.pos())

    def button_close(self):
        self.close()



#--------PPT针对timer计时的延续----------
    def showtime(self):
        if self.time > 0:
            self.time -= 1
            if self.time > self.time_before:
                if self.num03 == 0:
                    pass
                else:
                    self.label.setText("<font color=red size=10 > <b>%s秒</b>" % (self.time-self.time_before))
                    self.label.setAlignment(Qt.AlignCenter)
            else:
                m,s=divmod(self.time,60)
                self.label.setText("<font color=red size=40 > <b>%02d:%02d</b>" % (m,s))
                self.label.setAlignment(Qt.AlignCenter)
            if self.time == self.num02:
                if self.tip_before:
                    if self.num02 == 0:
                        pass
                    else:
                        os.system("aplay /opt/apps/com.ppt_clock/1.wav")
            if self.time_continue:
                pass
            else:
                if self.time == 0:
                    if self.tip_end:
                        os.system("aplay /opt/apps/com.ppt_clock/1.wav")
                    self.endtimer()
                    self.close()
        else:
            self.time_continue_num += 1
            m,s=divmod(self.time_continue_num,60)
            self.label.setText("<font color=red size=40 > <b>- %02d:%02d</b>" % (m,s))
            self.label.setAlignment(Qt.AlignCenter)
            if self.time == 0:
                if self.tip_end:
                    self.tip_end=False
                    os.system("aplay /home/uos/Desktop/clock/1.wav")

##---------------------1000毫秒等于1秒---------------
    def starttimer(self):
        self.timer.start(1000)

    def endtimer(self):
        self.timer.stop()
        

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = ControlBoard()
  win.show()
  sys.exit(app.exec_()) 

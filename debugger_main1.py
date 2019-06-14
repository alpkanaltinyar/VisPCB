# -*- coding: utf-8 -*-
"""
Created on Sat Apr 06 02:20:29 2019

@author: bil
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 22:53:05 2019

@author: bil
"""
import numpy as np
import cv2
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import debugger_gui1
import serial
import time

class myApp(QMainWindow,debugger_gui1.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myApp,self).__init__(parent)
        self.setupUi(self)
        self.buttonR.clicked.connect(self.R)
        self.buttonL.clicked.connect(self.L)
        self.buttonu.clicked.connect(self.UP)
        self.buttonDOWN.clicked.connect(self.DOWN)
        self.buttonF.clicked.connect(self.F)
        self.buttonstart.clicked.connect(self.START)
        self.buttonstartcam.clicked.connect(self.STARTCAM)
        self.buttonstopcam.clicked.connect(self.STOPCAM)
        self.buttonsnap.clicked.connect(self.SNAP)
        self.buttonboard.clicked.connect(self.SCANBOARD)
        self.radioRef.toggled.connect(self.setMode)
        self.radioTest.toggled.connect(self.setMode)
        
        
        self.myport=serial.Serial("COM3",timeout=3)
        self.videoTimer=QTimer()
              
        self.videoTimer.timeout.connect(self.getFrame)
               
        self.vidobj=None
        self.count=0
        self.mode = 0
      
        
        self.pic=1
    def getFrame(self):
        f,image=self.vidobj.read()
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        sub=QImage(image,image.shape[1],image.shape[0],QImage.Format_RGB888)
        pixmap=QPixmap.fromImage(sub)
        
        self.videoarea.setPixmap(pixmap)
        
        
        
    def STARTCAM(self):
        self.vidobj=cv2.VideoCapture(0)
        self.vidobj.set(6,cv2.cv.CV_FOURCC('M','J','P','G') & 0xFF)
        self.vidobj.set(5,30)
        self.vidobj.set(4,720)
        self.vidobj.set(3,1280)
        self.videoTimer.start(1000/30.)
        self.buttonstartcam.setEnabled(False)
        self.buttonstopcam.setEnabled(True)
        self.buttonsnap.setEnabled(True)
    def STOPCAM(self):
        self.videoTimer.stop()
        self.buttonstartcam.setEnabled(True)
        self.buttonstopcam.setEnabled(False)
        self.buttonsnap.setEnabled(False)
        self.vidobj.release()

    def SNAP(self):
        self.videoTimer.stop()
        f,g=self.vidobj.read()
        
        cv2.imwrite("debuggerpic" + str(self.count)+".jpeg" ,g)
        self.count+=1
        self.videoTimer.start(1000/30.)
              
    def F(self):
        self.myport.write("F")
    
    def R(self):
        steps = self.line_stepsize.text()
        
        self.myport.write("R"+str(steps)+"\n\r")
    def L(self):
        steps = self.line_stepsize.text()
        
        self.myport.write("L"+str(steps)+"\n\r")
    def UP(self):
        steps = self.line_stepsize.text()
        
        self.myport.write("U"+str(steps)+"\n\r")
    def DOWN(self):
        steps = self.line_stepsize.text()
        
        self.myport.write("D"+str(steps)+"\n\r")
    def START(self):
        self.myport.write("S\n\r")
    
    def SCANBOARD(self):
        self.groupVideo.setEnabled(False)
        if self.vidobj==None:
            self.vidobj=cv2.VideoCapture(0)
            time.sleep(1)
            self.vidobj.set(6,cv2.cv.CV_FOURCC('M','J','P','G') & 0xFF)
            self.vidobj.set(5,30)
            self.vidobj.set(4,720)
            self.vidobj.set(3,1280)
        elif not(self.vidobj.isOpened()):
            self.vidobj.open(0)
        if self.videoTimer.isActive():
            self.videoTimer.stop()
            time.sleep(1)
        self.myport.write("S")
        #-----------------------------------------
        rows=3
        cols=3
        H=720
        W=1280
        Ver_line=np.zeros((0,W*3,3))
        Hor_line=np.zeros((H,0,3))

        a=1
        for j in range(rows):
            Hor_line=np.zeros((H,0,3))
            for i in range(cols):
                self.waitMessage("C")
                time.sleep(0.5)
                f,frame=self.vidobj.read()
                f,frame=self.vidobj.read()
                print frame.shape
                if (j % 2)==0:
                    Hor_line=np.hstack((Hor_line,frame))
                else:
                    Hor_line=np.hstack((frame,Hor_line))
                time.sleep(0.5)
                print ("ok"+str(a))
                self.myport.write("M")
                print(a)                
                a=+1
                time.sleep(0.5)
            Ver_line=np.vstack((Hor_line,Ver_line))
            
            # Ver_line: Whole Picture
        # Fork: 1) REf Card? 2) Test Card?
        if self.mode==0:
            cv2.imwrite("ReferenceCard.jpeg" ,Ver_line)
        elif self.mode==1:
            im2 = cv2.imread("ReferenceCard.jpeg",0)
            r,th = cv2.threshold(Ver_line,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            r1,th1 = cv2.threshold(im2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            differ = cv2.subtract(th1,th).astype('bool')
            print "Score:", len(differ.nonzero()[0])
            
        
            
        self.groupVideo.setEnabled(True)
    def setMode(self):
        if self.radioRef.isChecked():
            self.mode = 0 # Reference
        else:
            self.mode = 1 # Test mode
        
                
   
    def waitMessage(self,message ):
        while True:
            if (self.myport.read()==message):
                break
        return True
        
    

        
        
                
             
         
            
        
        


        






app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()
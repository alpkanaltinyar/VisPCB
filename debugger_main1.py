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
import debugger_ver2_gui
import serial
import time

class myApp(QMainWindow,debugger_ver2_gui.Ui_MainWindow):
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
        self.setWindowTitle('VisPCB: Vision Based PCB Defect Analyser')
        self.line_stepsize.setText(u'5')


        self.myport=serial.Serial("COM3",timeout=3)
        self.videoTimer=QTimer()

        self.videoTimer.timeout.connect(self.getFrame)

        self.vidobj=None
        self.count=0
        self.mode = 0
        self.videoindex = 1
        self.scanindex = ((1,1),(1,2),(1,3),(2,3),(2,2),(2,1),(3,1),(3,2),(3,3))

        im2 = cv2.imread("ReferenceCard.jpeg")
        self.im2label(im2,self.imRef)


        self.pic=1
    def getFrame(self):
        f,image=self.vidobj.read()
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        M=cv2.getRotationMatrix2D((640,360),-0.9,1)
        image=cv2.warpAffine(image,M,(1280,720))
        cv2.line(image,(32,360),(0,360),(0,255,0),5)
        cv2.line(image,(1279,360),(1279-32,360),(0,255,0),5)
        cv2.line(image,(640,0),(640,31),(0,255,0),5)
        cv2.line(image,(640,719),(640,719-32),(0,255,0),5)
        cv2.line(image,(640-32,360),(640+32,360),(0,255,0),5)
        cv2.line(image,(640,360-32),(640,360+32),(0,255,0),5)
        sub=QImage(image,image.shape[1],image.shape[0],QImage.Format_RGB888)

        pixmap=QPixmap.fromImage(sub)
        pixmap=pixmap.scaled(self.videoarea.width(),self.videoarea.height(),Qt.KeepAspectRatio)

        self.videoarea.setPixmap(pixmap)



    def STARTCAM(self):
        self.vidobj=cv2.VideoCapture(self.videoindex)
        while not (self.vidobj.set(3,1280)):
            time.sleep(.1)
        while not (self.vidobj.set(4,720)):
            time.sleep(.1)
        while not (self.vidobj.set(5,30)):
            time.sleep(.1)
        while not (self.vidobj.set(6,cv2.cv.CV_FOURCC('M','J','P','G') & 0xFF)):
            time.sleep(.1)
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
        steps = float(self.line_stepsize.text())*400

        self.myport.write("R"+str(steps)+"\n\r")
    def L(self):
        steps = float(self.line_stepsize.text())*400

        self.myport.write("L"+str(steps)+"\n\r")
    def UP(self):
        steps = float(self.line_stepsize.text())*400

        self.myport.write("U"+str(steps)+"\n\r")
    def DOWN(self):
        steps = float(self.line_stepsize.text())*400

        self.myport.write("D"+str(steps)+"\n\r")
    def START(self):
        self.myport.write("S\n\r")

    def SCANBOARD(self):
        self.groupVideo.setEnabled(False)
        if self.vidobj==None:
            self.vidobj=cv2.VideoCapture(self.videoindex)
            time.sleep(1)

        elif not(self.vidobj.isOpened()):
            self.vidobj.open(1)
        if self.videoTimer.isActive():
            self.videoTimer.stop()
            time.sleep(1)

        while not (self.vidobj.set(3,1280)):
            time.sleep(.1)

        while not (self.vidobj.set(4,720)):
            time.sleep(.1)

        while not (self.vidobj.set(5,30)):
            time.sleep(.1)
        while not (self.vidobj.set(6,cv2.cv.CV_FOURCC('M','J','P','G') & 0xFF)):
            time.sleep(.1)
        print "camera parameters set ..."
        self.myport.write("S")
        #-----------------------------------------
        rows=3
        cols=3
        H=720
        W=1280
        Ver_line=np.zeros((0,W*3,3))
        Hor_line=np.zeros((H,0,3))

        a=0
        for j in range(rows):
            Hor_line=np.zeros((H,0,3))
            for i in range(cols):
                self.waitMessage("C")
                time.sleep(0.5)
                f,frame=self.vidobj.read()
                f,frame=self.vidobj.read()
                #M=cv2.getRotationMatrix2D((640,360),-0.9,1)
                #frame=cv2.warpAffine(frame,M,(1280,720))
                print 'Grid :' ,self.scanindex[a]
                if (j % 2)==0:
                    Hor_line=np.hstack((Hor_line,frame))
                else:
                    Hor_line=np.hstack((frame,Hor_line))
                time.sleep(0.5)

                self.myport.write("M")
                print 'Done...'
                a=a+1
                time.sleep(0.5)
            Ver_line=np.vstack((Hor_line,Ver_line))

            # Ver_line: Whole Picture
        # Fork: 1) REf Card? 2) Test Card?
        if self.mode==0:
            cv2.imwrite("ReferenceCard.jpeg" ,Ver_line)
            time.sleep(1)
            im2 = cv2.imread("ReferenceCard.jpeg")
            self.im2label(im2,self.imRef)

        elif self.mode==1:
            im2 = cv2.imread("ReferenceCard.jpeg",0)

            cv2.imwrite("TestedCard.jpeg",Ver_line)
            imtest = cv2.imread("TestedCard.jpeg")
            self.im2label(imtest,self.imTest)

            Ver_line=cv2.cvtColor(Ver_line.astype('uint8'), cv2.COLOR_BGR2GRAY)
            """
            r,th = cv2.threshold(Ver_line,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            #kernel = np.ones((5,5),np.uint8)
            #erosionTh = cv2.erode(th,kernel,iterations = 1)
            cv2.imwrite("ReferenceThresHold.jpeg",th)

            r1,th1 = cv2.threshold(im2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            #kernel1 = np.ones((5,5),np.uint8)
            #erosionTh1 = cv2.erode(th1,kernel1,iterations = 1)
            cv2.imwrite("TestThresHold.jpeg",th1)
            """
            differ = im2.astype('double')-Ver_line.astype('double')
            differ = differ - differ.min()
            differ=255*(differ/differ.max())

            #differ = cv2.subtract(th1,th).astype('bool')
            cv2.imwrite("difference.jpeg",differ.astype('uint8'))
            imDiff = cv2.imread("difference.jpeg")
            self.im2label(imDiff,self.imDiff)


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

    def im2label(self,image,label):
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        sub=QImage(image,image.shape[1],image.shape[0],QImage.Format_RGB888)
        pixmap=QPixmap.fromImage(sub)
        pixmap=pixmap.scaled(label.width(),label.height(),Qt.KeepAspectRatio)
        label.setPixmap(pixmap)




















app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()
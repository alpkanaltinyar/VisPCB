# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\debugger_ver2_gui.ui'
#
# Created: Thu Jun 20 18:56:42 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1540, 841)
        MainWindow.setMaximumSize(QtCore.QSize(11111111, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tab1 = QtGui.QTabWidget(self.centralwidget)
        self.tab1.setGeometry(QtCore.QRect(10, 0, 1511, 791))
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.videoarea = QtGui.QLabel(self.tab)
        self.videoarea.setGeometry(QtCore.QRect(190, 10, 1280, 720))
        self.videoarea.setMaximumSize(QtCore.QSize(1280, 11111))
        self.videoarea.setText(_fromUtf8(""))
        self.videoarea.setObjectName(_fromUtf8("videoarea"))
        self.groupVideo = QtGui.QGroupBox(self.tab)
        self.groupVideo.setGeometry(QtCore.QRect(-10, 110, 201, 131))
        self.groupVideo.setObjectName(_fromUtf8("groupVideo"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupVideo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonstartcam = QtGui.QPushButton(self.groupVideo)
        self.buttonstartcam.setEnabled(True)
        self.buttonstartcam.setObjectName(_fromUtf8("buttonstartcam"))
        self.verticalLayout.addWidget(self.buttonstartcam)
        self.buttonstopcam = QtGui.QPushButton(self.groupVideo)
        self.buttonstopcam.setEnabled(False)
        self.buttonstopcam.setObjectName(_fromUtf8("buttonstopcam"))
        self.verticalLayout.addWidget(self.buttonstopcam)
        self.buttonsnap = QtGui.QPushButton(self.groupVideo)
        self.buttonsnap.setEnabled(False)
        self.buttonsnap.setObjectName(_fromUtf8("buttonsnap"))
        self.verticalLayout.addWidget(self.buttonsnap)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 250, 191, 231))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonu = QtGui.QPushButton(self.groupBox)
        self.buttonu.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonu.setObjectName(_fromUtf8("buttonu"))
        self.gridLayout.addWidget(self.buttonu, 0, 1, 1, 1)
        self.buttonDOWN = QtGui.QPushButton(self.groupBox)
        self.buttonDOWN.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonDOWN.setObjectName(_fromUtf8("buttonDOWN"))
        self.gridLayout.addWidget(self.buttonDOWN, 2, 1, 1, 1)
        self.buttonL = QtGui.QPushButton(self.groupBox)
        self.buttonL.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonL.setObjectName(_fromUtf8("buttonL"))
        self.gridLayout.addWidget(self.buttonL, 1, 0, 1, 1)
        self.buttonR = QtGui.QPushButton(self.groupBox)
        self.buttonR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonR.setObjectName(_fromUtf8("buttonR"))
        self.gridLayout.addWidget(self.buttonR, 1, 2, 1, 1)
        self.buttonF = QtGui.QPushButton(self.groupBox)
        self.buttonF.setMaximumSize(QtCore.QSize(60, 16777215))
        self.buttonF.setObjectName(_fromUtf8("buttonF"))
        self.gridLayout.addWidget(self.buttonF, 1, 1, 1, 1)
        self.line_stepsize = QtGui.QLineEdit(self.groupBox)
        self.line_stepsize.setObjectName(_fromUtf8("line_stepsize"))
        self.gridLayout.addWidget(self.line_stepsize, 5, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.buttonstart = QtGui.QPushButton(self.groupBox)
        self.buttonstart.setEnabled(False)
        self.buttonstart.setMaximumSize(QtCore.QSize(70, 16777215))
        self.buttonstart.setObjectName(_fromUtf8("buttonstart"))
        self.gridLayout.addWidget(self.buttonstart, 5, 0, 1, 1)
        self.tab1.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 141, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 97, 84))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioRef = QtGui.QRadioButton(self.layoutWidget)
        self.radioRef.setChecked(True)
        self.radioRef.setObjectName(_fromUtf8("radioRef"))
        self.verticalLayout_2.addWidget(self.radioRef)
        self.radioTest = QtGui.QRadioButton(self.layoutWidget)
        self.radioTest.setObjectName(_fromUtf8("radioTest"))
        self.verticalLayout_2.addWidget(self.radioTest)
        self.buttonboard = QtGui.QPushButton(self.groupBox_2)
        self.buttonboard.setGeometry(QtCore.QRect(10, 120, 95, 28))
        self.buttonboard.setObjectName(_fromUtf8("buttonboard"))
        self.imRef = QtGui.QLabel(self.tab_2)
        self.imRef.setGeometry(QtCore.QRect(190, 70, 426, 240))
        self.imRef.setObjectName(_fromUtf8("imRef"))
        self.imTest = QtGui.QLabel(self.tab_2)
        self.imTest.setGeometry(QtCore.QRect(820, 70, 426, 240))
        self.imTest.setObjectName(_fromUtf8("imTest"))
        self.imDiff = QtGui.QLabel(self.tab_2)
        self.imDiff.setGeometry(QtCore.QRect(480, 360, 426, 240))
        self.imDiff.setObjectName(_fromUtf8("imDiff"))
        self.tab1.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1540, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pcb", None))
        self.groupVideo.setTitle(_translate("MainWindow", "Camera Controls", None))
        self.buttonstartcam.setText(_translate("MainWindow", "Start Camera", None))
        self.buttonstopcam.setText(_translate("MainWindow", "Stop Camera", None))
        self.buttonsnap.setText(_translate("MainWindow", "Snapshot", None))
        self.groupBox.setTitle(_translate("MainWindow", "Jogging", None))
        self.buttonu.setToolTip(_translate("MainWindow", "up", None))
        self.buttonu.setStatusTip(_translate("MainWindow", "UP", None))
        self.buttonu.setText(_translate("MainWindow", "U", None))
        self.buttonDOWN.setToolTip(_translate("MainWindow", "DOWN", None))
        self.buttonDOWN.setStatusTip(_translate("MainWindow", "DOWN", None))
        self.buttonDOWN.setText(_translate("MainWindow", "D", None))
        self.buttonL.setToolTip(_translate("MainWindow", "Left", None))
        self.buttonL.setStatusTip(_translate("MainWindow", "Left", None))
        self.buttonL.setText(_translate("MainWindow", "L", None))
        self.buttonR.setToolTip(_translate("MainWindow", "Right", None))
        self.buttonR.setStatusTip(_translate("MainWindow", "Right", None))
        self.buttonR.setText(_translate("MainWindow", "R", None))
        self.buttonF.setToolTip(_translate("MainWindow", "for RESET", None))
        self.buttonF.setStatusTip(_translate("MainWindow", "reset", None))
        self.buttonF.setText(_translate("MainWindow", "RST", None))
        self.label.setText(_translate("MainWindow", "Step size (mm):", None))
        self.buttonstart.setToolTip(_translate("MainWindow", "start", None))
        self.buttonstart.setStatusTip(_translate("MainWindow", "Starting", None))
        self.buttonstart.setText(_translate("MainWindow", "START", None))
        self.tab1.setTabText(self.tab1.indexOf(self.tab), _translate("MainWindow", "PCB Browser", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "PCB Type", None))
        self.radioRef.setText(_translate("MainWindow", "Reference", None))
        self.radioTest.setText(_translate("MainWindow", "Tested", None))
        self.buttonboard.setText(_translate("MainWindow", "Scan Board", None))
        self.imRef.setText(_translate("MainWindow", "Reference Image", None))
        self.imTest.setText(_translate("MainWindow", "Test Image", None))
        self.imDiff.setText(_translate("MainWindow", "Difference Image", None))
        self.tab1.setTabText(self.tab1.indexOf(self.tab_2), _translate("MainWindow", "PCB Test", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


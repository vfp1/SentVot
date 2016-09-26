__author__ = 'Victor'
from PyQt4 import QtGui, QtCore
import os

class Ui_SentVotWarning(object):
    def setupUiWarning(self, window_warning):
        window_warning.setWindowTitle("SentVot Warning")

        #Setting the Central Widget
        self.centralWidget = QtGui.QWidget(window_warning)
        self.centralWidget.setMinimumSize(300, 300)
        self.centralWidget.setGeometry(400, 200, 600, 500)

        #Text About
        self.text_about = QtGui.QLabel()
        self.text_about.setText("Before you start drawing, please" + '\n' +
                                "save your name at the Layer Manager at" + '\n' +
                                "the right (on the button 'Save new interviewee')" + '\n' +
                                "and save it. Then everything will" + '\n' +
                                "be ready to start!")
        self.separator_2 = QtGui.QFrame()
        self.separator_2.setFrameStyle(QtGui.QFrame.HLine)
        self.accept_button = QtGui.QPushButton("I understand, let's go!")

        about_frame = QtGui.QGroupBox(self)
        about_frame.setTitle("Warning!")
        about = QtGui.QVBoxLayout()
        about.addWidget(self.text_about)
        about.addWidget(self.separator_2)
        about.addWidget(self.accept_button)
        about_frame.setLayout(about)

        window_warning.setCentralWidget(about_frame)

        window_warning.resize(window_warning.sizeHint())
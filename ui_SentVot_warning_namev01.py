__author__ = 'vfp1'

from PyQt4 import QtGui, QtCore
import os

class Ui_SentVotWarningName(object):
    def setupUiWarningName(self, window_warning):
        window_warning.setWindowTitle("SentVot Warning")

        #Setting the Central Widget
        self.centralWidget = QtGui.QWidget(window_warning)
        self.centralWidget.setMinimumSize(300, 300)
        self.centralWidget.setGeometry(400, 200, 600, 500)

        #Text About
        self.text_about = QtGui.QLabel()
        self.text_about.setText("Please do not use Icelandic or other" + '\n' +
                                "special characters for saving names." + '\n' +
                                "The database of SentVot is quite" + '\n' +
                                "intolerant with the beautiful Icelandic" + '\n' +
                                "language, or with any character which is" + '\n' +
                                "non-ASCII. We will work on that for letting" + '\n' +
                                "our database accept it! (By basically including" + '\n' +
                                "extended ASCII codes soon)")
        self.separator_2 = QtGui.QFrame()
        self.separator_2.setFrameStyle(QtGui.QFrame.HLine)
        self.accept_button = QtGui.QPushButton("This database is discriminatory," + '\n' +
                                               "but I will accept it for the moment." + '\n' +
                                               "Let's go!")

        about_frame = QtGui.QGroupBox(self)
        about_frame.setTitle("Warning!")
        about = QtGui.QVBoxLayout()
        about.addWidget(self.text_about)
        about.addWidget(self.separator_2)
        about.addWidget(self.accept_button)
        about_frame.setLayout(about)

        window_warning.setCentralWidget(about_frame)

        window_warning.resize(window_warning.sizeHint())

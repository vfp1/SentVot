__author__ = 'vfp1'
from PyQt4 import QtGui, QtCore
import os

class Ui_SentVotAboutFile(object):
    def setupUiAbout(self, window_about):
        window_about.setWindowTitle("About SentVot")

        #Setting the Central Widget
        self.centralWidget = QtGui.QWidget(window_about)
        self.centralWidget.setMinimumSize(300, 300)
        self.centralWidget.setGeometry(350, 350, 600, 500)

        #Picture
        self.author_image = QtGui.QLabel()
        self.author_image_pix = QtGui.QPixmap("VictorFPMadrigal.jpeg")
        self.author_image.setPixmap(self.author_image_pix)
        self.author_image.show()

        author_image_frame = QtGui.QGroupBox()
        author_image_frame.setTitle("Victor Pajuelo Madrigal")
        inside_author_image = QtGui.QVBoxLayout()
        inside_author_image.addWidget(self.author_image)
        author_image_frame.setLayout(inside_author_image)

        #Text About
        self.text_about = QtGui.QLabel()
        self.text_about.setText("This is SentVot, an application for mapping" + '\n' +
                                "the feelings towards wetland restoration. It" + '\n' +
                                "has been developed as a tool for the Master thesis" + '\n' +
                                "of the author. This tool collects information on" + '\n' +
                                "the feelings of the user towards wetland restoration." + '\n' +
                                "SentVot stands for 'Sentiment Votlendi' (wetland in" + '\n' +
                                "icelandic). This tool is written entirely in Python" + '\n' +
                                "under PyQt and PyQgis wrappers, which means that this is" + '\n' +
                                "free software ('Free' as in freedom). Also, the code is" + '\n' +
                                "open and I am happy to share it with you. Send an email to" + '\n' +
                                "vfp1@hi.is if you want it. Use the Helpfile if" + '\n' +
                                "you have any trouble, and be patient, this is my very" + '\n' +
                                "first software of this kind :)")
        self.separator_1 = QtGui.QFrame()
        self.separator_1.setFrameStyle(QtGui.QFrame.HLine)
        self.author_font = QtGui.QFont()
        self.author_font.setPointSize(15)
        self.author_font.setBold(True)
        self.about_author = QtGui.QLabel("About the author")
        self.about_author.setFont(self.author_font)
        self.about_author_text = QtGui.QLabel()
        self.about_author_text.setText("Victor Pajuelo Madrigal is a Master student" + '\n' +
                                       "at Haskoli Islands. He is focusing on innovative" + '\n' +
                                       "approaches to wetland restoration. Former philosophy" + '\n' +
                                       "student, DIY enthusiast and self-taught programmer, he" + '\n' +
                                       "expects you to have fun with this app!")
        self.separator_2 = QtGui.QFrame()
        self.separator_2.setFrameStyle(QtGui.QFrame.HLine)
        self.accept_button = QtGui.QPushButton("Let's start mapping")

        about_frame = QtGui.QGroupBox(self)
        about_frame.setTitle("What is this?")
        about = QtGui.QVBoxLayout()
        about.addWidget(self.text_about)
        about.addWidget(self.separator_1)
        about.addWidget(self.about_author)
        about.addWidget(self.about_author_text)
        about.addWidget(self.separator_2)
        about.addWidget(self.accept_button)
        about_frame.setLayout(about)

        #Setting Splitters
        split = QtGui.QSplitter(self.centralWidget)

        split_left = QtGui.QSplitter(QtCore.Qt.Horizontal)
        split_right = QtGui.QSplitter(QtCore.Qt.Horizontal)

        split_left.addWidget(author_image_frame)
        split_right.addWidget(about_frame)

        split.addWidget(split_left)
        split.addWidget(split_right)

        window_about.setCentralWidget(split)

        window_about.resize(window_about.sizeHint())




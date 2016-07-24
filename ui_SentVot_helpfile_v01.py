__author__ = 'vfp1'

from PyQt4 import QtGui, QtCore

class Ui_SentVotHelpFile(object):
    def setupUiHelp(self, window_help):
        window_help.setWindowTitle("SentVot Help")

        #Setting the Central Widget
        self.centralWidget = QtGui.QWidget(window_help)
        self.centralWidget.setMinimumSize(400, 300)
        self.centralWidget.setGeometry(350, 350, 400, 300)
        window_help.setCentralWidget(self.centralWidget)

        window_help.resize(window_help.sizeHint())




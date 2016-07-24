__author__ = 'vfp1'

from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Ui_SentVot(object):
    def setupUi(self, window):
        window.setWindowTitle("SentVot: Wetland Sentiment Analysis")

        #Setting the Central Widget
        self.centralWidget = QtGui.QWidget(window)
        self.centralWidget.setMinimumSize(800, 600)
        window.setCentralWidget(self.centralWidget)

        #Setting the Main Menu
        self.menubar = window.menuBar()
        self.aboutMenu = self.menubar.addMenu('&About SentVot')

        #Contents of the Main Menu
        self.helpAction = QtGui.QAction('&Open the Help File', window)
        self.helpAction.setShortcut("Ctrl+H")
        self.helpAction.setStatusTip("Opens the SentVot Helpfile")
        self.helpAction.setCheckable(True)
        self.aboutMenu.addAction(self.helpAction)

        self.aboutAction = QtGui.QAction('&About SentVot', window)
        self.aboutAction.setShortcut("Ctrl+A")
        self.aboutAction.setStatusTip("About SentVot software")
        self.aboutAction.setCheckable(True)
        self.aboutMenu.addAction(self.aboutAction)

        self.closeAction = QtGui.QAction('&Close SentVot', window)
        self.closeAction.setShortcut("Ctrl+C")
        self.closeAction.setStatusTip("Closes the SentVot Application")
        self.closeAction.setCheckable(True)
        self.aboutMenu.addAction(self.closeAction)

        #Setting the Layer Menu
        self.layerMenu = self.menubar.addMenu('&Add Custom Layers')

        #Contents of the Main Menu
        self.rasterAction = QtGui.QAction('&Load a raster file', window)
        self.rasterAction.setShortcut("Ctrl+R")
        self.rasterAction.setStatusTip("Loads a Raster File")
        self.rasterAction.setCheckable(True)
        self.layerMenu.addAction(self.rasterAction)

        self.vectorAction = QtGui.QAction('&Load a Vector File', window)
        self.vectorAction.setShortcut("Ctrl+V")
        self.vectorAction.setStatusTip("Loads a Vector File")
        self.vectorAction.setCheckable(True)
        self.layerMenu.addAction(self.vectorAction)

        #Setting the toolbar
        self.toolBar = QtGui.QToolBar(window)
        window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        #Setting actions in toolbar
            # pan
        icon = QtGui.QIcon("pan.svg")
        self.actionPan = QtGui.QAction(icon, "Pan", window)
        self.actionPan.setShortcut("C")
        self.actionPan.setStatusTip("Panning the map")
        self.toolBar.addAction(self.actionPan)

            # user
        icon = QtGui.QIcon("user.png")
        self.actionUser = QtGui.QAction(icon, "Start Mapping", window)
        self.actionUser.setShortcut("Ctrl+S")
        self.actionUser.setStatusTip("Start Mapping")
        self.actionUser.setCheckable(True)
        self.toolBar.addAction(self.actionUser)

            # restore
        icon = QtGui.QIcon("green.png")
        self.actionGreen = QtGui.QAction(icon, "Suitable for Restoration", window)
        self.actionGreen.setShortcut("G")
        self.actionGreen.setCheckable(True)
        self.actionGreen.setEnabled(False)
        self.actionGreen.setStatusTip("Draw areas which are good for Restoration")
        self.toolBar.addAction(self.actionGreen)

             # not restore
        icon = QtGui.QIcon("red.png")
        self.actionRed = QtGui.QAction(icon, "Not suitable for Restoration", window)
        self.actionRed.setShortcut("R")
        self.actionRed.setCheckable(True)
        self.actionRed.setEnabled(False)
        self.actionRed.setStatusTip("Draw areas which are not good for Restoration")
        self.toolBar.addAction(self.actionRed)

            # select
        icon = QtGui.QIcon("select.png")
        self.actionSelect = QtGui.QAction(icon, "Select Drawing", window)
        self.actionSelect.setShortcut("Ctrl+S")
        self.actionSelect.setCheckable(True)
        self.actionSelect.setEnabled(False)
        self.actionSelect.setStatusTip("Select drawings")
        self.toolBar.addAction(self.actionSelect)

            # erase
        icon = QtGui.QIcon("erase.png")
        self.actionErase = QtGui.QAction(icon, "Erase Selected Drawing", window)
        self.actionErase.setShortcut("Ctrl+E")
        self.actionErase.setCheckable(True)
        self.actionErase.setEnabled(False)
        self.actionErase.setStatusTip("Erase the drawing")
        self.toolBar.addAction(self.actionErase)

        #Adding actions to toolbar
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUser)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGreen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRed)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionErase)
        self.toolBar.addSeparator()

        self.separator_space = QtGui.QSpacerItem(10, 10)
        self.new_code_label = QtGui.QLabel("Name of Interviewee:")
        self.new_code_font = QtGui.QFont()
        self.new_code_font.setItalic(True)
        self.new_code = QtGui.QLabel("None Yet")
        self.new_code.setFont(self.new_code_font)
        self.inner_split = QtGui.QFrame()
        self.inner_split.setFrameStyle(QtGui.QFrame.HLine)
        #Green
        self.code_description_label_green = QtGui.QLabel("Why the area selected is good for restoration?")
        #self.options_green = QtGui.QComboBox()
        self.options_green = QtGui.QTextEdit("Place your reason here")
        #self.options_green.addItem("Slope")
        #self.options_green.addItem("Water")
        #self.options_green.addItem("Not used land")
        self.comments_green = QtGui.QLabel("Place any comment in the area drawn below")
        self.comments_green_font = QtGui.QFont()
        self.comments_green_font.setItalic(True)
        self.comments_green.setFont(self.comments_green_font)
        self.code_description_green = QtGui.QTextEdit("None")
        self.code_description_label_green.setEnabled(False)
        self.options_green.setEnabled(False)
        self.options_green.setEnabled(False)
        self.options_green.setEnabled(False)
        self.comments_green.setEnabled(False)
        self.code_description_green.setEnabled(False)
        self.save_polygon_green = QtGui.QPushButton("Save Drawing")
        self.save_polygon_green.setCheckable(True)
        self.save_polygon_green.setEnabled(False)
        self.save_polygon_green.clicked.connect(self.green_attributes)
        #Red
        self.code_description_label_red = QtGui.QLabel("Why the area selected is bad for restoration?")
        #self.options_red = QtGui.QComboBox()
        self.options_red = QtGui.QTextEdit("Place your reason here")
        #self.options_red.addItem("Agriculture")
        #self.options_red.addItem("Cultural Value")
        #self.options_red.addItem("Not good conditions")
        self.comments_red = QtGui.QLabel("Place any comment in the area drawn below")
        self.comments_red_font = QtGui.QFont()
        self.comments_red_font.setItalic(True)
        self.comments_red.setFont(self.comments_green_font)
        self.code_description_red = QtGui.QTextEdit("None")
        self.inner_split_dash = QtGui.QFrame()
        self.inner_split_dash.setFrameStyle(QtGui.QFrame.HLine)
        self.inner_split_dash.setFrameShadow(QtGui.QFrame.Sunken)
        self.code_description_label_red.setEnabled(False)
        self.options_red.setEnabled(False)
        self.options_red.setEnabled(False)
        self.options_red.setEnabled(False)
        self.comments_red.setEnabled(False)
        self.code_description_red.setEnabled(False)
        self.save_polygon_red = QtGui.QPushButton("Save Drawing")
        self.save_polygon_red.setCheckable(True)
        self.save_polygon_red.setEnabled(False)
        self.save_polygon_red.clicked.connect(self.red_attributes)


        #Save
        self.inner_split2 = QtGui.QFrame()
        self.inner_split2.setFrameStyle(QtGui.QFrame.HLine)
        self.trans_layer = QtGui.QLabel("Layer Transparency:")
        self.comments_trans = QtGui.QLabel("Set the transparency of the layer" + '\n' +
                                           "at your convenience to help you drawing")
        self.comments_trans_font = QtGui.QFont()
        self.comments_trans_font.setItalic(True)
        self.comments_trans.setFont(self.comments_trans_font)
        self.trans_slider = QSlider(Qt.Horizontal)
        self.trans_slider.setMinimum(0)
        self.trans_slider.setMaximum(100)
        self.trans_slider.setValue(50)
        self.trans_slider.valueChanged.connect(self.transparency)


        self.inner_split3 = QtGui.QFrame()
        self.inner_split3.setFrameStyle(QtGui.QFrame.HLine)
        self.request_save = QtGui.QPushButton("Export the Map")
        self.request_save.clicked.connect(self.export)

        window.resize(window.sizeHint())




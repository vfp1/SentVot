__author__ = 'Victor'
from ui_SentVot_v01 import Ui_SentVot
from ui_SentVot_helpfile_v01 import Ui_SentVotHelpFile
from ui_SentVot_aboutfile_v01 import Ui_SentVotAboutFile
from ui_SentVot_warning_v01 import Ui_SentVotWarning

from SentVot_constants_v01 import *

from SentVot_tools import SentVotLocker
from SentVot_tools import SentVotLockerName
from SentVot_tools import PanTool
from SentVot_tools import GreenTool
from SentVot_tools import RedTool
from SentVot_tools import SelectTool
from SentVot_tools import DeleteTool
from SentVot_tools import SentVotAboutFile
from SentVot_tools import SentVotHelpFile

import os, os.path, sys, time

from PyQt4 import QtCore, QtGui
from qgis.utils import *
from qgis.core import *
from qgis.gui import *
from qgis.server import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SentVot(QMainWindow, Ui_SentVot):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)

        self.connect(self.helpAction, SIGNAL("triggered()"), self.help_file)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.about_file)
        self.connect(self.closeAction, SIGNAL("triggered()"), self.close_application)
        self.connect(self.actionPan, SIGNAL("triggered()"), self.pan)
        self.connect(self.actionUser, SIGNAL("triggered()"), self.dataBase)
        self.connect(self.actionGreen, SIGNAL("triggered()"), self.green)
        self.connect(self.actionRed, SIGNAL("triggered()"), self.red)
        self.connect(self.actionSelect, SIGNAL("triggered()"), self.select)
        self.connect(self.actionErase, SIGNAL("triggered()"), self.erase)
        self.connect(self.rasterAction, SIGNAL("triggered()"), self.open_raster)
        self.connect(self.vectorAction, SIGNAL("triggered()"), self.open_vector)

        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.useImageToRender(False)
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapCanvas.show()
        layout = QVBoxLayout()
        self.layers = []
        self.points = []

        layout.addWidget(self.mapCanvas)
        self.centralWidget.setLayout(layout)

        # -- Load predetermined layers
        fileinfo5 = QFileInfo("is50v_samgongur_linur_24122014.shp")
        vlayer5 = QgsVectorLayer("is50v_samgongur_linur_24122014.shp", fileinfo5.fileName(), "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(vlayer5)
        vl5 = QgsMapCanvasLayer(vlayer5)
        self.layers.append(vl5)
        symbols5 = vlayer5.rendererV2().symbols()
        symbol5 = symbols5[0]
        symbol5.setColor(QColor.fromRgb(0,0,0))

        fileinfo6 = QFileInfo("Skurdir.shp")
        vlayer6 = QgsVectorLayer("Skurdir.shp", fileinfo6.fileName(), "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(vlayer6)
        vl6 = QgsMapCanvasLayer(vlayer6)
        self.layers.append(vl6)
        symbols6 = vlayer6.rendererV2().symbols()
        symbol6 = symbols6[0]
        symbol6.setColor(QColor.fromRgb(128,0,0))

        fileinfo = QFileInfo("e355-1.tif")
        rlayer = QgsRasterLayer("e355-1.tif", fileinfo.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        self.mapCanvas.setExtent(rlayer.extent())
        rl = QgsMapCanvasLayer(rlayer)
        self.layers.append(rl)

        fileinfo2 = QFileInfo("e355-2.tif")
        rlayer2 = QgsRasterLayer("e355-2.tif", fileinfo2.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer2)
        self.mapCanvas.setExtent(rlayer2.extent())
        rl2 = QgsMapCanvasLayer(rlayer2)
        self.layers.append(rl2)

        fileinfo3 = QFileInfo("e345-3.tif")
        rlayer3 = QgsRasterLayer("e345-3.tif", fileinfo3.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer3)
        rl3 = QgsMapCanvasLayer(rlayer3)
        self.layers.append(rl3)

        fileinfo4 = QFileInfo("e345-4.tif")
        rlayer4 = QgsRasterLayer("e345-4.tif", fileinfo4.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer4)
        rl4 = QgsMapCanvasLayer(rlayer4)
        self.layers.append(rl4)

        fileinfo7 = QFileInfo("ism30.tif")
        rlayer7 = QgsRasterLayer("ism30.tif", fileinfo7.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer7)
        rl7 = QgsMapCanvasLayer(rlayer7)
        self.layers.append(rl7)

        fileinfo = QFileInfo("e355-1.tif")
        rlayer = QgsRasterLayer("e355-1.tif", fileinfo.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        self.mapCanvas.setExtent(rlayer.extent())
        rl = QgsMapCanvasLayer(rlayer)
        self.layers.append(rl)

        fileinfo2 = QFileInfo("e355-2.tif")
        rlayer2 = QgsRasterLayer("e355-2.tif", fileinfo2.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer2)
        self.mapCanvas.setExtent(rlayer2.extent())
        rl2 = QgsMapCanvasLayer(rlayer2)
        self.layers.append(rl2)

        fileinfo3 = QFileInfo("e345-3.tif")
        rlayer3 = QgsRasterLayer("e345-3.tif", fileinfo3.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer3)
        rl3 = QgsMapCanvasLayer(rlayer3)
        self.layers.append(rl3)

        fileinfo4 = QFileInfo("e345-4.tif")
        rlayer4 = QgsRasterLayer("e345-4.tif", fileinfo4.fileName())
        QgsMapLayerRegistry.instance().addMapLayer(rlayer4)
        rl4 = QgsMapCanvasLayer(rlayer4)
        self.layers.append(rl4)

        fileinfo5 = QFileInfo("is50v_samgongur_linur_24122014.shp")
        vlayer5 = QgsVectorLayer("is50v_samgongur_linur_24122014.shp", fileinfo5.fileName(), "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(vlayer5)
        vl5 = QgsMapCanvasLayer(vlayer5)
        self.layers.append(vl5)
        symbols5 = vlayer5.rendererV2().symbols()
        symbol5 = symbols5[0]
        symbol5.setColor(QColor.fromRgb(0,0,0))

        fileinfo6 = QFileInfo("Skurdir.shp")
        vlayer6 = QgsVectorLayer("Skurdir.shp", fileinfo6.fileName(), "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(vlayer6)
        vl6 = QgsMapCanvasLayer(vlayer6)
        self.layers.append(vl6)
        symbols6 = vlayer6.rendererV2().symbols()
        symbol6 = symbols6[0]
        symbol6.setColor(QColor.fromRgb(128,0,0))

        self.mapCanvas.setLayerSet(self.layers)
        self.mapCanvas.show()


        # -- Setting group boxes: Coding Manager
        coding_manager = QtGui.QGroupBox()
        coding_manager.setTitle("Layer Manager")
        inside_coding_manager = QtGui.QVBoxLayout()
        inside_coding_manager.addWidget(self.new_code_label)
        inside_coding_manager.addWidget(self.new_code)
        inside_coding_manager.addSpacerItem(self.separator_space)
        inside_coding_manager.addWidget(self.inner_split)
        #Green
        inside_coding_manager.addWidget(self.code_description_label_green)
        inside_coding_manager.addWidget(self.options_green)
        inside_coding_manager.addWidget(self.comments_green)
        inside_coding_manager.addWidget(self.code_description_green)
        inside_coding_manager.addWidget(self.save_polygon_green)
        inside_coding_manager.addWidget(self.inner_split_dash)
        #Red
        inside_coding_manager.addWidget(self.code_description_label_red)
        inside_coding_manager.addWidget(self.options_red)
        inside_coding_manager.addWidget(self.comments_red)
        inside_coding_manager.addWidget(self.code_description_red)
        inside_coding_manager.addWidget(self.save_polygon_red)
        #Save
        inside_coding_manager.addWidget(self.inner_split2)
        inside_coding_manager.addWidget(self.trans_layer)
        inside_coding_manager.addWidget(self.comments_trans)
        inside_coding_manager.addWidget(self.trans_slider)
        inside_coding_manager.addWidget(self.inner_split3)
        inside_coding_manager.addWidget(self.request_save)
        coding_manager.setLayout(inside_coding_manager)

        # -- Setting splitters
        split_main = QtGui.QSplitter()
        splitter_left = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter_right = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter_extreme_right = QtGui.QSplitter(QtCore.Qt.Horizontal)

        # -- Adding the widgets
        splitter_left.addWidget(self.mapCanvas)
        splitter_extreme_right.addWidget(coding_manager)
        split_main.addWidget(splitter_left)
        split_main.addWidget(splitter_right)
        split_main.addWidget(splitter_extreme_right)

        self.setCentralWidget(split_main)

        about = SentVotAboutFile()
        about.setGeometry(400, 200, 600, 300)
        about.show()
        about.raise_()

        self.setupDatabase()

    def dataBase(self):
        if not self.actionUser.isChecked():
            self.actionGreen.setChecked(False)
            self.actionRed.setChecked(False)
            self.actionGreen.setEnabled(False)
            self.actionRed.setEnabled(False)
            self.actionSelect.setEnabled(False)
            self.actionErase.setEnabled(False)
        elif self.actionUser.isChecked():
            self.actionGreen.setChecked(False)
            self.actionRed.setChecked(False)
            self.actionGreen.setEnabled(True)
            self.actionRed.setEnabled(True)
            self.actionSelect.setEnabled(True)
            self.actionErase.setEnabled(True)

    def setupMapTools(self): #New method. Set it here and pass it in the main function.
        #Toolbar Implementation
        self.toolPan = QgsMapToolPan(self.mapCanvas)
        self.toolPan.setAction(self.actionPan)

        self.toolGreen = GreenTool(self.mapCanvas, self.polygonLayer,
                                   self.layers, self.actionGreen,
                                   self.options_green, self.options_green,
                                   self.code_description_green,
                                   self.code_description_label_green, self.comments_green, self.code_description_green)
        self.toolGreen.setAction(self.actionGreen)

        self.toolRed = RedTool(self.mapCanvas, self.polygonLayer,
                               self.layers, self.actionRed,
                               self.options_red, self.options_red,
                               self.code_description_red,
                               self.code_description_label_green, self.comments_green, self.code_description_red)
        self.toolRed.setAction(self.actionRed)

        self.toolSelect = SelectTool(self)
        self.toolSelect.setAction(self.actionSelect)

        self.toolErase = DeleteTool(self.mapCanvas, self.polygonLayer, self.layers)
        self.toolErase.setAction(self.actionErase)

    def open_vector(self):
        file = QFileDialog.getOpenFileName(self,
                   "Open Shapefile", ".", "Shapefiles (*.shp)")
        fileinfo = QFileInfo(file)
        self.vlayer = QgsVectorLayer(file, fileinfo.fileName(), "ogr")

        if not self.vlayer.isValid():
          print "Vector Layer is invalid"

        # Add layer to the registry and plotting it in black colour
        QgsMapLayerRegistry.instance().addMapLayer(self.vlayer)
        symbols = self.vlayer.rendererV2().symbols()
        symbol = symbols[0]
        symbol.setColor(QColor.fromRgb(0,0,255))

        # Set extent to the extent of our layer
        self.mapCanvas.setExtent(self.vlayer.extent())

        # Set up the map canvas layer set
        vl = QgsMapCanvasLayer(self.vlayer)
        self.layers.append(vl)
        self.mapCanvas.setLayerSet(self.layers) #Appending layers
        self.mapCanvas.show()

    def open_raster(self):
        file = QFileDialog.getOpenFileName(self,
                   "Open Raster", ".", "TIFF raster data (*.tif)")
        fileinfo = QFileInfo(file)
        self.rlayer = QgsRasterLayer(file, fileinfo.fileName())

        if not self.rlayer.isValid():
          print "Raster Layer is invalid"

        # Add layer to the registry and plotting it in black colour
        QgsMapLayerRegistry.instance().addMapLayer(self.rlayer)

        # Set extent to the extent of our layer
        self.mapCanvas.setExtent(self.rlayer.extent())

        # Set up the map canvas layer set
        rl = QgsMapCanvasLayer(self.rlayer)
        self.layers.append(rl)
        self.mapCanvas.setLayerSet(self.layers) #Appending layers
        self.mapCanvas.show()

    def pan(self):
        self.mapCanvas.setMapTool(self.toolPan)

    def green(self):
        self.actionRed.setChecked(False)
        self.mapCanvas.setMapTool(self.toolGreen)
        self.actionGreen.setChecked(True)

        #Green Enable Attribute Picker
        self.code_description_label_green.setEnabled(True)
        self.options_green.setEnabled(True)
        self.comments_green.setEnabled(True)
        self.code_description_green.setEnabled(True)
        self.save_polygon_green.setEnabled(True)

        #Red Disable Attribute Picker
        self.code_description_label_red.setEnabled(False)
        self.options_red.setEnabled(False)
        self.comments_red.setEnabled(False)
        self.code_description_red.setEnabled(False)

    def green_attributes(self):
        self.polygonLayer.startEditing()
        save_question = QtGui.QMessageBox.question(self, "SentVot: Confirm", "Do you want to save this drawing?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if save_question == QtGui.QMessageBox.Yes:
            self.iter = self.polygonLayer.getFeatures()
            for feature in self.iter:
                self.saved_feature = feature.id()
            print self.saved_feature

            #self.polygonLayer.changeAttributeValue(int(self.saved_feature), 2, str(self.options_green.currentText()))
            self.polygonLayer.changeAttributeValue(int(self.saved_feature), 2, str(self.options_green.toPlainText()))
            self.polygonLayer.changeAttributeValue(int(self.saved_feature), 3, str(self.code_description_green.toPlainText()))
            self.polygonLayer.updateExtents()
            self.polygonLayer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayers([self.polygonLayer])
            self.mapCanvas.setLayerSet(self.layers)
            self.save_polygon_green.setChecked(False)

        elif save_question == QtGui.QMessageBox.No:
            self.polygonLayer.startEditing()
            print "Is Editable?)", self.polygonLayer.isEditable()
            self.iter = self.polygonLayer.getFeatures()
            for feature in self.iter:
                self.saved_feature = feature.id()
            print self.saved_feature
            self.polygonLayer.deleteFeature(self.saved_feature)
            self.polygonLayer.updateExtents()
            self.polygonLayer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayers([self.polygonLayer])
            self.mapCanvas.setLayerSet(self.layers)
            self.mapCanvas.refresh()
            self.save_polygon_green.setChecked(False)
            print "Layer", self.saved_feature, "has been deleted by user"

    def red(self):
        self.actionRed.setChecked(True)
        self.mapCanvas.setMapTool(self.toolRed)
        self.actionGreen.setChecked(False)

        #Green Enable Attribute Picker
        self.code_description_label_green.setEnabled(False)
        self.options_green.setEnabled(False)
        self.comments_green.setEnabled(False)
        self.code_description_green.setEnabled(False)
        self.save_polygon_green.setEnabled(False)

        #Red Disable Attribute Picker
        self.code_description_label_red.setEnabled(True)
        self.options_red.setEnabled(True)
        self.comments_red.setEnabled(True)
        self.code_description_red.setEnabled(True)
        self.save_polygon_red.setEnabled(True)

    def red_attributes(self):
        self.polygonLayer.startEditing()
        save_question = QtGui.QMessageBox.question(self, "SentVot: Confirm", "Do you want to save this drawing?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if save_question == QtGui.QMessageBox.Yes:
            self.iter = self.polygonLayer.getFeatures()
            for feature in self.iter:
                self.saved_feature = feature.id()
            print self.saved_feature

            #self.polygonLayer.changeAttributeValue(int(self.saved_feature), 2, str(self.options_red.currentText()))
            self.polygonLayer.changeAttributeValue(int(self.saved_feature), 2, str(self.options_red.toPlainText()))
            self.polygonLayer.changeAttributeValue(int(self.saved_feature), 3, str(self.code_description_red.toPlainText()))
            self.polygonLayer.updateExtents()
            self.polygonLayer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayers([self.polygonLayer])
            self.mapCanvas.setLayerSet(self.layers)
            self.save_polygon_red.setChecked(False)

        elif save_question == QtGui.QMessageBox.No:
            self.polygonLayer.startEditing()
            print "Is Editable?)", self.polygonLayer.isEditable()
            self.iter = self.polygonLayer.getFeatures()
            for feature in self.iter:
                self.saved_feature = feature.id()
            print self.saved_feature
            self.polygonLayer.deleteFeature(self.saved_feature)
            self.polygonLayer.updateExtents()
            self.polygonLayer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayers([self.polygonLayer])
            self.mapCanvas.setLayerSet(self.layers)
            self.mapCanvas.refresh()
            self.save_polygon_red.setChecked(False)
            print "Layer", self.saved_feature, "has been deleted by user"

    def select(self):
        self.mapCanvas.setMapTool(self.toolSelect)

    def erase(self):
        tool = self.toolErase
        self.mapCanvas.setMapTool(tool)

    def locker(self):
        self.lock = SentVotLocker()
        self.lock.show()

    def locker_name(self):
        self.lock_name = SentVotLockerName()
        self.lock_name.show()

    def help_file(self):
        self.helpfile = SentVotHelpFile()
        self.helpfile.show()

    def about_file(self):
        self.aboutfile = SentVotAboutFile()
        self.aboutfile.show()

    def export(self):
        mainPath = '/home/victor/Dropbox/Thesis/Ubuntu/QGIS Standalone/SentVot/exports/'
        filename = self.user
        imageType = "png"
        imageWidth_mm = 500
        imageHeight_mm = 400
        dpi = 300

        map_settings = self.mapCanvas.mapSettings()
        c = QgsComposition(map_settings)
        c.setPaperSize(500, 400)
        c.setPrintResolution(dpi)

        x, y = 0, 0
        w, h = c.paperWidth(), c.paperHeight()
        composerMap = QgsComposerMap(c, x, y, w, h)
        c.addItem(composerMap)

        dpmm = dpi/25.4
        width = int(dpmm * c.paperWidth())
        height = int(dpmm * c.paperHeight())

        image = QImage(QSize(width, height), QImage.Format_ARGB32)
        image.setDotsPerMeterX(dpmm * 1000)
        image.setDotsPerMeterY(dpmm * 1000)

        imagePainter = QPainter(image)

        c.setPlotStyle(QgsComposition.Print)
        c.renderPage(imagePainter, 0)
        imagePainter.end()

        imageFilename = mainPath + filename + '.' + imageType
        image.save(imageFilename, imageType)
        print "Map Saved by User"

    def setupUser(self):
        #TODO When "Cancel" is pressed the interviewee is still saved
        self.ok = True
        self.user, self.ok = QtGui.QInputDialog.getText(self, 'Sent Vot: User Registration', "Enter your name:")
        print "Name of the interviewee:", self.user

        return self.user

    def setupDatabase(self):
        try: #Raising a try/except for unexpected names
            self.setupUser()

            self.new_code.setText(self.user)
            self.user = str(self.user)

            current_directory = os.path.dirname(os.path.realpath(__file__))
            dbName = os.path.join(current_directory, "database", self.user)

            #TODO Warning if user has been signed in before
            if not os.path.exists(dbName):
                fields = QgsFields()
                fields.append(QgsField("category", QVariant.String)) #Able vs. not able
                fields.append(QgsField("reason", QVariant.String)) #Reason for restoration
                fields.append(QgsField("comment", QVariant.String)) #Comments made on the area drawn

                crs = QgsCoordinateReferenceSystem(3057, QgsCoordinateReferenceSystem.EpsgCrsId)

                writer = QgsVectorFileWriter(dbName, 'utf-8', fields,
                                                 QGis.WKBPolygon, crs, 'SQLite',
                                                 ["SPATIALITE=YES"])

                if writer.hasError() != QgsVectorFileWriter.NoError:
                    print "Error creating SentVot database"

                del writer

            self.polygonLayerSpatialite()
            self.polygonLayer.updateFields()# tell the vector layer to fetch changes from the provider

        except:
            #self.new_code.setText("")
            self.locker_name()
            self.setupDatabase()

    def polygonLayerSpatialite(self):
        self.user = self.new_code.text() #This is quite dirty but works, just inheriting self.user
        self.user_data = str(self.user)+".sqlite"
        print self.user

        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.layer_name = self.user

        uri = QgsDataSourceURI()
        uri.setDatabase(os.path.join(current_directory, "database", self.user_data))
        uri.setDataSource('', self.layer_name, 'GEOMETRY')

        self.polygonLayer = QgsVectorLayer(uri.uri(), self.layer_name, "spatialite")

        QgsMapLayerRegistry.instance().addMapLayer(self.polygonLayer)
        self.layers.append(QgsMapCanvasLayer(self.polygonLayer))

        self.mapCanvas.setLayerSet(self.layers)

        self.layers.reverse()

        self.transparency()

        return self.polygonLayer

    def transparency(self):
        trans = self.trans_slider.value()
        value = 100 - trans
        self.polygonLayer.setLayerTransparency(value)
        self.mapCanvas.refresh()

    def close_application(self):

        choice = QtGui.QMessageBox.question(self, 'Closing SentVot',"Are you sure that you want to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print ("User has left the application")
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()

def main(argv):
    app = QApplication(sys.argv)
    qgis_prefix = "/usr"
    #QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
    QgsApplication.setPrefixPath(qgis_prefix, True)
    QgsApplication.initQgis()
    print QgsApplication.showSettings()

    window = SentVot()
    window.show()
    window.setupMapTools()
    window.raise_()
    #window.loadMap()
    #window.setPanMode()

    retval = app.exec_()
    QgsApplication.exitQgis()
    sys.exit(retval)

if __name__ == "__main__":
    #main(sys.argv)
    main(sys.argv)

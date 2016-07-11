__author__ = 'Victor Francisco Pajuelo Madrigal'
from ui_SentVot_v01 import Ui_SentVot
from ui_SentVot_helpfile_v01 import Ui_SentVotHelpFile
from ui_SentVot_aboutfile_v01 import Ui_SentVotAboutFile
from ui_SentVot_warning_v01 import Ui_SentVotWarning
from ui_SentVot_warning_namev01 import Ui_SentVotWarningName
from SentVot_constants_v01 import *

from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SentVotLocker(QMainWindow, Ui_SentVotWarning):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUiWarning(self)

        self.accept_button.clicked.connect(self.close)

class SentVotLockerName(QMainWindow, Ui_SentVotWarningName):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUiWarningName(self)

        self.accept_button.clicked.connect(self.close)

class PanTool(QgsMapTool):
    def __init__(self, mapCanvas):
        QgsMapTool.__init__(self, mapCanvas)
        self.setCursor(Qt.OpenHandCursor)
        self.dragging = False

    def canvasMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.canvas().panAction(event)

    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragging:
            self.canvas().panActionEnd(event.pos())
            self.dragging = False

class GreenTool(QgsMapToolEmitPoint):
    def __init__(self, mapCanvas, polylayer, layers, actionGreen, optionsgreen,
                 dropdown, comment,
                 codedescriptionlabel, commentsgreen, codedescription):
        QgsMapToolEmitPoint.__init__(self, mapCanvas)
        self.canvas = mapCanvas #This is the QgsMapCanvas this map tool will be part of
        self.polylayer = polylayer #The QgsVectorLayer where the geometry will be added to (this is the drawn_vl)
        self.layers = layers
        self.actionGreen = actionGreen
        self.optionsgreen = optionsgreen
        self.dropdown = dropdown
        self.comment = comment
        self.codedescriptionlabel = codedescriptionlabel
        self.commentsgreen = commentsgreen
        self.codedescription = codedescription

        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(Qt.darkGreen)
        self.rubberband.setWidth(1)
        self.gpoi = []
        self.point = None
        self.points = []

    def canvasPressEvent(self, QgsMapMouseEvent):
        self.point_press = 0
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_press = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        return self.point_press

    def canvasDoubleClickEvent(self, QgsMapMouseEvent):
        self.point_doubleclick = 0
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_doubleclick = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        #self.actionGreen.isChecked(False)
        return self.point_doubleclick

    def canvasMoveEvent(self, QgsMapMouseEvent):
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_move = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

        while self.actionGreen.isChecked() == True:
            if self.point_press != 0:
                self.gpoi.append(self.point_move)
                self.PolygonDrawer()
            if self.point_doubleclick != 0:
                self.gpoi.append(self.gpoi[0]) #Append the first point of the list
                print self.gpoi
                self.savePoly(self.gpoi)
            break

    def PolygonDrawer(self):
        self.points.append(self.point_move)
        self.isEmittingPoint = True
        self.showPoly()

    def showPoly(self):
        self.rubberband.reset(QGis.Polygon)
        for point in self.points[:-1]:
            self.rubberband.addPoint(point, False)
        self.rubberband.addPoint(self.points[-1], True)
        self.rubberband.setOpacity(0.5)
        self.rubberband.show()

    def savePoly(self, points):
        field = self.polylayer.dataProvider().fields()
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPolygon([points]))
        feature.setFields(field)
        feature.setAttribute("category", CATEGORY_RESTORE)
        #feature.setAttribute("reason", str(self.dropdown.currentText()))
        feature.setAttribute("reason", str(self.dropdown.toPlainText()))
        feature.setAttribute("comment", str(self.comment.toPlainText()))
        self.polylayer.dataProvider().addFeatures([feature])

        #Rendering the layers based on Attributes
        symbol_green = QgsFillSymbolV2()
        symbol_green.setColor(QtGui.QColor(34,139,34))
        symbol_red = QgsFillSymbolV2()
        symbol_red.setColor(QtGui.QColor(178,34,34))
        categories = []
        categories.append(QgsRendererCategoryV2("ABLE_RESTORE", symbol_green, CATEGORY_RESTORE))
        categories.append(QgsRendererCategoryV2("NOT_ABLE_RESTORE", symbol_red, CATEGORY_NOT_RESTORE))
        renderer = QgsCategorizedSymbolRendererV2("category", categories)
        renderer.setClassAttribute("category")
        self.polylayer.setRendererV2(renderer)

        self.polylayer.updateExtents()
        self.polylayer.commitChanges()
        QgsMapLayerRegistry.instance().addMapLayers([self.polylayer])
        self.canvas.setLayerSet(self.layers)
        self.polylayer.setSelectedFeatures([feature.id()])

        self.restartPolygonDrawer()
        self.point_press = 0
        self.point_doubleclick = 0
        self.actionGreen.setChecked(False)
        self.actionGreen.isChecked() == False

    def restartPolygonDrawer(self):
        self.canvas.scene().removeItem(self.rubberband)
        self.canvas.refresh()
        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(Qt.darkGreen)
        self.rubberband.setWidth(1)
        self.point = None
        self.points = []
        self.gpoi = []
        self.actionGreen.isChecked() == False

class RedTool(QgsMapToolEmitPoint):
    def __init__(self, mapCanvas, polylayer, layers, actionRed, optionsred,
                 dropdown, comment,
                 codedescriptionlabel, commentsred, codedescription):
        QgsMapToolEmitPoint.__init__(self, mapCanvas)
        self.canvas = mapCanvas #This is the QgsMapCanvas this map tool will be part of
        self.polylayer = polylayer #The QgsVectorLayer where the geometry will be added to (this is the drawn_vl)
        self.layers = layers
        self.actionRed = actionRed
        self.optionsred = optionsred
        self.dropdown = dropdown
        self.comment = comment
        self.codedescriptionlabel = codedescriptionlabel
        self.commentsred = commentsred
        self.codedescription = codedescription

        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(Qt.darkRed)
        self.rubberband.setWidth(1)
        self.gpoi = []
        self.point = None
        self.points = []

    def canvasPressEvent(self, QgsMapMouseEvent):
        self.point_press = 0
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_press = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        return self.point_press

    def canvasDoubleClickEvent(self, QgsMapMouseEvent):
        self.point_doubleclick = 0
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_doubleclick = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        #self.actionGreen.isChecked(False)
        return self.point_doubleclick

    def canvasMoveEvent(self, QgsMapMouseEvent):
        x = QgsMapMouseEvent.pos().x()
        y = QgsMapMouseEvent.pos().y()
        self.point_move = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

        while self.actionRed.isChecked() == True:
            if self.point_press != 0:
                self.gpoi.append(self.point_move)
                self.PolygonDrawer()
            if self.point_doubleclick != 0:
                self.gpoi.append(self.gpoi[0]) #Append the first point of the list
                print self.gpoi
                self.savePoly(self.gpoi)
            break

    def PolygonDrawer(self):
        self.points.append(self.point_move)
        self.isEmittingPoint = True
        self.showPoly()

    def showPoly(self):
        self.rubberband.reset(QGis.Polygon)
        for point in self.points[:-1]:
            self.rubberband.addPoint(point, False)
        self.rubberband.addPoint(self.points[-1], True)
        self.rubberband.setOpacity(0.5)
        self.rubberband.show()

    def savePoly(self, points):
        field = self.polylayer.dataProvider().fields()
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPolygon([points]))
        feature.setFields(field)
        feature.setAttribute("category", CATEGORY_NOT_RESTORE)
        #feature.setAttribute("reason", str(self.dropdown.currentText()))
        feature.setAttribute("reason", str(self.dropdown.toPlainText()))
        feature.setAttribute("comment", str(self.comment.toPlainText()))
        self.polylayer.dataProvider().addFeatures([feature])

        #Rendering the layers based on Attributes
        symbol_green = QgsFillSymbolV2()
        symbol_green.setColor(QtGui.QColor(34,139,34))
        symbol_red = QgsFillSymbolV2()
        symbol_red.setColor(QtGui.QColor(178,34,34))
        categories = []
        categories.append(QgsRendererCategoryV2("ABLE_RESTORE", symbol_green, CATEGORY_RESTORE))
        categories.append(QgsRendererCategoryV2("NOT_ABLE_RESTORE", symbol_red, CATEGORY_NOT_RESTORE))
        renderer = QgsCategorizedSymbolRendererV2("category", categories)
        renderer.setClassAttribute("category")
        self.polylayer.setRendererV2(renderer)

        self.polylayer.updateExtents()
        self.polylayer.commitChanges()
        QgsMapLayerRegistry.instance().addMapLayers([self.polylayer])
        self.canvas.setLayerSet(self.layers)
        self.polylayer.setSelectedFeatures([feature.id()])

        self.restartPolygonDrawer()
        self.point_press = 0
        self.point_doubleclick = 0
        self.actionRed.setChecked(False)
        self.actionRed.isChecked() == False

    def restartPolygonDrawer(self):
        self.canvas.scene().removeItem(self.rubberband)
        self.canvas.refresh()
        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(Qt.darkRed)
        self.rubberband.setWidth(1)
        self.point = None
        self.points = []
        self.gpoi = []
        self.actionRed.isChecked() == False

class SelectTool(QgsMapToolIdentify):
    def __init__(self, window):
        QgsMapToolIdentify.__init__(self, window.mapCanvas)
        self.map = window
        self.setCursor(Qt.ArrowCursor)

    def canvasReleaseEvent(self, event):
        found_features = self.identify(event.x(), event.y(),
                                       self.TopDownStopAtFirst,
                                       self.VectorLayer)
        if len(found_features) > 0:
            vlayer = found_features[0].mLayer
            feature = found_features[0].mFeature
            if event.modifiers() & Qt.ShiftModifier:
                vlayer.select(feature.id())
                print vlayer
            else:
                vlayer.setSelectedFeatures([feature.id()])
                print vlayer
        else:
            self.map.polygonLayer.removeSelection()

class DeleteTool(QgsMapToolIdentify):
    def __init__(self, canvas, layer, layers):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.feature = None
        self.polygonLayer = layer
        self.layers = layers
        self.setCursor(Qt.CrossCursor)

    def transformCoordinates(self, screenPt):
        return (self.toMapCoordinates(screenPt),
                self.toLayerCoordinates(self.polygonLayer, screenPt))

    def calcTolerance(self, pos):
        pt1 = QPoint(pos.x(), pos.y())
        pt2 = QPoint(pos.x() + 10, pos.y())

        mapPt1,layerPt1 = self.transformCoordinates(pt1)
        mapPt2,layerPt2 = self.transformCoordinates(pt2)
        tolerance = layerPt2.x() - layerPt1.x()

        return tolerance

    def findFeatureAt(self, pos, excludeFeature=None):
        mapfeat, layerfeat = self.transformCoordinates(pos)
        tolerance = self.calcTolerance(pos)
        searchRect = QgsRectangle(layerfeat.x() - tolerance,
                                  layerfeat.y() - tolerance,
                                  layerfeat.x() + tolerance,
                                  layerfeat.y() + tolerance)

        request = QgsFeatureRequest()
        request.setFilterRect(searchRect)
        request.setFlags(QgsFeatureRequest.ExactIntersect)

        for feature in self.polygonLayer.getFeatures(request):
            if excludeFeature != None:
                if feature.id() == excludeFeature.id():
                    continue
            return feature

        return None

    def canvasPressEvent(self, event):
        self.feature = self.findFeatureAt(event.pos())

    def popup_warning(self):
        self.delete = QtGui.QMessageBox(QtGui.QMessageBox.Question, "SentVot: Confirm", "Are you sure that you want to delete this drawing?" + '\n' + "Changes are not reversible", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
        self.delete.setIcon(QMessageBox.Warning)
        self.delete.show()
        result = self.delete.exec_()
        if result == QtGui.QMessageBox.Yes:
            self.polygonLayer.startEditing()
            print "Is Editable?)", self.polygonLayer.isEditable()
            f = int(self.feature.id())
            self.polygonLayer.deleteFeature(f)
            self.polygonLayer.updateExtents()
            self.polygonLayer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayers([self.polygonLayer])
            self.canvas.setLayerSet(self.layers)
            self.canvas.refresh()
            print "Layer", f, "has been deleted by user"
        elif result == QtGui.QMessageBox.No:
            print "User has not deleted anything"
            pass

    def canvasReleaseEvent(self, event):
        feature = self.findFeatureAt(event.pos())
        if feature != None and feature.id() == self.feature.id():
            self.popup_warning()

class SentVotAboutFile(QMainWindow, Ui_SentVotAboutFile):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUiAbout(self)

        self.accept_button.clicked.connect(self.close)

class SentVotHelpFile(QMainWindow, Ui_SentVotHelpFile):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUiHelp(self)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree.ui'
#
# Created: Fri Mar 13 10:51:54 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Dialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui.setupUi(self)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(287, 398)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 271, 381))
        self.treeWidget.setObjectName("treeWidget")
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(item)
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item = QtGui.QTreeWidgetItem(self.treeWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "Transportation Demand Modeling", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Dialog", "Network / GIS", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Dialog", "Zone / Taz Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("Dialog", "Centroids", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, QtGui.QApplication.translate("Dialog", "Internal", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(0, QtGui.QApplication.translate("Dialog", "External", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Road Network", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).child(0).setText(0, QtGui.QApplication.translate("Dialog", "Centroid Connectors", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).child(1).setText(0, QtGui.QApplication.translate("Dialog", "Transit Network", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Non Motorized Vehicles", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Dialog", "Trip Generation", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Dialog", "ITE Method", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("Dialog", "QRM Method", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Balance", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("Dialog", "Other Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("Dialog", "Trip Distribution", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("Dialog", "Gravity Model", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(1).setText(0, QtGui.QApplication.translate("Dialog", "Gravity Application", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Friction Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(3).setText(0, QtGui.QApplication.translate("Dialog", "Impedance Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("Dialog", "External Trip Estimation", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).setText(0, QtGui.QApplication.translate("Dialog", "Mode Choice", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).child(0).setText(0, QtGui.QApplication.translate("Dialog", "Logit", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).child(1).setText(0, QtGui.QApplication.translate("Dialog", "Incremental Logit", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Model Coefficients", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(5).setText(0, QtGui.QApplication.translate("Dialog", "Vehicle Occupancy", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(6).setText(0, QtGui.QApplication.translate("Dialog", "Time of Day Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(7).setText(0, QtGui.QApplication.translate("Dialog", "Trip Assignment", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(7).child(0).setText(0, QtGui.QApplication.translate("Dialog", "User Equilibrium", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(7).child(1).setText(0, QtGui.QApplication.translate("Dialog", "System Equilibrium", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(7).child(2).setText(0, QtGui.QApplication.translate("Dialog", "Capacity Constraints", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(8).setText(0, QtGui.QApplication.translate("Dialog", "Highway Capacity Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(9).setText(0, QtGui.QApplication.translate("Dialog", "Highway and Spacing Density", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Ui_Dialog()
    myapp.show()
    sys.exit(app.exec_())


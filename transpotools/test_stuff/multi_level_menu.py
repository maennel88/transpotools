# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_level_menu.ui'
#
# Created: Tue Aug  4 16:25:54 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuLevel_1 = QtGui.QMenu(self.menubar)
        self.menuLevel_1.setObjectName("menuLevel_1")
        self.menuLevel_2 = QtGui.QMenu(self.menuLevel_1)
        self.menuLevel_2.setObjectName("menuLevel_2")
        self.menuLevel_3_a = QtGui.QMenu(self.menuLevel_2)
        self.menuLevel_3_a.setObjectName("menuLevel_3_a")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLevel_2_a = QtGui.QAction(MainWindow)
        self.actionLevel_2_a.setObjectName("actionLevel_2_a")
        self.actionLevel_3_b = QtGui.QAction(MainWindow)
        self.actionLevel_3_b.setObjectName("actionLevel_3_b")
        self.actionLevel_4_a = QtGui.QAction(MainWindow)
        self.actionLevel_4_a.setObjectName("actionLevel_4_a")
        self.menuLevel_3_a.addAction(self.actionLevel_4_a)
        self.menuLevel_2.addSeparator()
        self.menuLevel_2.addSeparator()
        self.menuLevel_2.addAction(self.menuLevel_3_a.menuAction())
        self.menuLevel_2.addAction(self.actionLevel_3_b)
        self.menuLevel_1.addAction(self.menuLevel_2.menuAction())
        self.menuLevel_1.addAction(self.actionLevel_2_a)
        self.menubar.addAction(self.menuLevel_1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLevel_1.setTitle(QtGui.QApplication.translate("MainWindow", "level 1", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLevel_2.setTitle(QtGui.QApplication.translate("MainWindow", "Level 2.a", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLevel_3_a.setTitle(QtGui.QApplication.translate("MainWindow", "Level 3.a", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLevel_2_a.setText(QtGui.QApplication.translate("MainWindow", "level 2.b", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLevel_3_b.setText(QtGui.QApplication.translate("MainWindow", "Level 3.b", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLevel_4_a.setText(QtGui.QApplication.translate("MainWindow", "Level 4.a", None, QtGui.QApplication.UnicodeUTF8))


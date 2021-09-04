# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Laptop\OneDrive\Documents\Python\Pyside QT\clculator_gui.ui'
#
# Created: Fri Nov  6 21:05:33 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.horizontalLayout.addWidget(self.lineEdit3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonClear = QtGui.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout_2.addWidget(self.buttonClear)
        self.buttonCalc = QtGui.QPushButton(self.centralwidget)
        self.buttonCalc.setObjectName("buttonCalc")
        self.horizontalLayout_2.addWidget(self.buttonCalc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL("clicked()"), self.lineEdit1.clear)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL("clicked()"), self.lineEdit2.clear)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL("clicked()"), self.lineEdit3.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit1.setToolTip(QtGui.QApplication.translate("MainWindow", "First Number", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit2.setToolTip(QtGui.QApplication.translate("MainWindow", "Second number", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit3.setToolTip(QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClear.setStatusTip(QtGui.QApplication.translate("MainWindow", "Clear All the Boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCalc.setStatusTip(QtGui.QApplication.translate("MainWindow", "Calculate the Result", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCalc.setText(QtGui.QApplication.translate("MainWindow", "Calculate", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


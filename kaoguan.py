# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kaoguan.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import res
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QApplication, QHBoxLayout, QLabel,QDialog
from PyQt5.QtCore import QResource
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 20, 201, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
#        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
#        self.graphicsView.setAutoFillBackground(True)
#        self.graphicsView.setObjectName("graphicsView")
#        self.horizontalLayout.addWidget(self.graphicsView)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget,pixmap=pmap1))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 510, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 450, 181, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(10.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 310, 221, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 570, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.doubleSpinBox.raise_()
        self.formLayoutWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.comboBox.raise_()
#        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 26))
        self.menubar.setObjectName("menubar")
#        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "确认评分"))
        self.label_3.setText(_translate("MainWindow", "考试科目："))
        self.label.setText(_translate("MainWindow", "考生姓名："))
        self.label_2.setText(_translate("MainWindow", "准考证号："))
        self.pushButton_2.setText(_translate("MainWindow", "申请重新评分"))
        self.comboBox.setItemText(0, _translate("MainWindow", "考官1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "考官2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "考官3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "考官4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "考官5"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kaoguandialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
#import res
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QApplication, QHBoxLayout, QLabel,QDialog
from PyQt5.QtCore import QResource
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 692)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 460, 181, 50))
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
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 320, 211, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_6)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 580, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 30, 201, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView_2.setAutoFillBackground(True)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 520, 181, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "考试科目："))
        self.label_5.setText(_translate("Dialog", "考生姓名："))
        self.label_6.setText(_translate("Dialog", "准考证号："))
        self.pushButton_2.setText(_translate("Dialog", "申请重新评分"))
        self.comboBox.setItemText(0, _translate("Dialog", "考官1"))
        self.comboBox.setItemText(1, _translate("Dialog", "考官2"))
        self.comboBox.setItemText(2, _translate("Dialog", "考官3"))
        self.comboBox.setItemText(3, _translate("Dialog", "考官4"))
        self.comboBox.setItemText(4, _translate("Dialog", "考官5"))
        self.pushButton.setText(_translate("Dialog", "确认评分"))

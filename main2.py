# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import res
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QApplication, QHBoxLayout, QLabel,QDialog
from PyQt5.QtCore import QResource
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import kaoguan


class Ui_MainWindow2(QDialog):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(928, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 470, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 30, 841, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #考官1
        self.graphicsView = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
#        self.graphicsView.add
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 20, 671, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget,pixmap=pmap1))
        #the end
        self.horizontalLayout.addWidget(self.graphicsView)

        #考官2
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_2.setAutoFillBackground(True)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(185, 20, 671, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_2)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget_2,pixmap=pmap1))
        self.horizontalLayout.addWidget(self.graphicsView_2)
        #考官3
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_4.setAutoFillBackground(True)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(365, 20, 671, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_3)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget_3,pixmap=pmap1))
        self.horizontalLayout.addWidget(self.graphicsView_4)
        #考官4
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_5.setAutoFillBackground(True)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(545, 20, 671, 221))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_4)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget_4,pixmap=pmap1))
        self.horizontalLayout.addWidget(self.graphicsView_5)
        #考官5
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_3.setAutoFillBackground(True)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(725, 20, 671, 221))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_5)
        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget_5,pixmap=pmap1))
        self.horizontalLayout.addWidget(self.graphicsView_3)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 370, 841, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
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
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(10.0)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setMaximum(10.0)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_4)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setMaximum(10.0)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_3)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_5.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setMaximum(10.0)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(39, 240, 841, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 310, 841, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_4.addWidget(self.checkBox_5, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.checkBox_4, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.checkBox_3, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2, 0, QtCore.Qt.AlignHCenter)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox, 0, QtCore.Qt.AlignHCenter)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

#        self.pushButton.setVisible(True)
        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
#        self.pushButton.setVisible(False)

        # 切换复选框状态
#        self.pushButton.setVisible(False)
        self.pushButton.setEnabled(False)
        self.checkBox.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_2.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_3.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_4.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_5.clicked['bool'].connect(self.change_button_checkable)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "考官打分"))
        self.pushButton.setText(_translate("MainWindow2", "确认"))
        self.label_2.setText(_translate("MainWindow2", "考官一"))
        self.label_5.setText(_translate("MainWindow2", "考官二"))
        self.label_4.setText(_translate("MainWindow2", "考官三"))
        self.label_3.setText(_translate("MainWindow2", "考官四"))
        self.label.setText(_translate("MainWindow2", "考官五"))
        self.checkBox_5.setText(_translate("MainWindow2", "已提交"))
        self.checkBox_4.setText(_translate("MainWindow2", "已提交"))
        self.checkBox_3.setText(_translate("MainWindow2", "已提交"))
        self.checkBox_2.setText(_translate("MainWindow2", "已提交"))
        self.checkBox.setText(_translate("MainWindow2", "已提交"))

    def change_button_checkable(self):
        if self.checkBox.isChecked() and \
                self.checkBox_2.isChecked() and \
                self.checkBox_3.isChecked() and \
                self.checkBox_4.isChecked() and \
                self.checkBox_5.isChecked() :
                self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


if __name__ == '__main__':
     app2 = QApplication(sys.argv)
     MainWindow2 = QMainWindow()
     ui = Ui_MainWindow2()
     ui.setupUi(MainWindow2)
     MainWindow2.show()
     MainWindow2.setFixedSize(MainWindow2.width(), MainWindow2.height())
     sys.exit(app2.exec_())
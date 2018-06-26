# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QApplication, QHBoxLayout, QLabel,QDialog
from PyQt5.QtCore import QResource,pyqtSignal,QObject
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import pymysql
import time


#监考端确认考生信息，要求：以准考证号为主键显示考生照片，准考证号，考试科目。
class Ui_MainWindow(QMainWindow,QObject):
    globals()['a'] = 0
    sendmsg_0 = pyqtSignal(object)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 260, 221, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        #考生姓名
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        #self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText('考生姓名')
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        #准考证号
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        #self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText('准考证号')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        #考试科目
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        #self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText('考试科目')
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 390, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 171, 221))
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
        #self.horizontalLayout.addWidget(QLabel(self.verticalLayoutWidget,pixmap=pmap1))
        self.label_0 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_0.setText("")
        self.label_0.setPixmap(pmap1)
        self.label_0.setScaledContents(True)
        self.label_0.setObjectName("label_0")
        self.horizontalLayout.addWidget(self.label_0)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 460, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 530, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menubar.addAction(self.menu.menuAction())

        #下一位考生按钮。
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 200, 61, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        #上一位考生按钮。
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 200, 61, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        #装饰界面。
        self.retranslateUi(MainWindow)


        # 点击考生信息发送按钮后，发射信号。
        self.pushButton_3.clicked.connect(self.run_0)
        #点击下一位考生按钮，信息替换为下一位考生。
        self.pushButton_4.clicked.connect(self.next_student)
        #点击上一位考生按钮，信息替换为上一位考生。
        self.pushButton_5.clicked.connect(self.previous_student)
        #信息有误手工修改按钮
#        self.pushButton_2.clicked.connect(self.modify_information_button_click)
        #考生信息手工选择
#        self.pushButton_3.clicked.connect(self.choose_student_button_click)

#        self.menubar.triggered['QAction*'].connect(self.Browse_history_button)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #连接数据库显示数据库第一个考生

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "准考证号："))
        self.label_3.setText(_translate("MainWindow", "考试科目："))
        self.label.setText(_translate("MainWindow", "考生姓名："))
        self.pushButton.setText(_translate("MainWindow", "开始考试"))
        self.pushButton_2.setText(_translate("MainWindow", "监考端"))
        self.pushButton_3.setText(_translate("MainWindow", "考生信息发送"))
        self.menu.setTitle(_translate("MainWindow", "浏览历史打分记录"))
        self.action_2.setText(_translate("MainWindow", "浏览历史打分"))
        self.action_3.setText(_translate("MainWindow", "退出"))
        self.pushButton_4.setText(_translate("MainWindow", ">>"))
        self.pushButton_5.setText(_translate("MainWindow", "<<"))


    def run_0(self):
        # 发射信号,考生姓名，准考证号，考试科目。
        #print(1)
        #print({'考生姓名':str(self.textEdit_3.toPlainText()),'准考证号':str(self.textEdit_2.toPlainText()),'考试科目':str(self.textEdit.toPlainText())})
        self.sendmsg_0.emit({'考生姓名':str(self.textEdit_3.toPlainText()),
                           '准考证号':str(self.textEdit_2.toPlainText()),
                           '考试科目':str(self.textEdit.toPlainText())})

    def next_student(self):
        if a<=3:
            globals()['a'] = a+1
            cur.execute(("""SELECT id,student_name,subject FROM exam LIMIT {},{}""").format(a,1))
            result_n = cur.fetchone()
            ID, NAME, SUBJECT = range(3)
            id = result_n[ID]
            name = result_n[NAME]
            subject = result_n[SUBJECT]
            #print(id)
            #print(name)
            #print(subject)
            self.textEdit_2.setText(str(id))  # 准考证号
            self.textEdit_3.setText(str(name))  # 考生姓名
            self.textEdit.setText(str(subject))  # 考试科目
            #考生照片
            pmap_new_n = QPixmap(('image\{}.jpg').format(id))
            # print(('image\{}.jpg').format(id))
            self.label_0.setPixmap(pmap_new_n)
        else:
            pass

    def previous_student(self):
        if a!=0:
            globals()['a'] = a-1
            cur.execute(("""SELECT id,student_name,subject FROM exam LIMIT {},{}""").format(a,1))
            result_n = cur.fetchone()
            ID, NAME, SUBJECT = range(3)
            id = result_n[ID]
            name = result_n[NAME]
            subject = result_n[SUBJECT]
            self.textEdit_2.setText(str(id))  # 准考证号
            self.textEdit_3.setText(str(name))  # 考生姓名
            self.textEdit.setText(str(subject))  # 考试科目
            pmap_new_p = QPixmap(('image\{}.jpg').format(id))
            # print(('image\{}.jpg').format(id))
            self.label_0.setPixmap(pmap_new_p)
        else:
            pass
#考官提交分数端
class Ui_Dialog(QDialog,QObject):
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
        #考生科目
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        #考生姓名
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_6)
        #准考证号
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

        pmap1 = QPixmap('image\example.jpg')
        pmap1 = pmap1.scaled(180,210)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setPixmap(pmap1)
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 520, 181, 51))
        self.pushButton.setObjectName("pushButton")

        #点击确认评分按钮后，发射信号。
        self.pushButton.clicked.connect(self.run)
        #点击重新评分按钮后，发射信号。
        self.pushButton_2.clicked.connect(self.run_0)


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

#    def btn1_clicked(self,event):
#        '''鼠标按下事件'''
#        # 判断是否为鼠标左键按下    #可以考虑重写鼠标事件。
#        if event.button() ==  Qt.LeftButton:
#
#            self.pushButton.hide()

    #定义信号。#提交分数按钮
    sendmsg = pyqtSignal(object)
    #申请重新打分按钮。
    sendmsg_1 = pyqtSignal(object)

    def run(self):
        # 发射信号
#        print({'考官姓名':str(self.comboBox.currentText()),'评分':str(self.doubleSpinBox.text())})
        print({'考官姓名':str(self.comboBox.currentText()),'评分':str(self.doubleSpinBox.text()),'准考证号':str(self.textEdit_6.toPlainText()),'考生姓名':str(self.textEdit_4.toPlainText()),'考试科目':self.textEdit_5.toPlainText()})
        self.sendmsg.emit({'考官姓名':str(self.comboBox.currentText()),'评分':str(self.doubleSpinBox.text()),'准考证号':str(self.textEdit_6.toPlainText()),'考生姓名':str(self.textEdit_4.toPlainText()),'考试科目':self.textEdit_5.toPlainText()})

    #接受考生信息
    def get_0(self, msg_0):
#        print(msg_0)
        print(msg_0['准考证号'])
        print(('image\{}.jpg').format(msg_0['准考证号']))
        #考生姓名
        self.textEdit_4.setText(str(msg_0['考生姓名']))
        #准考证号
        self.textEdit_6.setText(str(msg_0['准考证号']))
        #考试科目
        self.textEdit_5.setText(str(msg_0['考试科目']))
        #考生照片
        pmap_new_for_k = QPixmap(('image\{}.jpg').format(str(msg_0['准考证号'])))
        print(pmap_new_for_k)
        #pmap_new_for_k = pmap_new_for_k.scaled(180,210)
        self.label_7.setPixmap(pmap_new_for_k)
    #考官点击申请重新打分按钮
    def run_0(self):
        self.sendmsg_1.emit({'考官姓名':str(self.comboBox.currentText())})

#监考端

class Ui_Dialog_1(QObject):
    msg_from_grade = {}
    def setupUi3(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(917, 621)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 450, 841, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_11.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_11.setSizePolicy(sizePolicy)
        self.doubleSpinBox_11.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_11.setDecimals(1)
        self.doubleSpinBox_11.setMaximum(10.0)
        self.doubleSpinBox_11.setSingleStep(0.1)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_11)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_12.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_12.setDecimals(1)
        self.doubleSpinBox_12.setMaximum(10.0)
        self.doubleSpinBox_12.setSingleStep(0.1)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_12)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_13.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_13.setDecimals(1)
        self.doubleSpinBox_13.setMaximum(10.0)
        self.doubleSpinBox_13.setSingleStep(0.1)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_13)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_14.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_14.setDecimals(1)
        self.doubleSpinBox_14.setMaximum(10.0)
        self.doubleSpinBox_14.setSingleStep(0.1)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_14)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_15.setMinimumSize(QtCore.QSize(162, 50))
        self.doubleSpinBox_15.setDecimals(1)
        self.doubleSpinBox_15.setMaximum(10.0)
        self.doubleSpinBox_15.setSingleStep(0.1)
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_15)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 380, 841, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_11.setChecked(False)
        self.checkBox_11.setObjectName("checkBox_11")
        self.horizontalLayout_10.addWidget(self.checkBox_11, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_12 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_10.addWidget(self.checkBox_12, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_13 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_13.setObjectName("checkBox_13")
        self.horizontalLayout_10.addWidget(self.checkBox_13, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_14 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_14.setObjectName("checkBox_14")
        self.horizontalLayout_10.addWidget(self.checkBox_14, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_15 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_15.setObjectName("checkBox_15")
        self.horizontalLayout_10.addWidget(self.checkBox_15, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 310, 841, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_11.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_11.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_11.addWidget(self.label_23, 0, QtCore.Qt.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_11.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_11.addWidget(self.label_25, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 550, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 841, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        #图片缩放。
        pmap1 = QPixmap('image/k1.jpg')
        #pmap1 = pmap1.scaled(50,50)
        pmap2 = QPixmap('image/k2.jpg')
        #pmap2 = pmap2.scaled(50, 50)
        pmap3 = QPixmap('image/k3.jpg')
        #pmap3 = pmap3.scaled(50, 50)
        pmap4 = QPixmap('image/k4.jpg')
        #pmap4 = pmap4.scaled(50, 50)
        pmap5 = QPixmap('image/k5.jpg')
        #pmap5 = pmap5.scaled(50, 50)


        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_26.setText("")
        self.label_26.setPixmap(pmap1)
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_12.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_27.setText("")
        self.label_27.setPixmap(pmap2)
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_12.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_28.setText("")
        self.label_28.setPixmap(pmap3)
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_12.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_29.setText("")
        self.label_29.setPixmap(pmap4)
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_12.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_30.setText("")
        self.label_30.setPixmap(pmap5)
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_12.addWidget(self.label_30)
        #确认按钮默认设置为无法选中状态。监考端可以更改考官打分提交事项。
        self.pushButton.setEnabled(False)
        self.checkBox_11.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_12.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_13.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_14.clicked['bool'].connect(self.change_button_checkable)
        self.checkBox_15.clicked['bool'].connect(self.change_button_checkable)
        #点击提交按钮，考生信息及考官打分信息录入数据库。

        self.pushButton.clicked.connect(self.commit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox_11.setText(_translate("Dialog", "已打分"))
        self.checkBox_12.setText(_translate("Dialog", "已打分"))
        self.checkBox_13.setText(_translate("Dialog", "已打分"))
        self.checkBox_14.setText(_translate("Dialog", "已打分"))
        self.checkBox_15.setText(_translate("Dialog", "已打分"))
        self.label_21.setText(_translate("Dialog", "考官一"))
        self.label_22.setText(_translate("Dialog", "考官二"))
        self.label_23.setText(_translate("Dialog", "考官三"))
        self.label_24.setText(_translate("Dialog", "考官四"))
        self.label_25.setText(_translate("Dialog", "考官五"))
        self.pushButton.setText(_translate("Dialog", "确认"))


    def change_button_checkable(self):
        if self.checkBox_11.isChecked() and \
                self.checkBox_12.isChecked() and \
                self.checkBox_13.isChecked() and \
                self.checkBox_14.isChecked() and \
                self.checkBox_15.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


    def commit(self):
        #print(msg['准考证号'])
        #print(msg['考生姓名'])
        #print(msg['考试科目'])
        #print(self.doubleSpinBox_11.text())
        #print(self.doubleSpinBox_12.text())
        #print(self.doubleSpinBox_13.text())
        #print(self.doubleSpinBox_14.text())
        #print(self.doubleSpinBox_15.text())

        print(msg_from_grade)
        print(("insert into grade values('{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(str(msg_from_grade['准考证号']),str(msg_from_grade['考生姓名']),str(msg_from_grade['考试科目']),
                    str(self.doubleSpinBox_11.text()),str(self.doubleSpinBox_12.text()),str(self.doubleSpinBox_13.text()),str(self.doubleSpinBox_14.text()),str(self.doubleSpinBox_15.text()),
                    str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))))
        try:
            cur.execute(("insert into grade values('{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(str(msg_from_grade['准考证号']),str(msg_from_grade['考生姓名']),str(msg_from_grade['考试科目']),
                        str(self.doubleSpinBox_11.text()),str(self.doubleSpinBox_12.text()),str(self.doubleSpinBox_13.text()),str(self.doubleSpinBox_14.text()),str(self.doubleSpinBox_15.text()),
                        str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))))
            conn.commit()
            print('success')
            #分数提交数据库之后，前后学生选择按钮失效。
        except:
            print('error'+str(query.lastError().text()))
    # 设置槽对象
    def get(self,msg):
#        print(msg)
        global msg_from_grade
        msg_from_grade = msg
        print(msg_from_grade)

        if msg['考官姓名'] == '考官1':
            self.checkBox_11.setChecked(True)
            self.doubleSpinBox_11.setValue(float(msg['评分']))
            if self.checkBox_11.isChecked() and \
                    self.checkBox_12.isChecked() and \
                    self.checkBox_13.isChecked() and \
                    self.checkBox_14.isChecked() and \
                    self.checkBox_15.isChecked():
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官2':
            self.checkBox_12.setChecked(True)
            self.doubleSpinBox_12.setValue(float(msg['评分']))
            if self.checkBox_11.isChecked() and \
                    self.checkBox_12.isChecked() and \
                    self.checkBox_13.isChecked() and \
                    self.checkBox_14.isChecked() and \
                    self.checkBox_15.isChecked():
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官3':
            self.checkBox_13.setChecked(True)
            self.doubleSpinBox_13.setValue(float(msg['评分']))
            if self.checkBox_11.isChecked() and \
                    self.checkBox_12.isChecked() and \
                    self.checkBox_13.isChecked() and \
                    self.checkBox_14.isChecked() and \
                    self.checkBox_15.isChecked():
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官4':
            self.checkBox_14.setChecked(True)
            self.doubleSpinBox_14.setValue(float(msg['评分']))
            if self.checkBox_11.isChecked() and \
                    self.checkBox_12.isChecked() and \
                    self.checkBox_13.isChecked() and \
                    self.checkBox_14.isChecked() and \
                    self.checkBox_15.isChecked():
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官5':
            self.checkBox_15.setChecked(True)
            self.doubleSpinBox_15.setValue(float(msg['评分']))
            if self.checkBox_11.isChecked() and \
                    self.checkBox_12.isChecked() and \
                    self.checkBox_13.isChecked() and \
                    self.checkBox_14.isChecked() and \
                    self.checkBox_15.isChecked():
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)

    def get_0(self,msg):
        if msg['考官姓名'] == '考官1':
            self.checkBox_11.setChecked(False)
            self.checkBox_11.setText("重新打分")
            self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官2':
            self.checkBox_12.setChecked(False)
            self.checkBox_11.setText("重新打分")
            self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官3':
            self.checkBox_13.setChecked(False)
            self.checkBox_11.setText("重新打分")
            self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官4':
            self.checkBox_14.setChecked(False)
            self.checkBox_11.setText("重新打分")
            self.pushButton.setEnabled(False)
        elif msg['考官姓名'] == '考官5':
            self.checkBox_15.setChecked(False)
            self.checkBox_11.setText("重新打分")
            self.pushButton.setEnabled(False)
    def get_1(self):
        self.doubleSpinBox_11.setValue(0.0)
        self.doubleSpinBox_12.setValue(0.0)
        self.doubleSpinBox_13.setValue(0.0)
        self.doubleSpinBox_14.setValue(0.0)
        self.doubleSpinBox_15.setValue(0.0)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_13.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_11.setText("已打分")
        self.checkBox_12.setText("已打分")
        self.checkBox_13.setText("已打分")
        self.checkBox_14.setText("已打分")
        self.checkBox_15.setText("已打分")


if __name__ == '__main__':
    #主页面
    app = QApplication(sys.argv)
    #监考端考生信息确认界面。
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #连接数据库
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root',
                               password='123456', db='art_exam',charset='gbk')
        cur = conn.cursor()
        sqlstring = "SELECT id,student_name,subject FROM exam LIMIT 0,1"
        cur.execute(sqlstring)
        #if conn.:
        #    print("打开啦")
        #else:
        #    print('打开失败')
        #    print(db.lastError().text())
        print('success')
        result = cur.fetchone()
        #print(result[0])
    except:
        print('false')


    id = result[0]
    name = result[1]
    subject = result[2]

    ui.textEdit_2.setText(str(id))#准考证号
    ui.textEdit_3.setText(str(name))#考生姓名
    ui.textEdit.setText(str(subject))#考试科目
    pmap_new = QPixmap(('image\{}.jpg').format(id))
    #print(('image\{}.jpg').format(id))
    ui.label_0.setPixmap(pmap_new)
#    print(query.first())
    #考官打分界面
    Dialog = QDialog()
    Dialog_0 = Ui_Dialog()
    Dialog_0.setupUi2(Dialog)
    # 开始考试按钮
    ui.pushButton.clicked.connect(Dialog.show)

    #监考确认打分界面
    Dialog1 = QDialog()
    Dialog_1 = Ui_Dialog_1()
    Dialog_1.setupUi3(Dialog1)
    #打开监考打分界面按钮
    ui.pushButton_2.clicked.connect(Dialog1.show)


    #考官打分界面点击确认评分后，数据传输到监考端。包括已提交的checkbook.clicked(True),以及分数的传输doubleSpinBox

    #考官打分信号与监考端监控槽的绑定。
    Dialog_0.sendmsg.connect(Dialog_1.get)
#    Dialog_0.sendmsg.connect(Dialog_1.commit)

    #考生信息信号与考官打分监考界面槽的绑定。
    ui.sendmsg_0.connect(Dialog_0.get_0)
    ui.sendmsg_0.connect(Dialog_1.get_1)
    #打分考官点击申请重新打分按钮。

    Dialog_0.sendmsg_1.connect(Dialog_1.get_0)


    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    Dialog.setFixedSize(Dialog.width(),Dialog.height())
    Dialog1.setFixedSize(Dialog1.width(),Dialog1.height())

    #db.close()
    sys.exit(app.exec_())

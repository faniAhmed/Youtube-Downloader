# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alertNvTrbB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import *


class Ui_Alert(object):
    def setupUi(self, Alert):
        if Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(328, 128)
        Alert.setStyleSheet(u"fusion")
        Alert.setStyleSheet(u"background-color: rgb(54, 57, 63);")
        self.groupBox = QGroupBox(Alert)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 305, 85))
        self.groupBox.setStyleSheet(u"background-color: rgb(47, 49, 54);\n"
"border: 1px solid black;\n"
"border-color: rgb(41, 43, 47);\n"
"border-radius: 7px;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 31, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(208, 0, 0);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 231, 21))
        font1 = QFont()
        font1.setUnderline(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 282, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white;")
        self.retranslateUi(Alert)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Alert", u"Alert!", None))
        self.label_2.setText(QCoreApplication.translate("Alert", u"Entered wrong Url OR video doesnot exisit", None))
        self.label_3.setText(QCoreApplication.translate("Alert", u"If keeps happening. Please update to latest version", None))
    # retranslateUi


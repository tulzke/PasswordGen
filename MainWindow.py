# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(480, 0))
        Form.setMaximumSize(QtCore.QSize(480, 235))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(Form)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.passwordLine = QtWidgets.QLineEdit(self.frame)
        self.passwordLine.setReadOnly(True)
        self.passwordLine.setObjectName("passwordLine")
        self.horizontalLayout_4.addWidget(self.passwordLine)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.mainFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.optsButton = QtWidgets.QPushButton(self.frame_2)
        self.optsButton.setObjectName("optsButton")
        self.horizontalLayout_3.addWidget(self.optsButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.mainFrame)
        self.optsFrame = QtWidgets.QFrame(Form)
        self.optsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optsFrame.setObjectName("optsFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.optsFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.optsFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.amountLabel = QtWidgets.QLabel(self.frame_3)
        self.amountLabel.setObjectName("amountLabel")
        self.horizontalLayout.addWidget(self.amountLabel)
        self.AAALabel = QtWidgets.QLabel(self.frame_3)
        self.AAALabel.setObjectName("AAALabel")
        self.horizontalLayout.addWidget(self.AAALabel)
        self.aaaLabel = QtWidgets.QLabel(self.frame_3)
        self.aaaLabel.setObjectName("aaaLabel")
        self.horizontalLayout.addWidget(self.aaaLabel)
        self.numberLabel = QtWidgets.QLabel(self.frame_3)
        self.numberLabel.setObjectName("numberLabel")
        self.horizontalLayout.addWidget(self.numberLabel)
        self.symbolSpin_2 = QtWidgets.QLabel(self.frame_3)
        self.symbolSpin_2.setObjectName("symbolSpin_2")
        self.horizontalLayout.addWidget(self.symbolSpin_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.optsFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.amountSpin = QtWidgets.QSpinBox(self.frame_4)
        self.amountSpin.setMinimum(1)
        self.amountSpin.setObjectName("amountSpin")
        self.horizontalLayout_2.addWidget(self.amountSpin)
        self.AAASpin = QtWidgets.QSpinBox(self.frame_4)
        self.AAASpin.setMinimum(1)
        self.AAASpin.setObjectName("AAASpin")
        self.horizontalLayout_2.addWidget(self.AAASpin)
        self.aaaSpin = QtWidgets.QSpinBox(self.frame_4)
        self.aaaSpin.setMinimum(1)
        self.aaaSpin.setObjectName("aaaSpin")
        self.horizontalLayout_2.addWidget(self.aaaSpin)
        self.numberSpin = QtWidgets.QSpinBox(self.frame_4)
        self.numberSpin.setMinimum(1)
        self.numberSpin.setObjectName("numberSpin")
        self.horizontalLayout_2.addWidget(self.numberSpin)
        self.symbolSpin = QtWidgets.QSpinBox(self.frame_4)
        self.symbolSpin.setMinimum(1)
        self.symbolSpin.setObjectName("symbolSpin")
        self.horizontalLayout_2.addWidget(self.symbolSpin)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.optsFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Генератор паролей"))
        self.pushButton.setText(_translate("Form", "Сгенерировать"))
        self.optsButton.setText(_translate("Form", "Показать дополнительные параметры"))
        self.amountLabel.setText(_translate("Form", "Длина пароля"))
        self.AAALabel.setText(_translate("Form", "Заглавных"))
        self.aaaLabel.setText(_translate("Form", "Строчных"))
        self.numberLabel.setText(_translate("Form", "Цифр"))
        self.symbolSpin_2.setText(_translate("Form", "Символов"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# from . import login
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(848, 604)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 80, 331, 481))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(True)
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")

        self.l_fup = QtWidgets.QLabel(self.frame)
        self.l_fup.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.l_fup.setObjectName("l_fup")
        self.txt_up = QtWidgets.QLineEdit(self.frame)
        self.txt_up.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.txt_up.setObjectName("txt_up")
        self.btn_browse = QtWidgets.QPushButton(self.frame)
        self.btn_browse.setGeometry(QtCore.QRect(240, 40, 61, 23))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_browse.clicked.connect(lambda: self.btn_browse_click(Dialog))

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 130, 281, 331))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.l_doid = QtWidgets.QLabel(self.frame_2)
        self.l_doid.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.l_doid.setObjectName("l_doid")
        self.txt_viewer = QtWidgets.QTextBrowser(self.frame_2)
        self.txt_viewer.setGeometry(QtCore.QRect(10, 10, 251, 101))
        self.txt_viewer.setObjectName("txt_viewer")
        self.txt_doid = QtWidgets.QLineEdit(self.frame_2)
        self.txt_doid.setGeometry(QtCore.QRect(130, 140, 131, 20))
        self.txt_doid.setObjectName("txt_doid")
        self.btn = QtWidgets.QPushButton(self.frame_2)
        self.btn.setGeometry(QtCore.QRect(10, 180, 251, 31))
        self.btn.setObjectName("btn")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 230, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.l_fc = QtWidgets.QLabel(self.frame)
        self.l_fc.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.l_fc.setObjectName("l_fc")
        self.l_title1 = QtWidgets.QLabel(Dialog)
        self.l_title1.setGeometry(QtCore.QRect(60, 60, 71, 16))
        self.l_title1.setObjectName("l_title1")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(430, 80, 341, 481))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.btn_and = QtWidgets.QPushButton(self.frame_3)
        self.btn_and.setGeometry(QtCore.QRect(30, 20, 101, 23))
        self.btn_and.setObjectName("btn_and")
        self.btn_or = QtWidgets.QPushButton(self.frame_3)
        self.btn_or.setGeometry(QtCore.QRect(170, 20, 101, 23))
        self.btn_or.setObjectName("btn_or")
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 80, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 140, 141, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 160, 141, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_7.setGeometry(QtCore.QRect(170, 60, 141, 16))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_8.setGeometry(QtCore.QRect(170, 80, 141, 16))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_9.setGeometry(QtCore.QRect(170, 100, 141, 16))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_10.setGeometry(QtCore.QRect(170, 120, 141, 16))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_11.setGeometry(QtCore.QRect(170, 140, 141, 16))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_12.setGeometry(QtCore.QRect(170, 160, 141, 16))
        self.checkBox_12.setObjectName("checkBox_12")
        self.btn_encry = QtWidgets.QPushButton(self.frame_3)
        self.btn_encry.setGeometry(QtCore.QRect(30, 430, 101, 23))
        self.btn_encry.setObjectName("btn_encry")
        self.btn_up = QtWidgets.QPushButton(self.frame_3)
        self.btn_up.setGeometry(QtCore.QRect(200, 430, 75, 23))
        self.btn_up.setObjectName("btn_up")
        self.l_efc = QtWidgets.QLabel(self.frame_3)
        self.l_efc.setGeometry(QtCore.QRect(30, 260, 161, 16))
        self.l_efc.setObjectName("l_efc")
        self.txt_efc = QtWidgets.QTextBrowser(self.frame_3)
        self.txt_efc.setGeometry(QtCore.QRect(30, 280, 281, 71))
        self.txt_efc.setObjectName("txt_efc")
        self.l_efnts = QtWidgets.QLabel(self.frame_3)
        self.l_efnts.setGeometry(QtCore.QRect(40, 380, 151, 16))
        self.l_efnts.setObjectName("l_efnts")
        self.txt_save = QtWidgets.QLineEdit(self.frame_3)
        self.txt_save.setGeometry(QtCore.QRect(200, 380, 113, 20))
        self.txt_save.setObjectName("txt_save")
        self.l_title2 = QtWidgets.QLabel(Dialog)
        self.l_title2.setGeometry(QtCore.QRect(430, 60, 71, 16))
        self.l_title2.setObjectName("l_title2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_fup.setText(_translate("Dialog", "File Upload"))
        self.btn_browse.setText(_translate("Dialog", "Browse"))
        self.l_doid.setText(_translate("Dialog", "Data Owner ID"))
        self.btn.setText(_translate("Dialog", "Calculate pseudonym"))
        self.label_5.setText(_translate("Dialog", "Pseudonym"))
        self.l_fc.setText(_translate("Dialog", "File Content"))
        self.l_title1.setText(_translate("Dialog", "File Upload"))
        self.btn_and.setText(_translate("Dialog", "AND Operation"))
        self.btn_or.setText(_translate("Dialog", "OR Operation"))
        self.checkBox_1.setText(_translate("Dialog", "Employee"))
        self.checkBox_2.setText(_translate("Dialog", "Team Leader"))
        self.checkBox_3.setText(_translate("Dialog", "Project Manager"))
        self.checkBox_4.setText(_translate("Dialog", "AssProject Manager"))
        self.checkBox_5.setText(_translate("Dialog", "Manager"))
        self.checkBox_6.setText(_translate("Dialog", "Admin"))
        self.checkBox_7.setText(_translate("Dialog", "Non-Employee"))
        self.checkBox_8.setText(_translate("Dialog", "Unregistered"))
        self.checkBox_9.setText(_translate("Dialog", "Registered"))
        self.checkBox_10.setText(_translate("Dialog", "Student"))
        self.checkBox_11.setText(_translate("Dialog", "Trainee"))
        self.checkBox_12.setText(_translate("Dialog", "HR"))
        self.btn_encry.setText(_translate("Dialog", "ENCRYPTION"))
        self.btn_up.setText(_translate("Dialog", "UPLOAD"))
        self.l_efc.setText(_translate("Dialog", "Encrypted File Content"))
        self.l_efnts.setText(_translate("Dialog", "Enter File Name to Save"))
        self.l_title2.setText(_translate("Dialog", "File Encrypt"))

    def btn_browse_click(self, Dialog):
        fname = QtWidgets.QFileDialog.getOpenFileName()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

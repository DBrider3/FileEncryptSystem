# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 197)
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.btn_login.setStyleSheet("font: 75 9pt \"나눔명조 ExtraBold\";\n"
"border-color: rgb(45, 45, 185);\n"
"background-color: rgb(191, 191, 191);")
        self.btn_login.setObjectName("btn_login")
        self.l_id = QtWidgets.QLabel(Dialog)
        self.l_id.setGeometry(QtCore.QRect(100, 43, 56, 16))
        self.l_id.setStyleSheet("font: 75 9pt \"나눔명조 ExtraBold\";")
        self.l_id.setObjectName("l_id")
        self.l_pw = QtWidgets.QLabel(Dialog)
        self.l_pw.setGeometry(QtCore.QRect(100, 84, 56, 12))
        self.l_pw.setStyleSheet("font: 75 9pt \"나눔명조 ExtraBold\";")
        self.l_pw.setObjectName("l_pw")
        self.txt_id = QtWidgets.QLineEdit(Dialog)
        self.txt_id.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.txt_id.setObjectName("txt_id")
        self.txt_pw = QtWidgets.QLineEdit(Dialog)
        self.txt_pw.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.txt_pw.setObjectName("txt_pw")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_login.setText(_translate("Dialog", "login"))
        self.l_id.setText(_translate("Dialog", "ID"))
        self.l_pw.setText(_translate("Dialog", "PW"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

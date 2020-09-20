# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3

# AES libarary

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES




form_class_0 = uic.loadUiType("login.ui")[0]
form_class_1 = uic.loadUiType("register.ui")[0]
form_class_main = uic.loadUiType("main.ui")[0]
form_class_fileEn = uic.loadUiType("file_en.ui")[0]
form_class_fileDe = uic.loadUiType("file_de.ui")[0]


class AESCipher():
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AESCipher.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

class FileDeWindows(QDialog, form_class_fileDe):
    def __init__(self, parent=None):
        super(FileDeWindows, self).__init__(parent)
        self.setupUi(self)
        self.asecipher = AESCipher("key")

        # 속성 구별
        self.att_and = 0
        self.att_or = 0
        self.user_att = 0
        # 변수 선언
        self.file_en_content = ""
        self.file_de_content = ""
        self.filename = ""
        self.posibility_decry = 0
        # 각각의 event들
        self.btn_browse.clicked.connect(self.pushbtnClicked)
        self.btn_decry.clicked.connect(self.pushDecryClicked)
        self.btn_up.clicked.connect(self.save_text)
        # user attribute
        cur.execute("SELECT user_att from users where id='" + ID + "'")
        for row in cur:
            self.user_att = row[0]


    def pushbtnClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.chk=0
        self.txt_up.setText(fname[0])
        self.filename = fname[0]
        cur.execute("select file from encryption")
        for row in cur:
            if self.filename == row[0]:
                self.chk = 1
                break
        if self.chk == 1:
            cur.execute("select and_attribute,or_attribute from encryption where file='"+self.filename+"'")
            for row in cur:
                self.att_and = row[0]
                self.att_or = row[1]
            self.f = open(self.filename, "r+")
            self.file_en_content = self.f.read()
            self.txt_efc.setText(self.file_en_content)

            self.and_text = self.distinguish_att(self.att_and)
            self.txt_att_and.setText(self.and_text)

            self.or_text = self.distinguish_att(self.att_or)
            self.txt_att_or.setText(self.or_text)

            self.user_text = self.distinguish_att(self.user_att)
            self.txt_att_user.setText(self.user_text)

            if (self.user_att & self.att_and == self.att_and) or self.att_and==0:
                if (self.user_att & self.att_or != 0) or self.att_or ==0:

                    self.txt_chk_de.setText("It is decryption")
                    self.posibility_decry = 1
                else:
                    self.txt_chk_de.setText("It is not decryption")
            else:
                self.txt_chk_de.setText("It is not decryption")

        else:
            QMessageBox.information(self, "info", "File Not Encryption!")

    def distinguish_att(self,data):
        is_first = 1
        self.att_text = ""
        if data & (1 << 0):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Employee"
        if data & (1 << 1):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Team Leader"
        if data & (1 << 2):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Project Manager"
        if data & (1 << 3):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "AssProject Manager"
        if data & (1 << 4):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Manager"
        if data & (1 << 5):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Admin"
        if data & (1 << 6):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Non-Employee"
        if data & (1 << 7):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Unregistered"
        if data & (1 << 8):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Registered"
        if data & (1 << 9):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Student"
        if data & (1 << 10):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "Trainee"
        if data & (1 << 11):
            if (is_first):
                is_first = 0
            else:
                self.att_text += ", "
            self.att_text += "HR"
        return self.att_text

    def pushDecryClicked(self):
        if self.posibility_decry == 1:
            self.file_de_content = self.asecipher.decrypt(self.file_en_content)
            self.txt_dfc.setText(self.file_de_content)

    def save_text(self):
        if self.file_de_content != "":
            filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
            with open(filename[0], 'w') as f:
                f.write(self.file_de_content)
            QMessageBox.information(self, "info", "File Decrypt Complete!")
            self.accept()

class FileEnWindows(QDialog, form_class_fileEn):
    def __init__(self, parent=None):
        super(FileEnWindows, self).__init__(parent)
        self.setupUi(self)
        self.asecipher = AESCipher("key")
        # 속성 구별
        global att_and, att_or
        # 기본적으로 변수 선언
        self.file_content = ""
        self.file_en_content = ""
        self.login_idx = ""
        self.login_id = ""
        self.login_city = ""
        self.login_encont = ""

        cur.execute("select id,city,POCode from users where id='" + ID + "'")
        for row in cur:
            self.login_id = row[0]
            self.login_city = row[1]
            self.login_encont = row[2]

        # 각각의 event들
        self.btn_browse.clicked.connect(self.pushbtnClicked)
        self.txt_doid.setText(ID)
        self.btn_cal_pse.clicked.connect(self.crypto_id)
        # operation
        self.btn_and.clicked.connect(self.and_oper_Clicked)
        self.btn_or.clicked.connect(self.or_oper_Clicked)
        # Encryption
        self.btn_encry.clicked.connect(self.crypto_content)
        self.btn_up.clicked.connect(self.save_text)

    def save_text(self):
        input_filename = cur.execute("SELECT idx from encryption WHERE file is NULL")

        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            f.write(self.file_en_content)
        cur.execute("UPDATE encryption set file=(?) where idx=(?);",
                         (filename[0],input_filename.lastrowid))
        con.commit()
        QMessageBox.information(self, "info", "File Encrypt Complete!")
        self.accept()

    def crypto_content(self):
        self.file_en_content = self.asecipher.encrypt(self.file_content)
        self.txt_efc.setText(self.file_en_content)

        cur.execute("INSERT INTO encryption VALUES(?,?,?,?,?,?,?);",
            (None, self.login_id, self.login_city, self.login_encont, None,att_and,att_or))
        con.commit()

    def crypto_id(self):
        self.id_print = str(ID[len(ID) - 2:])
        self.xxx = str("")
        for i in range(len(ID) - 2):
            self.xxx += "X"
        self.id_print = self.xxx + self.id_print
        self.txt_pse.setText(self.id_print)

    def pushbtnClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.txt_up.setText(fname[0])
        self.filename = fname[0]
        self.f = open(self.filename, "r+")
        self.file_content = self.f.read()
        self.txt_viewer.setText(self.file_content)


    def btn_clear(self):
        self.chk_Employee.setChecked(False)
        self.chk_Team_Leader.setChecked(False)
        self.chk_Project_Manager.setChecked(False)
        self.chk_AssProject_Manager.setChecked(False)
        self.chk_Manager.setChecked(False)
        self.chk_Admin.setChecked(False)
        self.chk_Non_Employee.setChecked(False)
        self.chk_Unregistered.setChecked(False)
        self.chk_Registered.setChecked(False)
        self.chk_Student.setChecked(False)
        self.chk_Trainee.setChecked(False)
        self.chk_HR.setChecked(False)

    def and_oper_Clicked(self):
        global att_and
        att_and = 0
        if self.chk_Employee.isChecked():
            att_and += 1 << 0
        if self.chk_Team_Leader.isChecked():
            att_and += 1 << 1
        if self.chk_Project_Manager.isChecked():
            att_and += 1 << 2
        if self.chk_AssProject_Manager.isChecked():
            att_and += 1 << 3
        if self.chk_Manager.isChecked():
            att_and += 1 << 4
        if self.chk_Admin.isChecked():
            att_and += 1 << 5
        if self.chk_Non_Employee.isChecked():
            att_and += 1 << 6
        if self.chk_Unregistered.isChecked():
            att_and += 1 << 7
        if self.chk_Registered.isChecked():
            att_and += 1 << 8
        if self.chk_Student.isChecked():
            att_and += 1 << 9
        if self.chk_Trainee.isChecked():
            att_and += 1 << 10
        if self.chk_HR.isChecked():
            att_and += 1 << 11
        self.btn_clear()
        QMessageBox.information(self, "info", "AND Operation Complete!")
        return att_and


    def or_oper_Clicked(self):
        global att_or
        att_or = 0
        if self.chk_Employee.isChecked():
            att_or += 1 << 0
        if self.chk_Team_Leader.isChecked():
            att_or += 1 << 1
        if self.chk_Project_Manager.isChecked():
            att_or += 1 << 2
        if self.chk_AssProject_Manager.isChecked():
            att_or += 1 << 3
        if self.chk_Manager.isChecked():
            att_or += 1 << 4
        if self.chk_Admin.isChecked():
            att_or += 1 << 5
        if self.chk_Non_Employee.isChecked():
            att_or += 1 << 6
        if self.chk_Unregistered.isChecked():
            att_or += 1 << 7
        if self.chk_Registered.isChecked():
            att_or += 1 << 8
        if self.chk_Student.isChecked():
            att_or += 1 << 9
        if self.chk_Trainee.isChecked():
            att_or += 1 << 10
        if self.chk_HR.isChecked():
            att_or += 1 << 11
        self.btn_clear()
        QMessageBox.information(self, "info", "OR Operation Complete!")
        return att_or




class SignupWindows(QDialog, form_class_1):
    def __init__(self, parent=None):
        super(SignupWindows, self).__init__(parent)
        self.setupUi(self)
        self.login = LoginWindow()
        self.t_password.setEchoMode(QLineEdit.Password)

        self.user_att = 0

        self.employee_ichk = 0
        self.teamleader_ichk = 0
        self.projectmanager_ichk = 0
        self.asstprojectmanager_ichk = 0
        self.manager_ichk = 0
        self.admin_ichk = 0
        self.nonemployee_ichk = 0
        self.unregistered_ichk = 0
        self.registered_ichk = 0
        self.student_ichk = 0
        self.trainee_ichk = 0
        self.hr_ichk = 0

        self.Employee_check.stateChanged.connect(self.checkbtn_fnc)
        self.TeamLeader_check.stateChanged.connect(self.checkbtn_fnc)
        self.Projectmanager_check.stateChanged.connect(self.checkbtn_fnc)
        self.AsstProjectManager_check.stateChanged.connect(self.checkbtn_fnc)
        self.Manager_check.stateChanged.connect(self.checkbtn_fnc)
        self.Admin_check.stateChanged.connect(self.checkbtn_fnc)
        self.NonEmployee_check.stateChanged.connect(self.checkbtn_fnc)
        self.Unregistered_check.stateChanged.connect(self.checkbtn_fnc)
        self.Registered_check.stateChanged.connect(self.checkbtn_fnc)
        self.Student_check.stateChanged.connect(self.checkbtn_fnc)
        self.Trainee_check.stateChanged.connect(self.checkbtn_fnc)
        self.HR_check.stateChanged.connect(self.checkbtn_fnc)

        self.btn_register.clicked.connect(self.check_blank)

    def blank_clear(self):
        self.blank_target = [self.t_loginid,self.t_password,self.t_city,self.t_pocode,self.t_email,self.t_mobileno]
        for i in self.blank_target:
            i.clear()


    def check_blank(self):
        self.text_write_fnc()
        self.user = [self.loginid, self.passid, self.city, self.pocode, self.email, self.mobileno]
        chk_blank = 0
        for row in self.user:
            if row == "":
                chk_blank = 1
                break
        if chk_blank == 1:
            QMessageBox.information(self, "info", "Please Check blank exist!")
            self.blank_clear()
        else:
            self.check_id_overlap()


    def check_id_overlap(self):
        cur.execute('select * from users')
        check = 0
        for row in cur:
            if self.loginid == row[0]:
                check = 1
                break

        if check == 1:
            QMessageBox.information(self, "info", "Please ID, Already exist!")
            self.blank_clear()
        else:
            self.db_write_fnc()
            con.commit()
            QMessageBox.information(self, "info", "Congratulation Register!")
            self.blank_clear()
            self.login.blank()
            self.accept()

    def db_write_fnc(self):
        cur.execute("INSERT INTO users Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?);",
                         (self.loginid, self.passid, self.city,
                          self.pocode, self.email, self.mobileno,
                          self.employee_ichk, self.teamleader_ichk,
                          self.projectmanager_ichk, self.asstprojectmanager_ichk,
                          self.manager_ichk, self.admin_ichk, self.nonemployee_ichk,
                          self.unregistered_ichk, self.registered_ichk, self.student_ichk,
                          self.trainee_ichk, self.hr_ichk,None,self.user_att))

    def text_write_fnc(self):
        self.loginid = self.t_loginid.text()
        self.passid = self.t_password.text()
        self.city = self.t_city.text()
        self.pocode = self.t_pocode.text()
        self.email = self.t_email.text()
        self.mobileno = self.t_mobileno.text()

    def checkbtn_fnc(self):
        self.user_att = 0
        if self.Employee_check.isChecked():
            self.employee_ichk = 1
            self.user_att += 1 << 0
        if self.TeamLeader_check.isChecked():
            self.teamleader_ichk = 1
            self.user_att += 1 << 1
        if self.Projectmanager_check.isChecked():
            self.projectmanager_ichk = 1
            self.user_att += 1 << 2
        if self.AsstProjectManager_check.isChecked():
            self.asstprojectmanager_ichk = 1
            self.user_att += 1 << 3
        if self.Manager_check.isChecked():
            self.manager_ichk = 1
            self.user_att += 1 << 4
        if self.Admin_check.isChecked():
            self.admin_ichk = 1
            self.user_att += 1 << 5
        if self.NonEmployee_check.isChecked():
            self.nonemployee_ichk = 1
            self.user_att += 1 << 6
        if self.Unregistered_check.isChecked():
            self.unregistered_ichk = 1
            self.user_att += 1 << 7
        if self.Registered_check.isChecked():
            self.registered_ichk = 1
            self.user_att += 1 << 8
        if self.Student_check.isChecked():
            self.student_ichk = 1
            self.user_att += 1 << 9
        if self.Trainee_check.isChecked():
            self.trainee_ichk = 1
            self.user_att += 1 << 10
        if self.HR_check.isChecked():
            self.hr_ichk = 1
            self.user_att += 1 << 11

class MainWindows(QDialog, form_class_main):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        self.login = LoginWindow()

        self.btn_logout.clicked.connect(self.logout_Clicked)

        self.btn_push_1.clicked.connect(self.push1_Clicked)
        self.btn_push_2.clicked.connect(self.push2_Clicked)

    def logout_Clicked(self):
        QMessageBox.information(self, "info", "Logout Complete")
        self.login.blank()
        self.accept()


    def push1_Clicked(self):
        self.fileEnmwindows = FileEnWindows(self)
        self.fileEnmwindows.show()
    def push2_Clicked(self):
        self.fileDewindows = FileDeWindows(self)
        self.fileDewindows.show()

class LoginWindow(QMainWindow, form_class_0):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global con,cur,key
        key = "key"
        con = sqlite3.connect('oss.db')
        cur = con.cursor()

        self.txt_pw.setEchoMode(QLineEdit.Password)

        self.btn_newuser.clicked.connect(self.newuser_clicked)
        self.btn_login.clicked.connect(self.login_clicked)


    def blank(self):
        self.blank_target = [GTXT_ID,GTXT_PW]
        for i in self.blank_target:
            i.clear()

    def newuser_clicked(self):
        global GTXT_ID
        global GTXT_PW
        GTXT_ID = self.txt_id
        GTXT_PW = self.txt_pw
        self.signupwindows = SignupWindows(self)
        self.signupwindows.show()

    def login_clicked(self):
        global ID
        global GTXT_ID
        global GTXT_PW
        check = 0
        self.loginid = self.txt_id.text()
        ID = self.loginid
        self.passid = self.txt_pw.text()
        GTXT_ID = self.txt_id
        GTXT_PW = self.txt_pw

        cur.execute('select * from users')
        for row in cur:
            if self.loginid == row[0] and self.passid == row[1]:
                check = 1
                break

        if check == 1:
            QMessageBox.information(self, "info", "Hello Encryption Programming!")
            self.mainwindows = MainWindows(self)
            self.mainwindows.show()
        else:
            QMessageBox.information(self,"info","Error at the login!")

app = QApplication(sys.argv)
loginwindows = LoginWindow()
loginwindows.show()
app.exec_()

loginwindows.con.close()




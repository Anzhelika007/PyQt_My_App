import sys

import sqlite3
# шифруем пароль
import hashlib

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, Signal

from ui.base_ui.ui_registation import Ui_Form



class Regisrtation(QWidget):

    def __init__(self):
        super(Regisrtation, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # данные пользователя
        self.login : str = ''
        self.password = self.ui.lineEdit_2.text()


        self.ui.pushButton.clicked.connect(self.verification)
        self.ui.pushButton_2.clicked.connect(self.registration)
        # после вызова функции очистить
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def coding_pass(self, val):
        return hashlib.md5(val.encode()).hexdigest()

    def message_info(self, title, message_text):
        self.message = QMessageBox().information(self, title, message_text)
        print(self.message)
        print(title)




    def verification(self):
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()

        try:
            # подключаемся к базе
            db = sqlite3.connect('database.db')
            cursor = db.cursor()

            # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
            db.create_function("coding_pass", 1, self.coding_pass)

            cursor.execute("""SELECT user_login FROM users WHERE user_login = ?""", [self.login])
            if cursor.fetchone() is None:
                self.ui.lineEdit.setStyleSheet("border-color: rgba(255, 0, 0, 127);")
                self.message_info('Registration login', f'User {self.login} not registered')
            else:
                self.ui.lineEdit.setStyleSheet("border-color: rgba(0, 212, 155, 127);")
                cursor.execute(
                    'SELECT user_password FROM users WHERE user_login = ? AND user_password = coding_pass(?)',
                    [self.login, self.password])
                if cursor.fetchone() is None:
                    self.ui.lineEdit_2.setStyleSheet("border-color: rgba(255, 0, 0, 127);")
                    self.message_info('Registration password', 'Password is incorrect or missing')

                else:
                    self.ui.lineEdit_2.setStyleSheet("border-color: rgba(0, 212, 155, 127);")
                    self.message_info('Login', f'Hello  {self.login}!')

            cursor.close()
            db.close()
        except sqlite3.Error as e:
            print('Error', e)

    def registration(self):
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        self.email = self.ui.lineEdit_3.text()
        self.users_values = (self.login, self.password, self.email)

        if len(self.login) > 3 and self.login[0].isupper():
            self.ui.lineEdit.setStyleSheet("border-color: rgba(0, 212, 155, 125);")
            if len(self.password) > 5:
                self.total_upper = False
                self.total_lower = False
                self.total_digit = False
                for i in self.password:
                    if i.isupper():
                        self.total_upper = True
                    elif i.islower():
                        self.total_lower = True
                    elif i.isdigit():
                        self.total_digit = True
                if self.total_upper and self.total_lower and self.total_digit:
                    print(self.password)
                    self.ui.lineEdit_2.setStyleSheet("border-color: rgba(0, 212, 155, 125);")
                    if '@' in self.email and '.' in self.email and len(self.email) > 4:
                        self.ui.lineEdit_3.setStyleSheet("border-color: rgba(0, 212, 155, 125);")
                        # подключаемся к базе
                        db = sqlite3.connect('database.db')
                        cursor = db.cursor()

                        # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
                        db.create_function("coding_pass", 1, self.coding_pass)

                        cursor.execute(
                            "INSERT INTO users(user_login, user_password, user_email) VALUES (?,coding_pass(?),?)",
                            self.users_values)
                        db.commit()
                        cursor.close()
                        db.close()
                        self.message_info('Registration', f'User {self.login} successfully registered!')

                    else:
                        self.message_info('Registration email address', 'The mailing address must contain the characters "@" and "." Address length is at least 5 characters')
                else:
                    self.message_info('Registration password', 'The password must contain 1 uppercase letter, 1 lowercase letter, 1 number.')
            else:
                self.message_info('Registration password', 'The password must contain 1 uppercase letter, 1 lowercase letter, 1 number. Its length is at least 6 characters')
        else:
            self.message_info('Registration login', 'Login starts with a capital letter and is at least 4 characters long')

        self.users_values = []



if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    reg = Regisrtation()
    reg.show()
    sys.exit(app.exec())

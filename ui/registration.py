import sys

import sqlite3
# шифруем пароль
import hashlib
from string import octdigits

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHeaderView, QComboBox, QFormLayout, QWidget, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout

from ui.base_ui.ui_registation import Ui_Form


class Regisrtation(QWidget):
    def __init__(self):
        super(Regisrtation, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # данные пользователя
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()


        self.ui.pushButton.clicked.connect(self.verification)
        self.ui.pushButton_2.clicked.connect(self.registration)
        # после вызова функции очистить
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def coding_pass(self, val):
        return hashlib.md5(val.encode()).hexdigest()

    def message_info(self, title, message):
        self.massage = QMessageBox().information(window, title, message)

    def verification(self):
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        #print(self.login, self.password)

        try:
            # подключаемся к базе
            db = sqlite3.connect('../database.db')
            cursor = db.cursor()

            # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
            db.create_function("coding_pass", 1, self.coding_pass)

            cursor.execute("""SELECT user_login FROM users WHERE user_login = ?""", [self.login])
            if cursor.fetchone() is None:
                self.ui.lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
                print('Такого логина не существует!')
            else:
                self.ui.lineEdit.setStyleSheet("background-color: rgb(0, 212, 155);")
                cursor.execute('SELECT user_password FROM users WHERE user_login = ? AND user_password = coding_pass(?)', [self.login, self.password])
                if cursor.fetchone() is None:
                    self.ui.lineEdit_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                    print('Пароль неверный!')
                else:
                    self.ui.lineEdit_2.setStyleSheet("background-color: rgb(0, 212, 155);")
                    pass

            cursor.close()
            db.close()
        except sqlite3.Error as e:
            print('Error', e)

    def registration(self):
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        self.email = self.ui.lineEdit_3.text()
        self.users_values = (self.login, self.password, self.email)
        #print(self.login, self.password, self.email)

        if self.login[0].isupper() and len(self.login) > 3:
            self.ui.lineEdit.setStyleSheet("background-color: rgb(0, 212, 155);")
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
                    self.ui.lineEdit_2.setStyleSheet("background-color: rgb(0, 212, 155);")
                    if '@' in self.email and '.' in self.email and len(self.email) > 4:
                        self.ui.lineEdit_3.setStyleSheet("background-color: rgb(0, 212, 155);")
                        # подключаемся к базе
                        db = sqlite3.connect('../database.db')
                        cursor = db.cursor()

                        # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
                        db.create_function("coding_pass", 1, self.coding_pass)

                        cursor.execute(
                            "INSERT INTO users(user_login, user_password, user_email) VALUES (?,coding_pass(?),?)",
                            self.users_values)
                        db.commit()
                        # cursor.execute("SELECT * FROM users")
                        # k = cursor.fetchall()
                        # print(k)
                        cursor.close()
                        db.close()
                        self.message_info('Registration', f'Пользователь {self.login} успешно зарегистрирован!')
                    else:
                        self.message_info('Registration email address', 'Почта говно')
                else:
                    self.message_info('Registration password', 'Пароль должен содержать 1 цифру Букву Верх и букву ниж')
            else:
                self.message_info('Registration password','Пароль короткий')
        else:
            self.message_info('Registration login', 'Логин начинается с большой буквы не менее 4 символов')

        self.users_values = []


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = Regisrtation()
    window.show()
    sys.exit(app.exec())

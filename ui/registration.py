import sys

import sqlite3
# шифруем пароль
import hashlib

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHeaderView, QComboBox, QFormLayout, QWidget
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

    def coding_pass(self, val):
        return hashlib.md5(val.encode()).hexdigest()

    def verification(self):
        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        print(self.login, self.password)

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
        print(self.login, self.password, self.email)

        # подключаемся к базе
        db = sqlite3.connect('../database.db')
        cursor = db.cursor()

        # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
        db.create_function("coding_pass", 1, self.coding_pass)

        cursor.execute("INSERT INTO users(user_login, user_password, user_email) VALUES (?,coding_pass(?),?)", self.users_values)
        db.commit()
        cursor.execute("SELECT * FROM users")
        k = cursor.fetchall()
        print(k)


        cursor.close()
        db.close()

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.users_values = []


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = Regisrtation()
    window.show()
    sys.exit(app.exec())

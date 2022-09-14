import sys
import sqlite3

from datetime import timedelta, date

import PySide6
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QCheckBox
from PySide6.QtCore import QDate

from PySide6.QtCore import Slot, Signal

from ui.base_ui.ui_goal import Ui_Form
from ui.motivation import Motivation

class Goal(QWidget):

    def __init__(self, login, qdate):
        super(Goal, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.login = login
        self.qdate = qdate
        self.ui.comboBoxPriority.addItems(['Low', 'Medium', 'High'])
        self.ui.lineEditGoal_4.setText('')
        self.ui.lineEditTask_1.setText('')
        self.ui.lineEditTask_2.setText('')
        self.ui.lineEditTask_3.setText('')

        # даты - старт и енд
        self.qdate = QDate.currentDate()  # получили текущую
        self.ui.dateEdit_6.setDate(self.qdate)
        self.ui.dateEdit_7.setDate(self.qdate)

        self.ui.pushButtonAddTasks.clicked.connect(self.add_goals_base)

    def message_info_goals(self, title, message_text):
        self.message_goals = QMessageBox().information(self, title, message_text)

    def range_checkBox(self, value_list, list_day, task_day):
        # проверяем отмеченные чекбоксы и помещаем в список номер дня для дальнейшего сравнения (weekday())
        for checkBox in value_list:
            if checkBox.isChecked():
                name = str(checkBox.objectName())[-4:-1]
                for key, value in task_day.items():
                    if name in value:
                        list_day.append(key)

    def date_task(self, date_start, date_end, list_week, list_date):
        # прогоняем дни периода цели и проверяем на соответствие ранее заданным дням недели
        while date_start <= date_end:
            if date_start.weekday() in list_week:
                # получаем список дат задания за заданный период
                list_date.append(date_start.strftime('%Y-%m-%d'))
            date_start += timedelta(days=1)

    def add_info(self, task_row, task_date, user, goal, task, start_date, end_date, priority):
        # формируем список данных
        for i in task_date:
            task_row.append(
                (user, goal, task, i, priority, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))

    def add_goals_base(self):
        self.priority = self.ui.comboBoxPriority.currentText()
        if len(self.ui.lineEditGoal_4.text()) < 3:
            self.message_info_goals('Goal', "Fill in the 'Goal' field (must contain at least 3 characters)")
        elif len(self.ui.lineEditTask_1.text()) < 3 and 0 < len(self.ui.lineEditTask_2.text()) < 3 and 0 < len(
                self.ui.lineEditTask_3.text()) < 3:
            self.message_info_goals('Task', "Fill in the 'Task' field (must contain at least 3 characters)")

        self.task_week_day = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

        # нашли всех детей четбоксов из фрейма сложили в список task_week_days, затем сложим во второй список дату задачи
        self.task1_checbox = self.ui.frameTask1.findChildren(QCheckBox)
        # создали пустой лист для складывания задействованных чекбоксов (isChecked())
        self.task1_week_days = []
        self.task1_date = []
        self.task2_checbox = self.ui.frameTask2.findChildren(QCheckBox)
        self.task2_week_days = []
        self.task2_date = []
        self.task3_checbox = self.ui.frameTask3.findChildren(QCheckBox)
        self.task3_week_days = []
        self.task3_date = []

        self.range_checkBox(self.task1_checbox, self.task1_week_days, self.task_week_day)
        self.range_checkBox(self.task2_checbox, self.task2_week_days, self.task_week_day)
        self.range_checkBox(self.task3_checbox, self.task3_week_days, self.task_week_day)

        # проверяем заполнены ли чексбоксы или цели к ним
        if len(self.task1_week_days) == 0:
            self.message_info_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        elif len(self.ui.lineEditTask_2.text()) > 2 and len(self.task2_week_days) == 0:
            self.message_info_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        elif len(self.ui.lineEditTask_3.text()) > 2 and len(self.task3_week_days) == 0:
            self.message_info_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        else:
            # форматируем дату для обработки
            self.date_start = (self.ui.dateEdit_6.date()).toPython()
            self.date_end = (self.ui.dateEdit_7.date()).toPython()

            # собираем даты задач в списки
            self.date_task(self.date_start, self.date_end, self.task1_week_days, self.task1_date)
            # print(self.task1_date)
            if len(self.task2_week_days) > 0:
                self.date_task(self.date_start, self.date_end, self.task2_week_days, self.task2_date)
                # print(self.task2_date)
            if len(self.task3_week_days) > 0:
                self.date_task(self.date_start, self.date_end, self.task3_week_days, self.task3_date)
                # print(self.task3_date)

        # собираем строки для занисения в базу данных
        self.task1_row = []
        self.task2_row = []
        self.task3_row = []
        self.add_info(self.task1_row, self.task1_date, self.login, self.ui.lineEditGoal_4.text(),
                      self.ui.lineEditTask_1.text(), self.date_start, self.date_end, self.priority)
        if len(self.task2_date) > 0:
            self.add_info(self.task2_row, self.task2_date, self.login, self.ui.lineEditGoal_4.text(),
                          self.ui.lineEditTask_2.text(), self.date_start, self.date_end, self.priority)
        if len(self.task3_date) > 0:
            self.add_info(self.task3_row, self.task3_date, self.login, self.ui.lineEditGoal_4.text(),
                          self.ui.lineEditTask_3.text(), self.date_start, self.date_end, self.priority)

        try:
            # подключаемся к базе
            db = sqlite3.connect('../database.db')
            cursor = db.cursor()

            # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
            # db.create_function("coding_pass", 1, self.coding_pass)

            cursor.executemany(
                '''INSERT INTO goals(user_login, goal, goal_task, date_task, priority, date_start, date_end) VALUES (?,?,?,?,?,?,?)''',
                self.task1_row)
            if len(self.task2_row) > 0:
                cursor.executemany(
                    '''INSERT INTO goals(user_login, goal, goal_task, date_task, priority, date_start, date_end) VALUES (?,?,?,?,?,?,?)''',
                    self.task2_row)
            if len(self.task3_row) > 0:
                cursor.executemany(
                    '''INSERT INTO goals(user_login, goal, goal_task, date_task, priority, date_start, date_end) VALUES (?,?,?,?,?,?,?)''',
                    self.task3_row)

            cursor.execute('''SELECT * FROM goals''')
            k = cursor.fetchall()
            db.commit()
            print('база', k)
            cursor.close()
            db.close()
        except sqlite3.Error as e:
            print('Error', e)



        # print(self.task1_row)
        # print(self.task2_row)
        # print(self.task3_row)

        # qdate = QDate.currentDate()
        # pydate = qdate.toPython()
        #
        # print('то что нужно', pydate, pydate.weekday())

        # self.ui.pushButton_14.connect()
        # ловим изменения title цели (textChanged - генерит каждый символ) поэтому editingFinished
        # self.ui.lineEditGoal_4.editingFinished.connect(self.lineEdit_changed_title)
        # self.ui.lineEditTask_1.editingFinished.connect(self.lineEdit_changed_task1)
        # self.ui.lineEditTask_2.editingFinished.connect(self.lineEdit_changed)
        # self.ui.lineEditTask_3.editingFinished.connect(self.lineEdit_changed)

    # def message_info_goals(self, title, message_text):
    #     self.message_goals = QMessageBox().information(self, title, message_text)


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = Goal()
    window.show()
    sys.exit(app.exec())

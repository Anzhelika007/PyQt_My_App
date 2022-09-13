import sys
import time
from datetime import timedelta, date

import PySide6
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QCheckBox
from PySide6.QtCore import QDate

from PySide6.QtCore import Slot, Signal

from ui.base_ui.ui_goal import Ui_Form


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
        while date_start <= date_end:
            if date_start.weekday() in list_week:
                # получаем список дат задания за заданный период
                list_date.append(date_start.strftime('%y-%m-%d'))
            date_start += timedelta(days=1)

    def add_goals_base(self):
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
            # print(type(self.date_start))
            # print('njn', self.date_start)
            # собираем даты задачи
            self.date_task(self.date_start, self.date_end, self.task1_week_days, self.task1_date)
            print(self.task1_date)
            if len(self.task2_week_days) > 0:
                self.date_task(self.date_start, self.date_end, self.task2_week_days, self.task2_date)
                print(self.task2_date)
            if len(self.task3_week_days) > 0:
                self.date_task(self.date_start, self.date_end, self.task3_week_days, self.task3_date)
                print(self.task3_date)


            qdate = QDate.currentDate()
            pydate = qdate.toPython()

            print('то что нужно', pydate, pydate.weekday())

        # self.ui.pushButton_14.connect()
        # ловим изменения title цели (textChanged - генерит каждый символ) поэтому editingFinished
        # self.ui.lineEditGoal_4.editingFinished.connect(self.lineEdit_changed_title)
        # self.ui.lineEditTask_1.editingFinished.connect(self.lineEdit_changed_task1)
        # self.ui.lineEditTask_2.editingFinished.connect(self.lineEdit_changed)
        # self.ui.lineEditTask_3.editingFinished.connect(self.lineEdit_changed)

    # def message_info_goals(self, title, message_text):
    #     self.message_goals = QMessageBox().information(self, title, message_text)
    #
    # def lineEdit_changed_title(self):
    #     # после изменения фокуса - проверяем значение
    #     if len(self.ui.lineEditGoal_4.text()) < 3:
    #         self.message_info_goals('Title', 'ВВеди цель нормально')
    #         self.ui.lineEditTask_1.setMaxLength(0)
    #     else:
    #         self.ui.lineEditTask_1.setMask('xxxxxxxxXXXXXXXXXX')
    #
    #
    #


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = Goal()
    window.show()
    sys.exit(app.exec())

import sys
import time

import PySide6
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

        self.qdate = QDate.currentDate()  # получили текущую
        self.ui.dateEdit_6.setDate(self.qdate)
        self.ui.dateEdit_7.setDate(self.qdate)

        self.ui.pushButtonAddTasks.clicked.connect(self.add_goals_base)

    def message_info_goals(self, title, message_text):
        self.message_goals = QMessageBox().information(self, title, message_text)

    def range_checkBox(self, value_list, list_day):
        for checkBox in value_list:
            if checkBox.isChecked():
                name = str(checkBox.objectName())[-4:-1]
                list_day.append(name)

    def add_goals_base(self):
        if len(self.ui.lineEditGoal_4.text()) < 3:
            self.message_info_goals('Goal', "Fill in the 'Goal' field (must contain at least 3 characters)")
        elif len(self.ui.lineEditTask_1.text()) < 3 and 0 < len(self.ui.lineEditTask_2.text()) < 3 and 0 < len(
                self.ui.lineEditTask_3.text()) < 3:
            self.message_info_goals('Task', "Fill in the 'Task' field (must contain at least 3 characters)")

        self.task_day = {'Monday': 'Mon', 'Tuesday': 'Tue', 'Wednesday': 'Wed', 'Thursday': 'Thu', 'Friday': 'Fri',
                         'Saturday': 'Sat', 'Sunday': 'Sun'}

        self.task1_checbox = self.ui.frameTask1.findChildren(QCheckBox)
        self.task1_days = []
        self.task2_checbox = self.ui.frameTask2.findChildren(QCheckBox)
        self.task2_days = []
        self.task3_checbox = self.ui.frameTask3.findChildren(QCheckBox)
        self.task3_days = []

        self.range_checkBox(self.task1_checbox, self.task1_days)
        print(*self.task1_days)
        self.range_checkBox(self.task2_checbox, self.task2_days)
        print(*self.task2_days)
        self.range_checkBox(self.task3_checbox, self.task3_days)
        print(*self.task3_days)

        if len(self.task1_days) == 0:
            self.message_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        elif len(self.ui.lineEditTask_2.text()) > 2 and len(self.task2_days) == 0:
            self.message_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        elif len(self.ui.lineEditTask_3.text()) > 2 and len(self.task3_days) == 0:
            self.message_goals('Tasks days', 'You must devote at least 1 time per week to the task')
        else:
            print(self.ui.dateEdit_6.text())
            print(self.ui.dateEdit_6)
            print(self.ui.dateEdit_7.date())

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

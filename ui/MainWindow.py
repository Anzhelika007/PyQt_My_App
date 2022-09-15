import sys
import sqlite3
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHeaderView, QComboBox
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.base_ui.ui_mainWindow import Ui_MainWindow
from ui.goal import Goal
from ui.motivation import Motivation


#  тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow, QWidget):

    def __init__(self, login='Qqqq'):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login = login
        self.ui.pageHome.show()

        self.ui.pushButtonHome.clicked.connect(self.menu_home)
        self.ui.pushButtonGoals.clicked.connect(self.menu_goals)
        self.ui.pushButtonAnalis.clicked.connect(self.menu_analis)
        self.ui.pushButtonMotivation.clicked.connect(self.menu_motivation)
        self.ui.pushButtonHabit.clicked.connect(self.menu_hadit)
        self.ui.pushButtonEnglish.clicked.connect(self.menu_english)
        # переменные комбо боксов
        self.goals_list = ['none']

        # задаем и удаляем цель(сразу добавляем мотивацию для каждой цели)
        self.ui.pushButton.clicked.connect(self.add_goal)
        self.ui.pushButtonCreate.clicked.connect(self.add_motivation)

        # правим таблицу главной страницы
        self.ui.tableWidget.verticalHeader().setVisible(False);
        self.ui.tableWidget.setColumnWidth(0, 100)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 80)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setColumnWidth(5, 100)

        self.ui.labelName.setText(self.login)
        # задаем дату сейчас
        self.qdate = QDate.currentDate()  # получили текущую
        self.ui.dateEditTable.setDate(self.qdate)

        # связываем событие нажатия на кнопку (таблица главной страницы)
        self.row_count = self.ui.tableWidget.rowCount()
        self.ui.pushButtonAddRow.clicked.connect(self.add_row)
        self.ui.pushButtonDelRow.clicked.connect(self.del_row)
        self.ui.pushButtonClear.clicked.connect(self.clear_row)
        # self.add_row()
        # self.add_row()
        # self.add_row()

    # ==============================================================================
    # запросы SQL
    def show_goal(self):
        self.goals_list = set(self.goals_list)
        try:
            # подключаемся к базе
            self.db = sqlite3.connect('../database.db')
            cursor = self.db.cursor()

            self.goals = cursor.execute('''SELECT goal FROM goals''')

            for i in self.goals.fetchall():
                for j in i:
                    self.goals_list.add(j)
            print('база - цели', self.goals_list)
            cursor.close()
            self.db.close()
        except sqlite3.Error as e:
            print('Error', e)

        self.goals_list = list(self.goals_list)
        for i in self.goals_list:
            if i == 'none':
                self.goals_list.remove('none')
                self.goals_list.insert(0, 'none')
    # ==============================================================================
    # страница Цели
    def add_goal(self):
        self.goal = Goal(self.login, self.qdate)
        self.ui.verticalLayout_goals.addWidget(self.goal)
        self.ui.verticalLayout_goals.setAlignment(Qt.AlignTop)

    # ==============================================================================
    def add_motivation(self):
        # переопределили список как множество
        self.show_goal()

        for title in self.goals_list:
            if 'none' not in title:
                self.motivation = Motivation(self.login, title)
                self.ui.verticalLayout_motivation.addWidget(self.motivation)
                self.ui.verticalLayout_motivation.setAlignment(Qt.AlignTop)

    def save_motivation(self):
        ...

    # =============================================================================
    # манипуляции с таблицей на главной странице

    def add_row(self):
        self.ui.tableWidget.insertRow(self.row_count)
        comboBox_priority = QComboBox()
        comboBox_status = QComboBox()
        self.comboBox_goals = QComboBox()

        comboBox_priority.addItems(['Low', 'Medium', 'High'])
        comboBox_status.addItems(['Not done', 'To do', 'Done'])
        self.show_goal()
        self.comboBox_goals.addItems(self.goals_list)
        self.ui.tableWidget.setCellWidget(self.row_count, 2, comboBox_priority)
        self.ui.tableWidget.setCellWidget(self.row_count, 3, comboBox_status)
        self.ui.tableWidget.setCellWidget(self.row_count, 4, self.comboBox_goals)
        self.row_count = self.ui.tableWidget.rowCount()

    def del_row(self):
        self.row = self.ui.tableWidget.currentRow()
        if self.row > -1:
            self.ui.tableWidget.removeRow(self.row)

    def clear_row(self):
        self.row_count = self.ui.tableWidget.rowCount()
        print(self.row_count)
        while self.row_count > -1:
            self.ui.tableWidget.removeRow(self.row_count)
            self.row_count -= 1

    # def update_table(self):
    #     try:
    #         # подключаемся к базе
    #         db = sqlite3.connect('../database.db')
    #         cursor = db.cursor()
    #
    #         # передаем функцию в SQL аргументы: 1-алиаса, 2-кол значений, 3 сама функция
    #         # db.create_function("coding_pass", 1, self.coding_pass)
    #
    #         self.task_list = cursor.executemany(
    #             '''SELECT date_task, goal_task, priority, goal FROM goals WHERE user_login == self.login''')
    #
    #         k = cursor.fetchall()
    #         db.commit()
    #         print('база', k)
    #         cursor.close()
    #         db.close()
    #     except sqlite3.Error as e:
    #         print('Error', e)

    # =============================================================================

    # =============================================================================
    # меню переход по вкладкам
    def menu_home(self):
        self.ui.pageGoals.hide()
        self.ui.pageAnalis.hide()
        self.ui.pageMotivation.hide()
        self.ui.pageHadit.hide()
        self.ui.pageEnglish.hide()
        self.ui.pageHome.show()

    def menu_goals(self):
        self.ui.pageHome.hide()
        self.ui.pageAnalis.hide()
        self.ui.pageMotivation.hide()
        self.ui.pageHadit.hide()
        self.ui.pageEnglish.hide()
        self.ui.pageGoals.show()

    def menu_analis(self):
        self.ui.pageHome.hide()
        self.ui.pageGoals.hide()
        self.ui.pageMotivation.hide()
        self.ui.pageHadit.hide()
        self.ui.pageEnglish.hide()
        self.ui.pageAnalis.show()

    def menu_motivation(self):
        self.ui.pageHome.hide()
        self.ui.pageGoals.hide()
        self.ui.pageAnalis.hide()
        self.ui.pageHadit.hide()
        self.ui.pageEnglish.hide()
        self.ui.pageMotivation.show()

    def menu_hadit(self):
        self.ui.pageHome.hide()
        self.ui.pageGoals.hide()
        self.ui.pageAnalis.hide()
        self.ui.pageMotivation.hide()
        self.ui.pageEnglish.hide()
        self.ui.pageHadit.show()

    def menu_english(self):
        self.ui.pageHome.hide()
        self.ui.pageGoals.hide()
        self.ui.pageAnalis.hide()
        self.ui.pageMotivation.hide()
        self.ui.pageHadit.hide()
        self.ui.pageEnglish.show()

    # =======================================================================


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

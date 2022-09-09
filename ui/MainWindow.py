import sys

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHeaderView, QComboBox
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.base_ui.ui_mainWindow import Ui_MainWindow
from ui.goal import Goal
from ui.motivation import Motivation

#  тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow, QWidget):

    def __init__(self, login='yyyyyyyyyyyyy'):
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

        # правим таблицу главной страницы
        self.ui.tableWidget.verticalHeader().setVisible(False);
        self.ui.tableWidget.setColumnWidth(0, 100)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 80)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setColumnWidth(5, 100)

        self.ui.labelName.setText(self.login)
        print(self.login)
        # задаем дату сейчас
        self.qdate = QDate.currentDate()  # получили текущую
        self.ui.dateEditTable.setDate(self.qdate)
        # self.ui.dateEditTable.calendarWidget()
        # self.ui.dateEditTable.calendarPopup()

        # связываем событие нажатия на кнопку (таблица главной страницы)
        self.row_count = self.ui.tableWidget.rowCount()
        self.ui.pushButtonAddRow.clicked.connect(self.add_row)
        self.ui.pushButtonDelRow.clicked.connect(self.del_row)
        self.ui.pushButtonClear.clicked.connect(self.clear_row)
        self.add_row()
        self.add_row()
        self.add_row()

        # задаем и удаляем цель(сразу добавляем мотивацию для каждой цели)
        self.ui.pushButton.clicked.connect(self.add_goal)
        #self.goal.pushButtonAddTasks.cliked.connect(self.add_tasks_calendar)

    # =============================================================================
    # манипуляции с таблицей на главной странице

    def add_row(self):
        self.ui.tableWidget.insertRow(self.row_count)
        comboBox_priority = QComboBox()
        comboBox_status = QComboBox()
        comboBox_goals = QComboBox()

        comboBox_priority.addItems(['Low', 'Medium', 'High'])
        comboBox_status.addItems(['Not done', 'To do', 'Done'])
        comboBox_goals.addItems(['none'])
        self.ui.tableWidget.setCellWidget(self.row_count, 2, comboBox_priority)
        self.ui.tableWidget.setCellWidget(self.row_count, 3, comboBox_status)
        self.ui.tableWidget.setCellWidget(self.row_count, 4, comboBox_goals)
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
    # страница Цели
    def add_goal(self):
        self.goal = Goal(self.login, self.qdate)
        self.ui.verticalLayout_goals.addWidget(self.goal)
        self.ui.verticalLayout_goals.setAlignment(Qt.AlignTop)

    def add_tasks_calendar(self):
        ...

    def add_motivation(self):
        ...

        # посадили таблицу на главную страницу(создали экземпляр класса/ и добавили его)
        # layout_table = QVBoxLayout()
        # self.tableMain = MainTableWidget()
        # layout_table.addWidget(self.tableMain)
        # layout_table.addStretch()
        # self.ui.pageHome.setLayout(layout_table)
        # self.ui.pageHome.show()


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

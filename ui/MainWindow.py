import sys

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHeaderView, QComboBox

from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide2extn.RoundProgressBar import roundProgressBar
from ui.base_ui.ui_mainWindow import Ui_MainWindow


#  тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pageHome.show()

        # правим таблицу главной страницы
        self.ui.tableWidget.verticalHeader().setVisible(False);
        self.ui.tableWidget.setColumnWidth(0, 100)
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 80)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setColumnWidth(5, 100)


        # задаем дату сейчас
        qdate = QDate.currentDate()  # получили текущую
        print(qdate)
        self.ui.dateEditTable.setDate(qdate)

        # связываем событие нажатия на кнопку (таблица главной страницы)
        self.row_count = self.ui.tableWidget.rowCount()
        self.ui.pushButtonAddRow.clicked.connect(self.add_row)
        self.ui.pushButtonDelRow.clicked.connect(self.del_row)
        self.ui.pushButtonClear.clicked.connect(self.clear_row)


    #=============================================================================
    # манипуляции с таблицей на главной странице

    def add_row(self):
        self.ui.tableWidget.insertRow(self.row_count)
        comboBox_priority = QComboBox()
        comboBox_status = QComboBox()
        comboBox_goals = QComboBox()

        comboBox_priority.addItems(['Low', 'Medium', 'Medium'])
        comboBox_status.addItems(['Not done', 'To do', 'Done'])
        comboBox_goals.addItems(['none'])
        self.ui.tableWidget.setCellWidget(self.row_count, 2, comboBox_priority)
        self.ui.tableWidget.setCellWidget(self.row_count, 3, comboBox_status)
        self.ui.tableWidget.setCellWidget(self.row_count, 4, comboBox_goals)
        self.row_count = self.ui.tableWidget.rowCount()

    def del_row(self):
        row = self.ui.tableWidget.currentRow()
        if row > -1:
            self.ui.tableWidget.removeRow(row)

    def clear_row(self):
        while self.row_count > -1:
            self.ui.tableWidget.removeRow(self.row_count)
            self.row_count -= 1

    # =============================================================================

        # посадили таблицу на главную страницу(создали экземпляр класса/ и добавили его)
        # layout_table = QVBoxLayout()
        # self.tableMain = MainTableWidget()
        # layout_table.addWidget(self.tableMain)
        # layout_table.addStretch()
        # self.ui.pageHome.setLayout(layout_table)
        # self.ui.pageHome.show()

        # self.ui.pushButtonGoals.clicked.connect(self.ui.pageGoals.show)
        # self.ui.pushButtonAnalis.clicked.connect(self.ui.pageAnalis.show)
        # self.ui.pushButtonMotivation.clicked.connect(self.ui.pageMotivation.show)
        # self.ui.pushButtonHome.clicked.connect(self.ui.pageHome.show)
        # self.ui.pushButtonHabit.clicked.connect(self.ui.pageHadit.show)
        # self.ui.pushButtonEnglish.clicked.connect(self.ui.pageEnglish.show)


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    # app.setStyleSheet(open('SpyBot.qss', 'r').read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

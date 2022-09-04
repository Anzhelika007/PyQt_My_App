# import sys
# from PySide6.QtWidgets import QApplication


from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

from ui.base_ui.ui_mainWindowTable import Ui_Form


class MainTableWidget(QWidget):

    def __init__(self, parent=None):
        super(MainTableWidget, self).__init__(parent)
        # создали экземпляр класса
        self.ui = Ui_Form()
        # подгрузили файл
        self.ui.setupUi(self)


        self.row_count = self.ui.tableWidget.rowCount()
        print(self.row_count)
        # связываем событие нажатия на кнопку
        self.ui.pushButtonAddRow.clicked.connect(self.add_row)
        self.ui.pushButtonDelRow.clicked.connect(self.del_row)
        self.ui.pushButtonClear.clicked.connect(self.clear_row)

    def add_row(self):
        self.ui.tableWidget.insertRow(self.row_count)
        self.row_count = self.ui.tableWidget.rowCount()

    def del_row(self):
        row = self.ui.tableWidget.currentRow()
        if row > -1:
            self.ui.tableWidget.removeRow(row)

    def clear_row(self):
        while self.row_count > -1:
            self.ui.tableWidget.removeRow(self.row_count)
            self.row_count -= 1

# if __name__ == '__main__':
#     app = QApplication()
#
#     #app.setStyleSheet(open('SpyBot.qss', 'r').read())
#     window = MainTableWidget()
#     window.show()
#     sys.exit(app.exec())
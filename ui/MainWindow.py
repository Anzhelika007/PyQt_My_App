# import sys
# from PySide6.QtWidgets import QApplication, QHBoxLayout,

from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from ui.base_ui.ui_mainWindow import Ui_MainWindow
from ui.MainWindowTable import MainTableWidget



# тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # посадили таблицу на главную страницу(создали экземпляр класса/ и добавили его)
        layout_table = QVBoxLayout()
        self.tableMain = MainTableWidget()
        layout_table.addWidget(self.tableMain)
        #layout.addStretch()
        self.ui.pageHome.setLayout(layout_table)








# if __name__ == '__main__':
#     app = QApplication()
#     #app.setStyleSheet(open('Obit.qss', 'r').read())
#     #app.setStyleSheet(open('SpyBot.qss', 'r').read())
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
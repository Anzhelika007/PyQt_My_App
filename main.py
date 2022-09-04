import sys
from PySide6.QtWidgets import QApplication

from ui.MainWindow import MainWindow
from ui.MainWindowTable import MainTableWidget


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('Obit.qss', 'r').read())
    #app.setStyleSheet(open('SpyBot.qss', 'r').read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

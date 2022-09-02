from PySide6.QtWidgets import QMainWindow
from ui.base_ui.ui_mainWindow import Ui_MainWindow



# тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

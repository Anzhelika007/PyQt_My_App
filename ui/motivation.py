import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, Signal

from ui.base_ui.ui_motivation import Ui_Form


class Motivation(QWidget):

    def __init__(self, login, title):
        super(Motivation, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.login = login
        self.title = title
        self.ui.labelTitle.setText(title)





if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('../Obit.qss', 'r').read())
    window = Motivation()
    window.show()
    sys.exit(app.exec())

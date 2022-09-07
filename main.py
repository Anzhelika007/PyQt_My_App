import sys
import time
import PySide6
from PySide6.QtGui import QMovie, QPixmap, QPainter
from PySide6.QtCore import QSize

from ui.MainWindow import MainWindow
from ui.registration import Regisrtation

import sqlite3
# шифруем пароль
import hashlib

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QSplashScreen, QProgressBar
from ui.base_ui.ui_registation import Ui_Form


# гиф
class MovieSplashScreen(QSplashScreen):
    my_size = QSize(800, 600)

    def __init__(self, path_to_gif: str):
        self.movie = QMovie(path_to_gif)
        self.movie.jumpToFrame(0)
        pixmap = QPixmap(self.my_size)
        QSplashScreen.__init__(self, pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        self.movie.start()

    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        self.movie.stop()

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        pixmap = pixmap.scaled(self.my_size)
        painter.drawPixmap(0, 0, pixmap)


# загрузка заставки и стартовой страницы
def start_app():

    progressbar_value = 30
    path_to_gif = 'gif/102.gif.'

    splash = MovieSplashScreen(path_to_gif)
    progressbar = QProgressBar(splash)
    progressbar.setMaximum(progressbar_value)
    progressbar.setTextVisible(False)
    # устанавливаем размеры прогрессбара
    progressbar.setGeometry(0, splash.my_size.height() - 50, splash.my_size.width(), 20)
    reg.hide()
    splash.show()

    for i in range(progressbar_value):
        progressbar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    time.sleep(0)
    window = MainWindow()
    window.show()
    splash.finish(window)


class Start_registration(QWidget):
    def __init__(self):
        super(Start_registration, self).__init__()
        self.start_app = start_app
        self.ui = Regisrtation()


    def start(self):
        self.ui.hide()
        self.start_app
            # progressbar_value = 30
            # path_to_gif = 'gif/102.gif.'
            #
            # splash = MovieSplashScreen(path_to_gif)
            # progressbar = QProgressBar(splash)
            # progressbar.setMaximum(progressbar_value)
            # progressbar.setTextVisible(False)
            # # устанавливаем размеры прогрессбара
            # progressbar.setGeometry(0, splash.my_size.height() - 50, splash.my_size.width(), 20)
            #
            # splash.show()
            #
            # for i in range(progressbar_value):
            #     progressbar.setValue(i)
            #     t = time.time()
            #     while time.time() < t + 0.1:
            #         app.processEvents()
            #
            # time.sleep(0)
            # window = MainWindow()
            # window.show()
            # splash.finish(window)


if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(open('Obit.qss', 'r').read())

    reg = Regisrtation()
    reg.show()

    # progressbar_value = 30
    # path_to_gif = 'gif/102.gif.'
    #
    # splash = MovieSplashScreen(path_to_gif)
    # progressbar = QProgressBar(splash)
    # progressbar.setMaximum(progressbar_value)
    # progressbar.setTextVisible(False)
    # # устанавливаем размеры прогрессбара
    # progressbar.setGeometry(0, splash.my_size.height() - 50, splash.my_size.width(), 20)
    #
    # splash.show()
    #
    # for i in range(progressbar_value):
    #     progressbar.setValue(i)
    #     t = time.time()
    #     while time.time() < t + 0.1:
    #         app.processEvents()
    #
    # time.sleep(0)
    # window = MainWindow()
    # window.show()
    # splash.finish(window)
    sys.exit(app.exec())

import PySide6
from PySide6.QtGui import QMovie, QPixmap, QPainter
from PySide6.QtWidgets import QApplication, QSplashScreen, QProgressBar, QWidget
from PySide6.QtCore import QSize

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
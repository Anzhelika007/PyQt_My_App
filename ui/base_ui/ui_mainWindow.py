# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(60, 40))
        self.pushButton_7.setMaximumSize(QSize(60, 40))
        icon = QIcon()
        icon.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))
        self.pushButton.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 50))
        self.pushButton_2.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 50))
        self.pushButton_3.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 50))
        self.pushButton_4.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 50))
        self.pushButton_5.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 50))
        self.pushButton_6.setMaximumSize(QSize(200, 150))

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.stackedWidget.addWidget(self.pageHome)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Analis", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Motivation", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Habit tracker", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Learning English", None))
    # retranslateUi


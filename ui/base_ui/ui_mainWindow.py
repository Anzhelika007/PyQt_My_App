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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 650)
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

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 3))
        self.lineEdit.setMaximumSize(QSize(16777215, 3))

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(220, 0))
        self.widget.setMaximumSize(QSize(220, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frameMenu = QFrame(self.frame_16)
        self.frameMenu.setObjectName(u"frameMenu")
        font1 = QFont()
        font1.setPointSize(16)
        self.frameMenu.setFont(font1)
        self.frameMenu.setStyleSheet(u"")
        self.frameMenu.setFrameShape(QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frameMenu)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 20, 0, 20)
        self.pushButtonHome = QPushButton(self.frameMenu)
        self.pushButtonHome.setObjectName(u"pushButtonHome")
        self.pushButtonHome.setMinimumSize(QSize(200, 80))
        self.pushButtonHome.setMaximumSize(QSize(200, 80))
        self.pushButtonHome.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonHome)

        self.pushButtonGoals = QPushButton(self.frameMenu)
        self.pushButtonGoals.setObjectName(u"pushButtonGoals")
        self.pushButtonGoals.setMinimumSize(QSize(200, 80))
        self.pushButtonGoals.setMaximumSize(QSize(200, 80))
        self.pushButtonGoals.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonGoals)

        self.pushButtonAnalis = QPushButton(self.frameMenu)
        self.pushButtonAnalis.setObjectName(u"pushButtonAnalis")
        self.pushButtonAnalis.setMinimumSize(QSize(200, 80))
        self.pushButtonAnalis.setMaximumSize(QSize(200, 80))
        self.pushButtonAnalis.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonAnalis)

        self.pushButtonMotivation = QPushButton(self.frameMenu)
        self.pushButtonMotivation.setObjectName(u"pushButtonMotivation")
        self.pushButtonMotivation.setMinimumSize(QSize(200, 80))
        self.pushButtonMotivation.setMaximumSize(QSize(200, 80))
        self.pushButtonMotivation.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonMotivation)

        self.pushButtonEnglish = QPushButton(self.frameMenu)
        self.pushButtonEnglish.setObjectName(u"pushButtonEnglish")
        self.pushButtonEnglish.setMinimumSize(QSize(200, 80))
        self.pushButtonEnglish.setMaximumSize(QSize(200, 80))
        self.pushButtonEnglish.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonEnglish)

        self.pushButtonHabit = QPushButton(self.frameMenu)
        self.pushButtonHabit.setObjectName(u"pushButtonHabit")
        self.pushButtonHabit.setMinimumSize(QSize(200, 80))
        self.pushButtonHabit.setMaximumSize(QSize(200, 80))
        self.pushButtonHabit.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButtonHabit)


        self.verticalLayout_14.addWidget(self.frameMenu, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.pageHome)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.pushButtonAddRow = QPushButton(self.frame_3)
        self.pushButtonAddRow.setObjectName(u"pushButtonAddRow")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddRow.sizePolicy().hasHeightForWidth())
        self.pushButtonAddRow.setSizePolicy(sizePolicy)
        self.pushButtonAddRow.setMinimumSize(QSize(120, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButtonAddRow.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButtonAddRow)

        self.pushButtonDelRow = QPushButton(self.frame_3)
        self.pushButtonDelRow.setObjectName(u"pushButtonDelRow")
        sizePolicy.setHeightForWidth(self.pushButtonDelRow.sizePolicy().hasHeightForWidth())
        self.pushButtonDelRow.setSizePolicy(sizePolicy)
        self.pushButtonDelRow.setMinimumSize(QSize(120, 40))
        self.pushButtonDelRow.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButtonDelRow)

        self.pushButtonClear = QPushButton(self.frame_3)
        self.pushButtonClear.setObjectName(u"pushButtonClear")
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        self.pushButtonClear.setMinimumSize(QSize(120, 40))
        self.pushButtonClear.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButtonClear)

        self.dateEditTable = QDateEdit(self.frame_3)
        self.dateEditTable.setObjectName(u"dateEditTable")
        self.dateEditTable.setMinimumSize(QSize(150, 40))
        self.dateEditTable.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_3.addWidget(self.dateEditTable)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(99)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setFont(font1)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 8)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.pageHome)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_11.addWidget(self.label_2)

        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(100, 0))
        self.progressBar.setValue(80)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.progressBar)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalLayout_4.setStretch(0, 7)
        self.verticalLayout_4.setStretch(1, 4)
        self.stackedWidget.addWidget(self.pageHome)
        self.pageGoals = QWidget()
        self.pageGoals.setObjectName(u"pageGoals")
        self.verticalLayout_6 = QVBoxLayout(self.pageGoals)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pageGoals)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMinimumSize(QSize(0, 80))
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 20, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.pageGoals)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 20, 0)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.textBrowser_2 = QTextBrowser(self.frame_14)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_12.addWidget(self.textBrowser_2)

        self.verticalLayout_12.setStretch(0, 3)
        self.verticalLayout_12.setStretch(1, 7)

        self.verticalLayout_13.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_15)

        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 5)

        self.verticalLayout_6.addWidget(self.frame_8)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 8)
        self.stackedWidget.addWidget(self.pageGoals)
        self.pageAnalis = QWidget()
        self.pageAnalis.setObjectName(u"pageAnalis")
        self.stackedWidget.addWidget(self.pageAnalis)
        self.pageMotivation = QWidget()
        self.pageMotivation.setObjectName(u"pageMotivation")
        self.verticalLayout_7 = QVBoxLayout(self.pageMotivation)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.pageMotivation)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.pageMotivation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 55, 16))
        self.textBrowser = QTextBrowser(self.frame_9)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 30, 451, 61))

        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.pageMotivation)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_11)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 7)
        self.stackedWidget.addWidget(self.pageMotivation)
        self.pageHadit = QWidget()
        self.pageHadit.setObjectName(u"pageHadit")
        self.verticalLayout_9 = QVBoxLayout(self.pageHadit)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.pageHadit)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.dateEdit = QDateEdit(self.frame_12)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_6.addWidget(self.dateEdit)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.calendarWidget = QCalendarWidget(self.frame_12)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_10.addWidget(self.calendarWidget)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.pageHadit)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 101, 21))
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 50, 81, 31))
        self.dateEdit_2 = QDateEdit(self.frame_13)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(100, 60, 90, 22))
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 60, 81, 21))
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(320, 50, 81, 31))

        self.verticalLayout_9.addWidget(self.frame_13)

        self.verticalLayout_9.setStretch(0, 6)
        self.verticalLayout_9.setStretch(1, 4)
        self.stackedWidget.addWidget(self.pageHadit)
        self.pageEnglish = QWidget()
        self.pageEnglish.setObjectName(u"pageEnglish")
        self.stackedWidget.addWidget(self.pageEnglish)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

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
        self.pushButtonHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButtonGoals.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.pushButtonAnalis.setText(QCoreApplication.translate("MainWindow", u"Analis", None))
        self.pushButtonMotivation.setText(QCoreApplication.translate("MainWindow", u"Motivation", None))
        self.pushButtonEnglish.setText(QCoreApplication.translate("MainWindow", u"Learning English", None))
        self.pushButtonHabit.setText(QCoreApplication.translate("MainWindow", u"Habit tracker", None))
        self.pushButtonAddRow.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButtonDelRow.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.pushButtonClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Priority", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Goals", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0436\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u043b\u043e", None))
    # retranslateUi


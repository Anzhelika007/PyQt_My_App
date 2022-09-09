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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 660)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_20 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(60, 40))
        self.pushButton_7.setMaximumSize(QSize(60, 40))
        icon = QIcon()
        icon.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_20.addWidget(self.frame)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 3))
        self.lineEdit.setMaximumSize(QSize(16777215, 3))

        self.verticalLayout_20.addWidget(self.lineEdit)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
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
        self.widget_2.setMaximumSize(QSize(1677215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.pageHome.setMaximumSize(QSize(16777215, 16777215))
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
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 30, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_2)

        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(100, 40))
        self.progressBar.setFont(font3)
        self.progressBar.setValue(80)
        self.progressBar.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.progressBar.setTextVisible(True)
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
        self.verticalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.frame_7 = QFrame(self.pageGoals)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMinimumSize(QSize(560, 80))
        self.frame_7.setMaximumSize(QSize(580, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        self.pushButton.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.pushButton_2.setFont(font4)

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)

        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.pageGoals)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(580, 0))
        self.frame_8.setMaximumSize(QSize(580, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_17)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(69, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.dateEdit = QDateEdit(self.frame_14)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_7.addWidget(self.dateEdit)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.dateEdit_3 = QDateEdit(self.frame_14)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.horizontalLayout_7.addWidget(self.dateEdit_3)

        self.pushButton_12 = QPushButton(self.frame_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)

        self.horizontalLayout_7.addWidget(self.pushButton_12)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.frame_27 = QFrame(self.frame_17)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_27)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setMaximumSize(QSize(800, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lineEditGoal = QLineEdit(self.frame_18)
        self.lineEditGoal.setObjectName(u"lineEditGoal")
        self.lineEditGoal.setMinimumSize(QSize(0, 30))
        self.lineEditGoal.setMaximumSize(QSize(800, 16777215))
        self.lineEditGoal.setFont(font)

        self.verticalLayout_16.addWidget(self.lineEditGoal)

        self.lineEditTask3 = QLineEdit(self.frame_18)
        self.lineEditTask3.setObjectName(u"lineEditTask3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEditTask3.sizePolicy().hasHeightForWidth())
        self.lineEditTask3.setSizePolicy(sizePolicy3)
        self.lineEditTask3.setMinimumSize(QSize(0, 30))
        self.lineEditTask3.setMaximumSize(QSize(800, 16777215))
        self.lineEditTask3.setFont(font)

        self.verticalLayout_16.addWidget(self.lineEditTask3)

        self.lineEditTask1 = QLineEdit(self.frame_18)
        self.lineEditTask1.setObjectName(u"lineEditTask1")
        self.lineEditTask1.setMinimumSize(QSize(0, 30))
        self.lineEditTask1.setMaximumSize(QSize(800, 16777215))
        self.lineEditTask1.setFont(font)

        self.verticalLayout_16.addWidget(self.lineEditTask1)

        self.lineEditTask2 = QLineEdit(self.frame_18)
        self.lineEditTask2.setObjectName(u"lineEditTask2")
        self.lineEditTask2.setMinimumSize(QSize(0, 30))
        self.lineEditTask2.setMaximumSize(QSize(800, 16777215))
        self.lineEditTask2.setFont(font)

        self.verticalLayout_16.addWidget(self.lineEditTask2)


        self.horizontalLayout_14.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_27)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(200, 16777215))
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_6 = QFrame(self.frame_19)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkBox_5 = QCheckBox(self.frame_6)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMaximumSize(QSize(30, 30))
        self.checkBox_5.setText(u"")
        self.checkBox_5.setIconSize(QSize(30, 30))
        self.checkBox_5.setTristate(True)

        self.horizontalLayout_8.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.frame_6)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMaximumSize(QSize(30, 30))
        self.checkBox_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox_4)

        self.checkBox_22 = QCheckBox(self.frame_6)
        self.checkBox_22.setObjectName(u"checkBox_22")
        self.checkBox_22.setMaximumSize(QSize(30, 30))
        self.checkBox_22.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox_22)

        self.checkBox_6 = QCheckBox(self.frame_6)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setMaximumSize(QSize(30, 30))
        self.checkBox_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox_6)

        self.checkBox_3 = QCheckBox(self.frame_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(30, 30))
        self.checkBox_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.frame_6)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(30, 30))
        self.checkBox_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(30, 30))
        self.checkBox.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.checkBox)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.checkBox_23 = QCheckBox(self.frame_22)
        self.checkBox_23.setObjectName(u"checkBox_23")
        self.checkBox_23.setMaximumSize(QSize(30, 30))
        self.checkBox_23.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_23)

        self.checkBox_8 = QCheckBox(self.frame_22)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setMaximumSize(QSize(30, 30))
        self.checkBox_8.setText(u"")
        self.checkBox_8.setIconSize(QSize(30, 30))
        self.checkBox_8.setTristate(True)

        self.horizontalLayout_9.addWidget(self.checkBox_8)

        self.checkBox_10 = QCheckBox(self.frame_22)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setMaximumSize(QSize(30, 30))
        self.checkBox_10.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.frame_22)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setMaximumSize(QSize(30, 30))
        self.checkBox_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.frame_22)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setMaximumSize(QSize(30, 30))
        self.checkBox_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_12)

        self.checkBox_13 = QCheckBox(self.frame_22)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setMaximumSize(QSize(30, 30))
        self.checkBox_13.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.frame_22)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setMaximumSize(QSize(30, 30))
        self.checkBox_14.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.checkBox_14)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox_24 = QCheckBox(self.frame_23)
        self.checkBox_24.setObjectName(u"checkBox_24")
        self.checkBox_24.setMaximumSize(QSize(30, 30))
        self.checkBox_24.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_24)

        self.checkBox_15 = QCheckBox(self.frame_23)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setMaximumSize(QSize(30, 30))
        self.checkBox_15.setText(u"")
        self.checkBox_15.setIconSize(QSize(30, 30))
        self.checkBox_15.setTristate(True)

        self.horizontalLayout_10.addWidget(self.checkBox_15)

        self.checkBox_17 = QCheckBox(self.frame_23)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setMaximumSize(QSize(30, 30))
        self.checkBox_17.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_17)

        self.checkBox_18 = QCheckBox(self.frame_23)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setMaximumSize(QSize(30, 30))
        self.checkBox_18.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_18)

        self.checkBox_19 = QCheckBox(self.frame_23)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setMaximumSize(QSize(30, 30))
        self.checkBox_19.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_19)

        self.checkBox_20 = QCheckBox(self.frame_23)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setMaximumSize(QSize(30, 30))
        self.checkBox_20.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_20)

        self.checkBox_21 = QCheckBox(self.frame_23)
        self.checkBox_21.setObjectName(u"checkBox_21")
        self.checkBox_21.setMaximumSize(QSize(30, 30))
        self.checkBox_21.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.checkBox_21)


        self.verticalLayout_12.addWidget(self.frame_23)


        self.horizontalLayout_14.addWidget(self.frame_19)


        self.verticalLayout_13.addWidget(self.frame_27)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_28 = QFrame(self.frame_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_28)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 6)

        self.verticalLayout_6.addWidget(self.frame_8)

        self.verticalLayout_6.setStretch(0, 5)
        self.stackedWidget.addWidget(self.pageGoals)
        self.pageAnalis = QWidget()
        self.pageAnalis.setObjectName(u"pageAnalis")
        self.stackedWidget.addWidget(self.pageAnalis)
        self.pageMotivation = QWidget()
        self.pageMotivation.setObjectName(u"pageMotivation")
        self.verticalLayout_7 = QVBoxLayout(self.pageMotivation)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.frame_10 = QFrame(self.pageMotivation)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_5.setFont(font5)

        self.verticalLayout_8.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.pageMotivation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 30, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setFont(font)

        self.verticalLayout_17.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 90))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.lineEdit_2)


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
        self.frame_12.setMaximumSize(QSize(1660, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.calendarWidget = QCalendarWidget(self.frame_12)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(500, 0))
        self.calendarWidget.setMaximumSize(QSize(500, 16777215))

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

        self.verticalLayout_9.setStretch(1, 4)
        self.stackedWidget.addWidget(self.pageHadit)
        self.pageEnglish = QWidget()
        self.pageEnglish.setObjectName(u"pageEnglish")
        self.verticalLayout_18 = QVBoxLayout(self.pageEnglish)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 10, 0)
        self.widget_3 = QWidget(self.pageEnglish)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.widget_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 15, 0)
        self.frame_25 = QFrame(self.frame_15)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.pushButton_3 = QPushButton(self.frame_25)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_12.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_25)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setFont(font2)

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_25)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font2)

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_25)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setFont(font2)

        self.horizontalLayout_12.addWidget(self.pushButton_6)


        self.verticalLayout_19.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.pushButton_8 = QPushButton(self.frame_26)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        self.pushButton_8.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_26)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 50))
        self.pushButton_9.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.pushButton_11 = QPushButton(self.frame_26)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 50))
        self.pushButton_11.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_26)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 50))
        self.pushButton_10.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pushButton_10)


        self.verticalLayout_19.addWidget(self.frame_26)


        self.verticalLayout.addWidget(self.frame_15)

        self.frame_21 = QFrame(self.widget_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_21)

        self.frame_24 = QFrame(self.widget_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_24)


        self.verticalLayout_18.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.pageEnglish)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(1, 7)

        self.verticalLayout_20.addWidget(self.frame_2)

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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Progress Today", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Write the main goals (preferably no more than 3)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lineEditGoal.setText("")
        self.lineEditGoal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your goal", None))
        self.lineEditTask3.setText("")
        self.lineEditTask3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task 1", None))
        self.lineEditTask1.setText("")
        self.lineEditTask1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task 2", None))
        self.lineEditTask2.setText("")
        self.lineEditTask2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task 3", None))
        self.label_11.setText("")
        self.checkBox_22.setText("")
        self.checkBox_6.setText("")
        self.checkBox_3.setText("")
        self.checkBox_2.setText("")
        self.checkBox.setText("")
        self.checkBox_23.setText("")
        self.checkBox_11.setText("")
        self.checkBox_12.setText("")
        self.checkBox_13.setText("")
        self.checkBox_14.setText("")
        self.checkBox_24.setText("")
        self.checkBox_18.setText("")
        self.checkBox_19.setText("")
        self.checkBox_20.setText("")
        self.checkBox_21.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"What will you get by reaching the goal?", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write down your highest expectations", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0436\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u043b\u043e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Verbs", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


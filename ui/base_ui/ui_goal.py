# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_goal.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(669, 230)
        Form.setMinimumSize(QSize(0, 222))
        Form.setMaximumSize(QSize(16777215, 230))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.goals = QFrame(Form)
        self.goals.setObjectName(u"goals")
        self.goals.setMinimumSize(QSize(580, 200))
        self.goals.setMaximumSize(QSize(1000, 200))
        self.goals.setFrameShape(QFrame.StyledPanel)
        self.goals.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.goals)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.goals)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_40)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(160, 30))
        self.frame_41.setMaximumSize(QSize(700, 60))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_41)
        self.label_29.setObjectName(u"label_29")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setWordWrap(False)

        self.horizontalLayout_21.addWidget(self.label_29)

        self.horizontalSpacer_9 = QSpacerItem(69, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_9)

        self.label_30 = QLabel(self.frame_41)
        self.label_30.setObjectName(u"label_30")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_30.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_30)

        self.dateEdit_6 = QDateEdit(self.frame_41)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setMinimumSize(QSize(100, 0))
        self.dateEdit_6.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.dateEdit_6)

        self.label_31 = QLabel(self.frame_41)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_31)

        self.dateEdit_7 = QDateEdit(self.frame_41)
        self.dateEdit_7.setObjectName(u"dateEdit_7")
        self.dateEdit_7.setMinimumSize(QSize(100, 0))
        self.dateEdit_7.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.dateEdit_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_10)

        self.pushButtonAddTasks = QPushButton(self.frame_41)
        self.pushButtonAddTasks.setObjectName(u"pushButtonAddTasks")
        self.pushButtonAddTasks.setMinimumSize(QSize(100, 0))
        self.pushButtonAddTasks.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButtonAddTasks.setFont(font2)

        self.horizontalLayout_21.addWidget(self.pushButtonAddTasks)


        self.verticalLayout_23.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMaximumSize(QSize(800, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_43)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_43)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditGoal_4 = QLineEdit(self.frame)
        self.lineEditGoal_4.setObjectName(u"lineEditGoal_4")
        sizePolicy.setHeightForWidth(self.lineEditGoal_4.sizePolicy().hasHeightForWidth())
        self.lineEditGoal_4.setSizePolicy(sizePolicy)
        self.lineEditGoal_4.setMinimumSize(QSize(0, 30))
        self.lineEditGoal_4.setMaximumSize(QSize(800, 30))
        font3 = QFont()
        font3.setPointSize(14)
        self.lineEditGoal_4.setFont(font3)

        self.horizontalLayout.addWidget(self.lineEditGoal_4)

        self.comboBoxPriority = QComboBox(self.frame)
        self.comboBoxPriority.setObjectName(u"comboBoxPriority")
        self.comboBoxPriority.setMinimumSize(QSize(50, 30))
        self.comboBoxPriority.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.comboBoxPriority)


        self.verticalLayout_2.addWidget(self.frame)

        self.lineEditTask_1 = QLineEdit(self.frame_43)
        self.lineEditTask_1.setObjectName(u"lineEditTask_1")
        sizePolicy.setHeightForWidth(self.lineEditTask_1.sizePolicy().hasHeightForWidth())
        self.lineEditTask_1.setSizePolicy(sizePolicy)
        self.lineEditTask_1.setMinimumSize(QSize(0, 20))
        self.lineEditTask_1.setMaximumSize(QSize(800, 25))
        self.lineEditTask_1.setFont(font3)

        self.verticalLayout_2.addWidget(self.lineEditTask_1)

        self.lineEditTask_2 = QLineEdit(self.frame_43)
        self.lineEditTask_2.setObjectName(u"lineEditTask_2")
        sizePolicy.setHeightForWidth(self.lineEditTask_2.sizePolicy().hasHeightForWidth())
        self.lineEditTask_2.setSizePolicy(sizePolicy)
        self.lineEditTask_2.setMinimumSize(QSize(0, 20))
        self.lineEditTask_2.setMaximumSize(QSize(800, 25))
        self.lineEditTask_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.lineEditTask_2)

        self.lineEditTask_3 = QLineEdit(self.frame_43)
        self.lineEditTask_3.setObjectName(u"lineEditTask_3")
        sizePolicy.setHeightForWidth(self.lineEditTask_3.sizePolicy().hasHeightForWidth())
        self.lineEditTask_3.setSizePolicy(sizePolicy)
        self.lineEditTask_3.setMinimumSize(QSize(0, 20))
        self.lineEditTask_3.setMaximumSize(QSize(800, 25))
        self.lineEditTask_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.lineEditTask_3)


        self.horizontalLayout_22.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(200, 16777215))
        self.frame_44.setFrameShape(QFrame.Box)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_44)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frameTaskDay = QFrame(self.frame_44)
        self.frameTaskDay.setObjectName(u"frameTaskDay")
        self.frameTaskDay.setFrameShape(QFrame.StyledPanel)
        self.frameTaskDay.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frameTaskDay)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frameTaskDay)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_23.addWidget(self.label_32)

        self.label_33 = QLabel(self.frameTaskDay)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_23.addWidget(self.label_33)

        self.label_34 = QLabel(self.frameTaskDay)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_23.addWidget(self.label_34)

        self.label_35 = QLabel(self.frameTaskDay)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_23.addWidget(self.label_35)

        self.label_36 = QLabel(self.frameTaskDay)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_23.addWidget(self.label_36)

        self.label_37 = QLabel(self.frameTaskDay)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.frameTaskDay)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_23.addWidget(self.label_38)


        self.verticalLayout_25.addWidget(self.frameTaskDay)

        self.frameTask1 = QFrame(self.frame_44)
        self.frameTask1.setObjectName(u"frameTask1")
        self.frameTask1.setFrameShape(QFrame.StyledPanel)
        self.frameTask1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frameTask1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.checkBoxMon1 = QCheckBox(self.frameTask1)
        self.checkBoxMon1.setObjectName(u"checkBoxMon1")
        self.checkBoxMon1.setMaximumSize(QSize(30, 30))
        self.checkBoxMon1.setText(u"")
        self.checkBoxMon1.setIconSize(QSize(30, 30))
        self.checkBoxMon1.setTristate(True)

        self.horizontalLayout_24.addWidget(self.checkBoxMon1)

        self.checkBoxTue1 = QCheckBox(self.frameTask1)
        self.checkBoxTue1.setObjectName(u"checkBoxTue1")
        self.checkBoxTue1.setMaximumSize(QSize(30, 30))
        self.checkBoxTue1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxTue1)

        self.checkBoxWed1 = QCheckBox(self.frameTask1)
        self.checkBoxWed1.setObjectName(u"checkBoxWed1")
        self.checkBoxWed1.setMaximumSize(QSize(30, 30))
        self.checkBoxWed1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxWed1)

        self.checkBoxThu1 = QCheckBox(self.frameTask1)
        self.checkBoxThu1.setObjectName(u"checkBoxThu1")
        self.checkBoxThu1.setMaximumSize(QSize(30, 30))
        self.checkBoxThu1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxThu1)

        self.checkBoxFri1 = QCheckBox(self.frameTask1)
        self.checkBoxFri1.setObjectName(u"checkBoxFri1")
        self.checkBoxFri1.setMaximumSize(QSize(30, 30))
        self.checkBoxFri1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxFri1)

        self.checkBoxSat1 = QCheckBox(self.frameTask1)
        self.checkBoxSat1.setObjectName(u"checkBoxSat1")
        self.checkBoxSat1.setMaximumSize(QSize(30, 30))
        self.checkBoxSat1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxSat1)

        self.checkBoxSun1 = QCheckBox(self.frameTask1)
        self.checkBoxSun1.setObjectName(u"checkBoxSun1")
        self.checkBoxSun1.setMaximumSize(QSize(30, 30))
        self.checkBoxSun1.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.checkBoxSun1)


        self.verticalLayout_25.addWidget(self.frameTask1)

        self.frameTask2 = QFrame(self.frame_44)
        self.frameTask2.setObjectName(u"frameTask2")
        self.frameTask2.setFrameShape(QFrame.StyledPanel)
        self.frameTask2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frameTask2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.checkBoxMon2 = QCheckBox(self.frameTask2)
        self.checkBoxMon2.setObjectName(u"checkBoxMon2")
        self.checkBoxMon2.setMaximumSize(QSize(30, 30))
        self.checkBoxMon2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxMon2)

        self.checkBoxTue2 = QCheckBox(self.frameTask2)
        self.checkBoxTue2.setObjectName(u"checkBoxTue2")
        self.checkBoxTue2.setMaximumSize(QSize(30, 30))
        self.checkBoxTue2.setText(u"")
        self.checkBoxTue2.setIconSize(QSize(30, 30))
        self.checkBoxTue2.setTristate(True)

        self.horizontalLayout_25.addWidget(self.checkBoxTue2)

        self.checkBoxWed2 = QCheckBox(self.frameTask2)
        self.checkBoxWed2.setObjectName(u"checkBoxWed2")
        self.checkBoxWed2.setMaximumSize(QSize(30, 30))
        self.checkBoxWed2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxWed2)

        self.checkBoxThu2 = QCheckBox(self.frameTask2)
        self.checkBoxThu2.setObjectName(u"checkBoxThu2")
        self.checkBoxThu2.setMaximumSize(QSize(30, 30))
        self.checkBoxThu2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxThu2)

        self.checkBoxFri2 = QCheckBox(self.frameTask2)
        self.checkBoxFri2.setObjectName(u"checkBoxFri2")
        self.checkBoxFri2.setMaximumSize(QSize(30, 30))
        self.checkBoxFri2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxFri2)

        self.checkBoxSat2 = QCheckBox(self.frameTask2)
        self.checkBoxSat2.setObjectName(u"checkBoxSat2")
        self.checkBoxSat2.setMaximumSize(QSize(30, 30))
        self.checkBoxSat2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxSat2)

        self.checkBoxSun2 = QCheckBox(self.frameTask2)
        self.checkBoxSun2.setObjectName(u"checkBoxSun2")
        self.checkBoxSun2.setMaximumSize(QSize(30, 30))
        self.checkBoxSun2.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.checkBoxSun2)


        self.verticalLayout_25.addWidget(self.frameTask2)

        self.frameTask3 = QFrame(self.frame_44)
        self.frameTask3.setObjectName(u"frameTask3")
        self.frameTask3.setFrameShape(QFrame.StyledPanel)
        self.frameTask3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frameTask3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.checkBoxMon3 = QCheckBox(self.frameTask3)
        self.checkBoxMon3.setObjectName(u"checkBoxMon3")
        self.checkBoxMon3.setMaximumSize(QSize(30, 30))
        self.checkBoxMon3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxMon3)

        self.checkBoxTue3 = QCheckBox(self.frameTask3)
        self.checkBoxTue3.setObjectName(u"checkBoxTue3")
        self.checkBoxTue3.setMaximumSize(QSize(30, 30))
        self.checkBoxTue3.setText(u"")
        self.checkBoxTue3.setIconSize(QSize(30, 30))
        self.checkBoxTue3.setTristate(True)

        self.horizontalLayout_26.addWidget(self.checkBoxTue3)

        self.checkBoxWed3 = QCheckBox(self.frameTask3)
        self.checkBoxWed3.setObjectName(u"checkBoxWed3")
        self.checkBoxWed3.setMaximumSize(QSize(30, 30))
        self.checkBoxWed3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxWed3)

        self.checkBoxThu3 = QCheckBox(self.frameTask3)
        self.checkBoxThu3.setObjectName(u"checkBoxThu3")
        self.checkBoxThu3.setMaximumSize(QSize(30, 30))
        self.checkBoxThu3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxThu3)

        self.checkBoxFri3 = QCheckBox(self.frameTask3)
        self.checkBoxFri3.setObjectName(u"checkBoxFri3")
        self.checkBoxFri3.setMaximumSize(QSize(30, 30))
        self.checkBoxFri3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxFri3)

        self.checkBoxSat3 = QCheckBox(self.frameTask3)
        self.checkBoxSat3.setObjectName(u"checkBoxSat3")
        self.checkBoxSat3.setMaximumSize(QSize(30, 30))
        self.checkBoxSat3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxSat3)

        self.checkBoxSun3 = QCheckBox(self.frameTask3)
        self.checkBoxSun3.setObjectName(u"checkBoxSun3")
        self.checkBoxSun3.setMaximumSize(QSize(30, 30))
        self.checkBoxSun3.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.checkBoxSun3)


        self.verticalLayout_25.addWidget(self.frameTask3)


        self.horizontalLayout_22.addWidget(self.frame_44)


        self.verticalLayout_23.addWidget(self.frame_42)


        self.verticalLayout_29.addWidget(self.frame_40)


        self.verticalLayout.addWidget(self.goals)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Achievement period", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"start", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"end", None))
        self.pushButtonAddTasks.setText(QCoreApplication.translate("Form", u"Start", None))
        self.lineEditGoal_4.setText("")
        self.lineEditGoal_4.setPlaceholderText(QCoreApplication.translate("Form", u"Your goal", None))
        self.lineEditTask_1.setText("")
        self.lineEditTask_1.setPlaceholderText(QCoreApplication.translate("Form", u"Task 1", None))
        self.lineEditTask_2.setText("")
        self.lineEditTask_2.setPlaceholderText(QCoreApplication.translate("Form", u"Task 2", None))
        self.lineEditTask_3.setText("")
        self.lineEditTask_3.setPlaceholderText(QCoreApplication.translate("Form", u"Task 3", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Mon", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Tue", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Wed", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Thu", None))
        self.label_36.setText(QCoreApplication.translate("Form", u" Fri", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Sat", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Sun", None))
        self.checkBoxWed1.setText("")
        self.checkBoxThu1.setText("")
        self.checkBoxFri1.setText("")
        self.checkBoxSat1.setText("")
        self.checkBoxSun1.setText("")
        self.checkBoxMon2.setText("")
        self.checkBoxThu2.setText("")
        self.checkBoxFri2.setText("")
        self.checkBoxSat2.setText("")
        self.checkBoxSun2.setText("")
        self.checkBoxMon3.setText("")
        self.checkBoxThu3.setText("")
        self.checkBoxFri3.setText("")
        self.checkBoxSat3.setText("")
        self.checkBoxSun3.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_motivation.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(570, 149)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 30, 0)
        self.labelTitle = QLabel(self.frame_9)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setMinimumSize(QSize(30, 0))
        font = QFont()
        font.setPointSize(14)
        self.labelTitle.setFont(font)

        self.verticalLayout_17.addWidget(self.labelTitle)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 90))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.frame_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("Form", u"Q", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Write down your highest expectations", None))
    # retranslateUi


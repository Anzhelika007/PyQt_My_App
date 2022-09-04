# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindowTable.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(651, 219)
        font = QFont()
        font.setPointSize(14)
        Form.setFont(font)
        self.tableWidget = QTableWidget(Form)
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
        self.tableWidget.setGeometry(QRect(10, 70, 631, 141))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 411, 51))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.pushButtonAddRow = QPushButton(self.widget)
        self.pushButtonAddRow.setObjectName(u"pushButtonAddRow")
        self.pushButtonAddRow.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pushButtonAddRow)

        self.pushButtonDelRow = QPushButton(self.widget)
        self.pushButtonDelRow.setObjectName(u"pushButtonDelRow")
        self.pushButtonDelRow.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pushButtonDelRow)

        self.pushButtonClear = QPushButton(self.widget)
        self.pushButtonClear.setObjectName(u"pushButtonClear")
        self.pushButtonClear.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pushButtonClear)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Data", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Task", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Priority", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Goals", None));
        self.pushButtonAddRow.setText(QCoreApplication.translate("Form", u"Add", None))
        self.pushButtonDelRow.setText(QCoreApplication.translate("Form", u"Del", None))
        self.pushButtonClear.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi


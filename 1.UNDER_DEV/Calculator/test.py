# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RCalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorBYyRon(object):
    def setupUi(self, CalculatorBYyRon):
        CalculatorBYyRon.setObjectName("CalculatorBYyRon")
        CalculatorBYyRon.resize(484, 577)
        CalculatorBYyRon.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.gridLayoutWidget = QtWidgets.QWidget(CalculatorBYyRon)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.push_Equals = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Equals.sizePolicy().hasHeightForWidth())
        self.push_Equals.setSizePolicy(sizePolicy)
        self.push_Equals.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(193, 193, 193);\n"
"\n"
"}")
        self.push_Equals.setObjectName("push_Equals")
        self.gridLayout.addWidget(self.push_Equals, 6, 3, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 5, 1, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 3, 0, 1, 1)
        self.push_Multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Multiply.sizePolicy().hasHeightForWidth())
        self.push_Multiply.setSizePolicy(sizePolicy)
        self.push_Multiply.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.push_Multiply.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(193, 193, 193);\n"
"\n"
"}")
        self.push_Multiply.setObjectName("push_Multiply")
        self.gridLayout.addWidget(self.push_Multiply, 4, 3, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 3, 2, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 4, 0, 1, 1)
        self.push_Divide = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Divide.sizePolicy().hasHeightForWidth())
        self.push_Divide.setSizePolicy(sizePolicy)
        self.push_Divide.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(193, 193, 193);\n"
"\n"
"}")
        self.push_Divide.setObjectName("push_Divide")
        self.gridLayout.addWidget(self.push_Divide, 5, 3, 1, 1)
        self.push_Subtract = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Subtract.sizePolicy().hasHeightForWidth())
        self.push_Subtract.setSizePolicy(sizePolicy)
        self.push_Subtract.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(193, 193, 193);\n"
"\n"
"}")
        self.push_Subtract.setObjectName("push_Subtract")
        self.gridLayout.addWidget(self.push_Subtract, 3, 3, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 4, 2, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 5, 2, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 4, 1, 1, 1)
        self.push_Add = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Add.sizePolicy().hasHeightForWidth())
        self.push_Add.setSizePolicy(sizePolicy)
        self.push_Add.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(193, 193, 193);\n"
"\n"
"}")
        self.push_Add.setObjectName("push_Add")
        self.gridLayout.addWidget(self.push_Add, 2, 3, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 5, 0, 1, 1)
        self.push_Del = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Del.sizePolicy().hasHeightForWidth())
        self.push_Del.setSizePolicy(sizePolicy)
        self.push_Del.setStyleSheet("QPushButton {\n"
"    font: 75 23pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 39px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_Del.setObjectName("push_Del")
        self.gridLayout.addWidget(self.push_Del, 2, 2, 1, 1)
        self.push_Dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Dot.sizePolicy().hasHeightForWidth())
        self.push_Dot.setSizePolicy(sizePolicy)
        self.push_Dot.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_Dot.setObjectName("push_Dot")
        self.gridLayout.addWidget(self.push_Dot, 6, 2, 1, 1)
        self.push_Clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_Clear.sizePolicy().hasHeightForWidth())
        self.push_Clear.setSizePolicy(sizePolicy)
        self.push_Clear.setStyleSheet("QPushButton {\n"
"    font: 75 23pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 39px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_Clear.setObjectName("push_Clear")
        self.gridLayout.addWidget(self.push_Clear, 2, 0, 1, 2)
        self.push_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 6, 0, 1, 2)
        self.push_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton {\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 38px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 35pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4, QtCore.Qt.AlignRight)

        self.retranslateUi(CalculatorBYyRon)
        QtCore.QMetaObject.connectSlotsByName(CalculatorBYyRon)

    def retranslateUi(self, CalculatorBYyRon):
        _translate = QtCore.QCoreApplication.translate
        CalculatorBYyRon.setWindowTitle(_translate("CalculatorBYyRon", "CalculatorByRON"))
        self.push_Equals.setText(_translate("CalculatorBYyRon", "="))
        self.push_Equals.setShortcut(_translate("CalculatorBYyRon", "="))
        self.push_8.setText(_translate("CalculatorBYyRon", "8"))
        self.push_8.setShortcut(_translate("CalculatorBYyRon", "8"))
        self.push_1.setText(_translate("CalculatorBYyRon", "1"))
        self.push_1.setShortcut(_translate("CalculatorBYyRon", "1"))
        self.push_Multiply.setText(_translate("CalculatorBYyRon", "*"))
        self.push_Multiply.setShortcut(_translate("CalculatorBYyRon", "*"))
        self.push_3.setText(_translate("CalculatorBYyRon", "3"))
        self.push_3.setShortcut(_translate("CalculatorBYyRon", "3"))
        self.push_4.setText(_translate("CalculatorBYyRon", "4"))
        self.push_4.setShortcut(_translate("CalculatorBYyRon", "4"))
        self.push_Divide.setText(_translate("CalculatorBYyRon", "/"))
        self.push_Divide.setShortcut(_translate("CalculatorBYyRon", "/"))
        self.push_Subtract.setText(_translate("CalculatorBYyRon", "-"))
        self.push_Subtract.setShortcut(_translate("CalculatorBYyRon", "-"))
        self.push_6.setText(_translate("CalculatorBYyRon", "6"))
        self.push_6.setShortcut(_translate("CalculatorBYyRon", "6"))
        self.push_9.setText(_translate("CalculatorBYyRon", "9"))
        self.push_9.setShortcut(_translate("CalculatorBYyRon", "9"))
        self.push_5.setText(_translate("CalculatorBYyRon", "5"))
        self.push_5.setShortcut(_translate("CalculatorBYyRon", "5"))
        self.push_Add.setText(_translate("CalculatorBYyRon", "+"))
        self.push_Add.setShortcut(_translate("CalculatorBYyRon", "+"))
        self.push_7.setText(_translate("CalculatorBYyRon", "7"))
        self.push_7.setShortcut(_translate("CalculatorBYyRon", "7"))
        self.push_Del.setText(_translate("CalculatorBYyRon", "Del"))
        self.push_Del.setShortcut(_translate("CalculatorBYyRon", "Ctrl+S"))
        self.push_Dot.setText(_translate("CalculatorBYyRon", "."))
        self.push_Dot.setShortcut(_translate("CalculatorBYyRon", "."))
        self.push_Clear.setText(_translate("CalculatorBYyRon", "Clear"))
        self.push_0.setText(_translate("CalculatorBYyRon", "0"))
        self.push_0.setShortcut(_translate("CalculatorBYyRon", "0"))
        self.push_2.setText(_translate("CalculatorBYyRon", "2"))
        self.push_2.setShortcut(_translate("CalculatorBYyRon", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculatorBYyRon = QtWidgets.QDialog()
    ui = Ui_CalculatorBYyRon()
    ui.setupUi(CalculatorBYyRon)
    CalculatorBYyRon.show()
    sys.exit(app.exec_())

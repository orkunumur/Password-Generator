# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siferelerim_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sifrelerim_ui(object):
    def setupUi(self, sifrelerim_ui):
        sifrelerim_ui.setObjectName("sifrelerim_ui")
        sifrelerim_ui.resize(605, 580)
        sifrelerim_ui.setMinimumSize(QtCore.QSize(605, 580))
        sifrelerim_ui.setMaximumSize(QtCore.QSize(605, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/kilit/kilit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sifrelerim_ui.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(sifrelerim_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.kayit_defteri = QtWidgets.QTableWidget(self.centralwidget)
        self.kayit_defteri.setGeometry(QtCore.QRect(20, 140, 561, 381))
        self.kayit_defteri.setRowCount(0)
        self.kayit_defteri.setColumnCount(4)
        self.kayit_defteri.setObjectName("kayit_defteri")
        self.siralama = QtWidgets.QComboBox(self.centralwidget)
        self.siralama.setEnabled(True)
        self.siralama.setGeometry(QtCore.QRect(480, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.siralama.setFont(font)
        self.siralama.setEditable(False)
        self.siralama.setObjectName("siralama")
        self.siralama.addItem("")
        self.siralama.addItem("")
        self.siralama.addItem("")
        self.siralama.addItem("")
        self.ara_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.ara_lineedit.setGeometry(QtCore.QRect(20, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ara_lineedit.setFont(font)
        self.ara_lineedit.setStatusTip("")
        self.ara_lineedit.setInputMask("")
        self.ara_lineedit.setText("")
        self.ara_lineedit.setObjectName("ara_lineedit")
        self.ara_push_but = QtWidgets.QPushButton(self.centralwidget)
        self.ara_push_but.setGeometry(QtCore.QRect(180, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ara_push_but.setFont(font)
        self.ara_push_but.setObjectName("ara_push_but")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("image: url(:/kilit/kilit.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tumunu_sec = QtWidgets.QPushButton(self.centralwidget)
        self.tumunu_sec.setGeometry(QtCore.QRect(370, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.tumunu_sec.setFont(font)
        self.tumunu_sec.setObjectName("tumunu_sec")
        sifrelerim_ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sifrelerim_ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 26))
        self.menubar.setObjectName("menubar")
        sifrelerim_ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sifrelerim_ui)
        self.statusbar.setObjectName("statusbar")
        sifrelerim_ui.setStatusBar(self.statusbar)

        self.retranslateUi(sifrelerim_ui)
        self.siralama.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(sifrelerim_ui)

    def retranslateUi(self, sifrelerim_ui):
        _translate = QtCore.QCoreApplication.translate
        sifrelerim_ui.setWindowTitle(_translate("sifrelerim_ui", "MainWindow"))
        self.siralama.setItemText(0, _translate("sifrelerim_ui", "Sırala"))
        self.siralama.setItemText(1, _translate("sifrelerim_ui", "A\'dan Z\'ye Sırala"))
        self.siralama.setItemText(2, _translate("sifrelerim_ui", "Z\'den A\'ya Sırala"))
        self.siralama.setItemText(3, _translate("sifrelerim_ui", "Tarihe Göre Sırala"))
        self.ara_lineedit.setPlaceholderText(_translate("sifrelerim_ui", "ARA"))
        self.ara_push_but.setText(_translate("sifrelerim_ui", "ARA"))
        self.label_3.setText(_translate("sifrelerim_ui", "PAROLA KAYIT DEFTERİ"))
        self.pushButton.setText(_translate("sifrelerim_ui", "SİL"))
        self.tumunu_sec.setText(_translate("sifrelerim_ui", "TÜMÜNÜ SEÇ"))
import arkaplan_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tri.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 931, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 50, 171, 16))
        self.label.setObjectName("label")
        self.textZone = QtWidgets.QLineEdit(self.groupBox)
        self.textZone.setGeometry(QtCore.QRect(130, 80, 771, 51))
        self.textZone.setObjectName("textZone")
        self.sortCombo = QtWidgets.QComboBox(self.groupBox)
        self.sortCombo.setGeometry(QtCore.QRect(10, 80, 111, 51))
        self.sortCombo.setStyleSheet("")
        self.sortCombo.setObjectName("sortCombo")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.etatZone = QtWidgets.QTextBrowser(self.groupBox)
        self.etatZone.setGeometry(QtCore.QRect(355, 10, 541, 41))
        self.etatZone.setObjectName("etatZone")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 931, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.resZone = QtWidgets.QTextBrowser(self.groupBox_2)
        self.resZone.setGeometry(QtCore.QRect(20, 70, 881, 131))
        self.resZone.setObjectName("resZone")
        self.croissantBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.croissantBtn.setGeometry(QtCore.QRect(110, 30, 95, 20))
        self.croissantBtn.setChecked(True)
        self.croissantBtn.setObjectName("croissantBtn")
        self.decroissantBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.decroissantBtn.setGeometry(QtCore.QRect(250, 30, 95, 20))
        self.decroissantBtn.setObjectName("decroissantBtn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 931, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.algZone = QtWidgets.QTextBrowser(self.groupBox_3)
        self.algZone.setGeometry(QtCore.QRect(130, 40, 771, 131))
        self.algZone.setObjectName("algZone")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.animerBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.animerBtn.setGeometry(QtCore.QRect(20, 70, 93, 71))
        self.animerBtn.setObjectName("animerBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tri"))
        self.groupBox.setTitle(_translate("MainWindow", "Parametres de tri"))
        self.label.setText(_translate("MainWindow", "Liste d\'entiers"))
        self.sortCombo.setItemText(0, _translate("MainWindow", "Tri rapide"))
        self.sortCombo.setItemText(1, _translate("MainWindow", "Tri par selection"))
        self.sortCombo.setItemText(2, _translate("MainWindow", "Tri par insertion"))
        self.sortCombo.setItemText(3, _translate("MainWindow", "Tri par fusion"))
        self.sortCombo.setItemText(4, _translate("MainWindow", "Tri à bulles"))
        self.label_3.setText(_translate("MainWindow", "Etat :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Resultats"))
        self.croissantBtn.setText(_translate("MainWindow", "Croissante"))
        self.decroissantBtn.setText(_translate("MainWindow", "Décroissante"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Principe"))
        self.label_2.setText(_translate("MainWindow", "Algorithme"))
        self.animerBtn.setText(_translate("MainWindow", "Animer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 26))
        self.menubar.setObjectName("menubar")
        self.menuMen_ler = QtWidgets.QMenu(self.menubar)
        self.menuMen_ler.setObjectName("menuMen_ler")
        self.menu_lemler = QtWidgets.QMenu(self.menuMen_ler)
        self.menu_lemler.setObjectName("menu_lemler")
        self.menu_ifre = QtWidgets.QMenu(self.menu_lemler)
        self.menu_ifre.setObjectName("menu_ifre")
        self.menuKar_la_t_r = QtWidgets.QMenu(self.menuMen_ler)
        self.menuKar_la_t_r.setObjectName("menuKar_la_t_r")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cikis = QtWidgets.QAction(MainWindow)
        self.cikis.setObjectName("cikis")
        self.degistir = QtWidgets.QAction(MainWindow)
        self.degistir.setObjectName("degistir")
        self.dice = QtWidgets.QAction(MainWindow)
        self.dice.setObjectName("dice")
        self.levenshtein = QtWidgets.QAction(MainWindow)
        self.levenshtein.setObjectName("levenshtein")
        self.menu_ifre.addAction(self.degistir)
        self.menu_lemler.addAction(self.menu_ifre.menuAction())
        self.menuKar_la_t_r.addAction(self.dice)
        self.menuKar_la_t_r.addSeparator()
        self.menuKar_la_t_r.addAction(self.levenshtein)
        self.menuMen_ler.addAction(self.menu_lemler.menuAction())
        self.menuMen_ler.addSeparator()
        self.menuMen_ler.addAction(self.menuKar_la_t_r.menuAction())
        self.menuMen_ler.addSeparator()
        self.menuMen_ler.addAction(self.cikis)
        self.menubar.addAction(self.menuMen_ler.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMen_ler.setTitle(_translate("MainWindow", "Menü"))
        self.menu_lemler.setTitle(_translate("MainWindow", "İşlemler"))
        self.menu_ifre.setTitle(_translate("MainWindow", "Şifre"))
        self.menuKar_la_t_r.setTitle(_translate("MainWindow", "Karşılaştır"))
        self.cikis.setText(_translate("MainWindow", "Çıkış"))
        self.degistir.setText(_translate("MainWindow", "Değiştir"))
        self.dice.setText(_translate("MainWindow", "Dice Katsayısı Kullanarak Karşılaştır"))
        self.levenshtein.setText(_translate("MainWindow", "Levenshtein Distance Kullanarak Karşılaştır"))

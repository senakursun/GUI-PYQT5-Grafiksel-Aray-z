from PyQt5.QtWidgets import QApplication,QMessageBox, QMainWindow, QAction, QMenu, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from panel2 import Ui_MainWindow
from update import UpdatePasswordDialog
from dice_benzerlik import DiceKarsilastirPage
from levenshtein import LevenshteinKarsilastirPage


class AnaPencerePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ana Ekran")
        self.updateform =UpdatePasswordDialog()
        self.diceform =DiceKarsilastirPage()
        self.levenshteinform = LevenshteinKarsilastirPage()
        self.ui.degistir.triggered.connect(self. UpdateFormu)
        self.ui.dice.triggered.connect(self.DiceFormu)
        self.ui.levenshtein.triggered.connect(self.LevenshteinFormu)
        self.ui.cikis.triggered.connect(self.exit_application)

    def exit_application(self):
        # Uygulamadan çıkış işlemi
        reply = QMessageBox.question(self, 'Çıkış İşlemi', 'Uygulamadan çıkmak istediğinizden emin misiniz?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.quit()

    
    
    def UpdateFormu(self):
        self.updateform.show()

    
    def DiceFormu(self):
        self.diceform.show()
        
    def LevenshteinFormu(self):
        self.levenshteinform.show()
        


        # Menü oluşturma
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # İşlemler menüsü
        islemler_menu = menubar.addMenu("İşlemler")

        # Şifre alt menüsü
        sifre_menu = QMenu("Şifre", self)
        islemler_menu.addMenu(sifre_menu)

        # Değiştir alt menüsü ekleme
        degistir_action = QAction("Değiştir", self)
        degistir_action.triggered.connect(self.show_update_password_dialog)
        sifre_menu.addAction(degistir_action)

    def show_update_password_dialog(self):
        # Güncelleme ekranını oluştur
        update_dialog = UpdatePasswordDialog(self)
        update_dialog.exec_()

  

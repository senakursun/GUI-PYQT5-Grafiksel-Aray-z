from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import sqlite3
from panel3 import Ui_UpdatePasswordDialog


class UpdatePasswordDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Arayüz öğelerini yükleme
        self.updateform = Ui_UpdatePasswordDialog()
        self.updateform.setupUi(self)
        self.setWindowTitle("Şifre Değiştir")

        # Güncelleme butonuna tıklama işlemini bağlama
        self.updateform.pushButton.clicked.connect(self.update_password)

    def update_password(self):
        username = self.updateform.lineEdit.text()
        new_password = self.updateform.lineEdit_2.text()

        # SQLite veritabanına bağlan
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Kullanıcının şifresini güncelle
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        QMessageBox.information(self, "Başarılı", "Şifre başarıyla güncellendi.")
        connection.commit()
        connection.close()

        self.close()

        
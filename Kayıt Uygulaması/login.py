from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from panel import Ui_MainWindow
import sqlite3
from anapencere import AnaPencerePage


class LoginPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.anapencereac=AnaPencerePage()
        self.setWindowTitle("Kullanıcı Girişi ve Kaydı")

        # SQLite veritabanını oluştur
        self.create_database()

        # Butonlara tıklama işlemleri
        self.ui.registerr.clicked.connect(self.register)
        self.ui.login.clicked.connect(self.login)

    def create_database(self):
        # SQLite veritabanına bağlan
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Kullanıcılar tablosunu oluştur
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                        )""")
        connection.commit()
        connection.close()

    def register(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        # SQLite veritabanına bağlan
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Kullanıcı adının zaten var olup olmadığını kontrol et
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten mevcut.")
        else:
            # Kullanıcıyı kaydet
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            QMessageBox.information(self, "Başarılı", "Kullanıcı başarıyla kaydedildi.")

            

        connection.close()

    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        # SQLite veritabanına bağlan
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Kullanıcı adı ve şifreyi kontrol et
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            QMessageBox.information(self, "Başarılı", "Giriş başarılı!")
            self.hide()
            self.anapencereac.show()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")

        connection.close()

    


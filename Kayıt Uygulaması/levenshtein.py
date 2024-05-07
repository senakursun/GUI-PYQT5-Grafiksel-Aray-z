import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from panel5 import Ui_MainWindow

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances
    return distances[-1]

def similarity_ratio(s1, s2):
    distance = levenshtein_distance(s1, s2)
    max_length = max(len(s1), len(s2))
    return (max_length - distance) / max_length * 100

class LevenshteinKarsilastirPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.levenshteinform = Ui_MainWindow()
        self.levenshteinform.setupUi(self)
        self.setWindowTitle("Levenshtein Algoritması Kullanarak Metin Karşılaştırma Aracı")

        # Butonlara tıklama işlemleri
        self.levenshteinform.pushButton_2.clicked.connect(self.select_file1)
        self.levenshteinform.pushButton_3.clicked.connect(self.select_file2)
        self.levenshteinform.pushButton.clicked.connect(self.compare_texts)

        # Dosya yollarını saklamak için değişkenler
        self.file1_path = ""
        self.file2_path = ""

    def select_file1(self):
        # İlk dosyayı seçmek için dosya seçme penceresi aç
        file_path, _ = QFileDialog.getOpenFileName(self, "Birinci Dosyayı Seç", "", "Text Files (*.txt)")
        if file_path:
            self.levenshteinform.lineEdit.setText(file_path)
            self.file1_path = file_path

    def select_file2(self):
        # İkinci dosyayı seçmek için dosya seçme penceresi aç
        file_path, _ = QFileDialog.getOpenFileName(self, "İkinci Dosyayı Seç", "", "Text Files (*.txt)")
        if file_path:
            self.levenshteinform.lineEdit_2.setText(file_path)
            self.file2_path = file_path

    def compare_texts(self):
        # Dosya yolları belirtilmemişse uyarı ver
        if not self.file1_path or not self.file2_path:
            QMessageBox.warning(self, "Uyarı", "Lütfen iki dosyayı da seçiniz.")
            return

        # Dosyaları açıp içeriklerini oku
        try:
            with open(self.file1_path, "r", encoding="utf-8") as file1:
                text1 = file1.read()
            with open(self.file2_path, "r", encoding="utf-8") as file2:
                text2 = file2.read()

            # Metinleri karşılaştır ve sonucu göster
            similarity = similarity_ratio(text1, text2)
            self.levenshteinform.lineEdit_3.setText(f"Levenshtein Benzerlik Yüzdesi: %{similarity:.2f}")

        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))


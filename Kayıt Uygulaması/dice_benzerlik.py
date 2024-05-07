from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from panel4 import Ui_MainWindow

def dice_similarity(text1, text2):
    def create_bi_grams(text):
        bi_grams = set()
        for i in range(len(text) - 1):
            bi_grams.add(text[i:i+2])
        return bi_grams
    
    bi_grams1 = create_bi_grams(text1)
    bi_grams2 = create_bi_grams(text2)
    
    intersection = len(bi_grams1.intersection(bi_grams2))
    total_bi_gram_count = len(bi_grams1) + len(bi_grams2)
    
    similarity = (2 * intersection) / total_bi_gram_count
    
    return similarity

class DiceKarsilastirPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.diceform = Ui_MainWindow()
        self.diceform.setupUi(self)
        self.setWindowTitle("Dice Katsayısı Kullanarak Metin Karşılaştırma Aracı")

        # Butonlara tıklama işlemleri
        self.diceform.pushButton_2.clicked.connect(self.select_file1)
        self.diceform.pushButton_3.clicked.connect(self.select_file2)
        self.diceform.pushButton.clicked.connect(self.compare_texts)

        # Dosya yollarını saklamak için değişkenler
        self.file1_path = ""
        self.file2_path = ""

    def select_file1(self):
        # İlk dosyayı seçmek için dosya seçme penceresi aç
        file_path, _ = QFileDialog.getOpenFileName(self, "Birinci Dosyayı Seç", "", "Text Files (*.txt)")
        if file_path:
            self.diceform.lineEdit.setText(file_path)
            self.file1_path = file_path

    def select_file2(self):
        # İkinci dosyayı seçmek için dosya seçme penceresi aç
        file_path, _ = QFileDialog.getOpenFileName(self, "İkinci Dosyayı Seç", "", "Text Files (*.txt)")
        if file_path:
            self.diceform.lineEdit_2.setText(file_path)
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
            similarity = dice_similarity(text1, text2)
            self.diceform.lineEdit_3.setText(f"Dice Katsayısı: {similarity:.2f}")

        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))


from PyQt5.QtWidgets import QApplication
from login import LoginPage


app = QApplication([])
window = LoginPage()
window.show()
app.exec_()

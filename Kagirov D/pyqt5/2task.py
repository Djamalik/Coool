from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Секретик')
main_win.resize(800,400)
text = QLabel('Ты просто нулёвый!')
button = QPushButton('Кнопка с секретом')
def texting():
    line.addWidget(text, alignment = Qt.AlignCenter)

line = QVBoxLayout()
line.addWidget(button, alignment = Qt.AlignCenter)
button.clicked.connect(texting)
main_win.setLayout(line)
main_win.show()
app.exec_()
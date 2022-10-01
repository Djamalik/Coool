from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Языки програмирования')
main_win.resize(800,400)
text1 = QLabel('PHP')
text2 = QLabel('JavaScript')
text3 = QLabel('Python')
text4 = QLabel('PAscal')
text5 = QLabel('SQL')
text6 = QLabel('C++')

lineV = QVBoxLayout()
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()

lineH1.addWidget(text1, alignment = Qt.AlignCenter)
lineH1.addWidget(text2, alignment = Qt.AlignCenter)
lineH2.addWidget(text3, alignment = Qt.AlignCenter)
lineH2.addWidget(text4, alignment = Qt.AlignCenter)
lineH3.addWidget(text5, alignment = Qt.AlignCenter)
lineH3.addWidget(text6, alignment = Qt.AlignCenter)

lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
lineV.addLayout(lineH3)
main_win.setLayout(lineV)

main_win.show()
app.exec_()
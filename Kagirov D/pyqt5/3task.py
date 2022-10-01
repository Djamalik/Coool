from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Испытай удачу!')
main_win.resize(800,400)
main_win1 = QWidget()
main_win1.setWindowTitle('Пфф, мимо')
main_win1.resize(800,400)
main_win2 = QWidget()
main_win2.setWindowTitle('Конец')
main_win2.resize(800,400)

def reset():
    text1 = text.text()
    text2 = str(int(text1)+1)
    text.setText(text2)

    lists = list()
    lists.append(button1)
    lists.append(button2)
    lists.append(button3)
    lists.append(button4)
    lists.append(button5)
    for i in range(4):
        a = randint(0,len(lists)-1)
        lists[a].clicked.connect(lose)
        lists.remove(lists[a])
    for i in lists:
        i.clicked.connect(win)
    
def restart():
    main_win1.hide()
    main_win.show()
    button1.clicked.disconnect()
    button2.clicked.disconnect()
    button3.clicked.disconnect()
    button4.clicked.disconnect()
    button5.clicked.disconnect() 
    reset()
    

def lose():
    if text.text()!='4':
        main_win.hide()
        main_win1.show()
        but1.clicked.connect(restart)
    else:
        win()

def win():
    if text.text()=='4':
        text.setText('Поражение')
    else:
        text.setText('Победа')
    main_win.hide()
    main_win1.hide()
    main_win2.show()

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

lineV = QVBoxLayout()
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()

lineH1.addWidget(button1, alignment = Qt.AlignLeft)
lineH1.addWidget(button2, alignment = Qt.AlignRight)
lineH2.addWidget(button3, alignment = Qt.AlignCenter)
lineH3.addWidget(button4, alignment = Qt.AlignLeft)
lineH3.addWidget(button5, alignment = Qt.AlignRight)
lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
lineV.addLayout(lineH3)
main_win.setLayout(lineV)
main_win.show()

but1 = QPushButton('Ты просто нулёвый, чел!!!')
line1 = QVBoxLayout()
line1.addWidget(but1, alignment = Qt.AlignCenter)
main_win1.setLayout(line1)

text = QLabel('0')
line2 = QVBoxLayout()
line2.addWidget(text, alignment = Qt.AlignCenter)
main_win2.setLayout(line2)

reset()

app.exec_()
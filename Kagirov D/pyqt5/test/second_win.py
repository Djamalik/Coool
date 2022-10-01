from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from final_win import *

class Experiment():
    def __init__(self,age,test1,test2,test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self,mw):
        ''' окно, в котором проводится опрос '''
        super().__init__()
    
        # создаём и настраиваем графические элементы:
        self.initUI()
    
        #устанавливает связи между элементами
        self.connects()
    
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()

        self.mw = mw

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.btn1=QPushButton(txt_starttest1)
        self.btn2=QPushButton(txt_starttest2)
        self.btn3=QPushButton(txt_starttest3)
        self.btn4=QPushButton(txt_sendresults)
        self.t1 = QLabel(txt_hintname)
        self.t2 = QLabel(txt_age)
        self.t3 = QLabel(txt_test1)
        self.t4 = QLabel(txt_test2)
        self.t5 = QLabel(txt_test3)
        self.line1 = QLineEdit(txt_hintname)
        self.line2 = QLineEdit(txt_hintage)
        self.line3 = QLineEdit(txt_hinttest1)
        self.line4 = QLineEdit(txt_hinttest2)
        self.line5 = QLineEdit(txt_hinttest3)
        self.back=QPushButton("Назад")
        self.text_timer = QLabel(time)

        self.t1.setStyleSheet("color: rgb(160,50,75)")
        self.t1.setFont(QFont("Times", 30, QFont.Bold))
        self.t2.setStyleSheet("color: rgb(10,150,205)")
        self.t3.setFont(QFont("Times", 10, QFont.Bold))

        self.btn1.setStyleSheet("color: rgb(160,50,75)")
        self.btn1.setFont(QFont("Times", 30, QFont.Bold))
        self.btn2.setStyleSheet("color: rgb(10,150,205)")
        self.btn3.setFont(QFont("Times", 10, QFont.Bold))
        self.btn4.setStyleSheet('background: rgb(255,0,0);')

        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.back, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.t1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.t2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.t3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn4, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.t4, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.t5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn1, alignment = Qt.AlignLeft)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.exp = Experiment(int(self.line2.text()),self.line3.text(),self.line4.text(),self.line5.text(),)
        self.fw=FinalWin(self.exp,self.mw)
        self.hide()

    def back_click(self):
        self.mw.show()
        self.hide()

    def connects(self):
        self.btn4.clicked.connect(self.next_click)
        self.btn1.clicked.connect(self.timer_start)
        self.btn2.clicked.connect(self.timer_second)
        self.btn3.clicked.connect(self.timer_finish)
        self.back.clicked.connect(self.back_click)

    def set_appear(self):
        self.setWindowTitle(txt_title )
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def timer_start(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(500)

    def timer_second(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(3000)
    
    def timer_finish(self):
        global time
        time = QTime(0, 10, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(100)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("mm:ss"))
        self.text_timer.setStyleSheet("color: rgb(160,50,75)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("mm:ss") == "59:59":
            self.timer.stop()
            self.text_timer.setText("")

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(79,92,192)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "23:59:59":
            self.timer.stop()
            self.text_timer.setText("")

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(231,123,31)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(104,180,234)")
        else:
            self.text_timer.setStyleSheet("color: rgb(94,180,123)")
        if time.toString("hh:mm:ss") == "23:59:59":
            self.timer.stop()
            self.text_timer.setText("")


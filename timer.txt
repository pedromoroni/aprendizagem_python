import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont


class Timer(QWidget):

    is_running = False

    def __init__(self):
        super().__init__()
        self.time_label = QLabel('00:00:00.00', self)
        self.timer = QTimer(self)
        self.elapsed_time = QTime(0, 0, 0, 0)
        self.button_start = QPushButton('Start', self)
        self.button_stop = QPushButton('Stop', self)
        self.button_reset = QPushButton('Reset', self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Timer')
        self.setGeometry(600, 350, 500, 200)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.button_start.setGeometry(0, 0, 275, 40)
        self.button_start.setStyleSheet('background-color: green')
        self.button_start.setFont(QFont('Arial', 12, QFont.Bold))


        self.button_stop.setGeometry(275, 0, 275, 40)
        self.button_stop.setStyleSheet('background-color: red')
        self.button_stop.setFont(QFont('Arial', 12, QFont.Bold))

        self.button_reset.setGeometry(550, 0, 275, 40)
        self.button_reset.setStyleSheet('background-color: gray')
        self.button_reset.setFont(QFont('Arial', 12, QFont.Bold))

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setStyleSheet('font-size: 149px;'
                                      'color: black;')
        self.setStyleSheet('background-color: #78a6f0')

        self.button_start.clicked.connect(self.timer_start)
        self.button_stop.clicked.connect(self.timer_stop)
        self.button_reset.clicked.connect(self.timer_reset)

        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(10)

        self.updateTimer()


    def updateTimer(self):
        if self.is_running:
            self.elapsed_time = self.elapsed_time.addMSecs(10)
            hours = self.elapsed_time.toString('hh')
            minutes = self.elapsed_time.toString('mm')
            seconds = self.elapsed_time.toString('ss')
            milliseconds = str(int(self.elapsed_time.toString('zzz')) // 10).zfill(2)

            time_str = f"{hours}:{minutes}:{seconds}.{milliseconds}"
            self.time_label.setText(time_str)

    def timer_start(self):
        self.is_running = True


    def timer_stop(self):
        self.is_running = False


    def timer_reset(self):
        self.elapsed_time = QTime(0, 0, 0, 0)
        hours = self.elapsed_time.toString('hh')
        minutes = self.elapsed_time.toString('mm')
        seconds = self.elapsed_time.toString('ss')
        milliseconds = str(int(self.elapsed_time.toString('zzz')) // 10).zfill(2)

        time_str = f"{hours}:{minutes}:{seconds}.{milliseconds}"
        self.time_label.setText(time_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())
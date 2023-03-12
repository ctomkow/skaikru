#!/usr/bin/env python3

import requests
import jsonparse
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle('Weather App')
        self.setMinimumSize(QSize(400, 400))  # Set sizes
        button = QPushButton('Get the weather', self)
        button.setGeometry(50, 50, 50, 50)
        button.resize(150, 50)

        label = QLabel("Old Text", self)

        w = Weather('Langley', label)
        button.clicked.connect(lambda: w.avg_temp())


class Weather:

    def __init__(self, city: str, label: QLabel):

        self.city = city
        self.label = label

    def avg_temp(self):

        jp = jsonparse.Parser()
        data = requests.get(f'https://wttr.in/{self.city}?format=j1').json()
        current_condition = jp.find_key(data, 'current_condition')
        self.label.setText(str(jp.find_key(current_condition, 'temp_C')))


app = QApplication([])
window = MainWindow()
window.show()
# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
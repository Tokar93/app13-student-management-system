from PyQt6.QtCore import QLine
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QComboBox)
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Average Speed Calculator')

        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel('Distance')
        self.distance_line_edit = QLineEdit()

        time_label = QLabel('Time (hours)')
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        self.drop_list = QComboBox()
        self.drop_list.addItems(['Kilometers (km)', 'Imperial (miles)'])

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.drop_list, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)

        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance/time

        if self.drop_list.currentText() == 'Kilometers (km)':
            speed = round(speed, 2)
            unit = 'km/h'

        elif self.drop_list.currentText() == 'Imperial (miles)':
            speed = round(speed, 2)
            unit = 'mph'

        self.output_label.setText(f'Average speed: {speed} {unit}')

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
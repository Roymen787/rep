import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Circle_Drawer(QWidget):
    def __init__(self):
        super(CircleDrawer, self).__init__()
        self.circles = []

    def update_canvas(self, diameter):
        new_circle = Circle(diameter)
        self.circles.append(new_circle)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x = random.randint(0, self.width() - circle.diameter)
            y = random.randint(0, self.height() - circle.diameter)
            painter.setBrush(circle.color)
            painter.drawEllipse(x, y, circle.diameter, circle.diameter)


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()

        self.setWindowTitle("Random Circles Application")
        self.setGeometry(100, 100, 800, 600)

        self.circle_drawer = CircleDrawer()
        self.setCentralWidget(self.circle_drawer)

        self.layout = QVBoxLayout()
        self.circle_drawer.setLayout(self.layout)

        self.button = QPushButton("Добавить окружность")
        self.button.clicked.connect(self.add_circle)
        self.layout.addWidget(self.button)

    def add_circle(self):
        diameter = random.randint(20, 100)
        self.circle_drawer.update_canvas(diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

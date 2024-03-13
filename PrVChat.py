import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class PrVChat_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PrVChat")
        self.setMinimumSize(640, 360)
        self.resize(800, 450)
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    PrVChat_QApplication = QApplication()
    PrVChat_GUI = PrVChat_MainWindow()
    PrVChat_GUI.show()
    sys.exit(PrVChat_QApplication.exec())

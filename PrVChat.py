import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QStatusBar
from PySide6.QtGui import QClipboard
from twisted.internet import reactor, protocol


class PrVChat_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        self.GRID = QGridLayout(widget)

        self.HostHBox = QHBoxLayout()
        self.HostHBox_Host_Port_Label = QLabel("Port:")
        self.HostHBox_Host_Port_Input = QLineEdit()
        self.HostHBox_Host_Port_Input.setPlaceholderText("8000")
        self.HostHBox_Host_Btn = QPushButton("Host")
        self.HostHBox_Host_Info_Copy_Btn = QPushButton("Copy Host Info")
        self.HostHBox_Host_Info_Copy_Btn.clicked.connect(self.HostHBox_Host_Info_Copy_Btn_Clicked)

        self.ClientHBox = QHBoxLayout()
        self.ClientHBox_Client_Label = QLabel("Host IP:")
        self.ClientHBox_Host_IP_Input = QLineEdit()
        self.ClientHBox_Host_IP_Input.setPlaceholderText("0.0.0.0")
        self.ClientHBox_Host_IP_Port_Label = QLabel("Port:")
        self.ClientHBox_Host_Port_Input = QLineEdit()
        self.ClientHBox_Host_Port_Input.setPlaceholderText("8000")
        self.ClientHBox_Connect_Btn = QPushButton("Connect")

        self.Settings_Btn = QPushButton("Settings")

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.setWindowTitle("PrVChat")
        self.setFixedSize(500, 150)
        self.initUI()

    def initUI(self):
        self.HostHBox.addWidget(self.HostHBox_Host_Port_Label)
        self.HostHBox.addWidget(self.HostHBox_Host_Port_Input)
        self.HostHBox.addWidget(self.HostHBox_Host_Btn)
        self.HostHBox.addWidget(self.HostHBox_Host_Info_Copy_Btn)

        self.ClientHBox.addWidget(self.ClientHBox_Client_Label)
        self.ClientHBox.addWidget(self.ClientHBox_Host_IP_Input)
        self.ClientHBox.addWidget(self.ClientHBox_Host_IP_Port_Label)
        self.ClientHBox.addWidget(self.ClientHBox_Host_Port_Input)
        self.ClientHBox.addWidget(self.ClientHBox_Connect_Btn)

        self.GRID.addLayout(self.HostHBox, 0, 0, 1, 1)
        self.GRID.addLayout(self.ClientHBox, 1, 0, 1, 1)
        self.GRID.addWidget(self.Settings_Btn, 2, 0, 1, 1)

        self.statusBar.showMessage("Ready")

    def HostHBox_Host_Info_Copy_Btn_Clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(f"Host IP: a, Port: 8000")
        self.statusBar.showMessage("Host Info Copied")


if __name__ == "__main__":
    PrVChat_QApplication = QApplication()
    PrVChat_GUI = PrVChat_MainWindow()
    PrVChat_GUI.show()
    sys.exit(PrVChat_QApplication.exec())

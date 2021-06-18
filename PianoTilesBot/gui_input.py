from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

from PianoTilesBot.clicker import Clicker


class inputWindow(QWidget):
    def __init__(self):
        super(inputWindow, self).__init__()
        self.setLayout(QHBoxLayout())
        self.initVars()
        self.applySettings()
        self.construct()

    def initVars(self):
        self.clickCount = 0

    def applySettings(self):
        self.setWindowOpacity(0.2)
        self.layout().setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def construct(self):
        self.label = QLabel("Click number 1")
        self.label.setStyleSheet("QLabel { color : blue; }")
        self.label.setFont(QFont("Arial", 20))
        self.layout().addWidget(self.label)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if len(Clicker.clickPoints) == 4:
            Clicker.clickPoints = []
        Clicker.clickPoints.append(event.windowPos())
        self.label.setText(f"Click number {self.clickCount+2}")
        self.clickCount += 1
        if self.clickCount >= 4:
            # print(f"{Clicker.clickPoints = }")
            print("Received input areas.")
            self.close()


import os

from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from pynput import mouse
from PIL import ImageGrab

from PianoTilesBot.clicker import Clicker
from PianoTilesBot.gui_input import inputWindow


class PianoTilesGui(QWidget):
    def __init__(self):
        super(PianoTilesGui, self).__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.applySettings()
        self.construct()
        self.show()

    def applySettings(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Piano Tiles Bot")
        self.setMinimumWidth(400)
        # Vars
        self.thread = None

    def construct(self):
        self.llayout = QVBoxLayout()
        self.rlayout = QVBoxLayout()
        self.layout.addLayout(self.llayout)
        self.layout.addLayout(self.rlayout)
        selectInputBtn = QPushButton("Select Input Areas")
        selectInputBtn.clicked.connect(self._getInputAreas)
        self.rlayout.addWidget(selectInputBtn)
        startAppBtn = QPushButton("Start Piano Tiles")
        startAppBtn.clicked.connect(self._startApp)
        self.llayout.addWidget(startAppBtn)
        startSongBtn = QPushButton("Start Song")
        startSongBtn.clicked.connect(self._startSong)
        self.llayout.addWidget(startSongBtn)
        btn = QPushButton("Stop Song (WIP)")
        # TODO :: refactor name
        btn.clicked.connect(self._stopSong)
        self.llayout.addWidget(btn)

    @staticmethod
    def _startApp():
        print(f"Starting app...")
        os.startfile("C:\\Users\\tongq\\Desktop\\PianoTiles.lnk")
        print(f"Started app")

    def _getInputAreas(self):
        print(f"Getting input areas...")
        Clicker.clickPoints = []
        self.input_widget = inputWindow()
        self.input_widget.showFullScreen()

    def _startSong(self):
        def on_finish():
            print(f"{firstClickThread.__name__} finished!")
            self.thread2 = clickerThread()
            self.thread2.finished.connect(lambda: print(f"{clickerThread.__name__} finished!"))
            self.thread2.start()

        self.thread = firstClickThread()
        self.thread.finished.connect(on_finish)
        self.thread.start()

    def _stopSong(self):
        if self.thread is not None and self.thread2.isRunning():
            self.thread2.quit()
            print(f"Ended {clickerThread.__name__}.")
        else:
            print(f"Thread not running.")

class firstClickThread(QThread):
    def run(self):
        print(f"Starting {self.__class__.__name__}...")
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    @staticmethod
    def on_click(x, y, button, pressed):
        return False

class clickerThread(QThread):
    lastClicked = None

    def run(self) -> None:
        print(f"Starting {self.__class__.__name__}...")
        while True:
            loc = self.chooseClick()
            if loc != self.lastClicked:
                self.lastClicked = loc
                Clicker.click(loc)

    @staticmethod
    def chooseClick() -> int:
        """If blue not greater than 250, return i"""
        # TODO :: fix drag problem, resolved through color comparison???
        image = ImageGrab.grab()
        for i, coord in enumerate(Clicker.coords()):
            # Compares it with dark background
            if image.getpixel(coord)[2] < 250:
                return i
        return -1

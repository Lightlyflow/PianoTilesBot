import ctypes
import pynput

from PyQt5.QtCore import QPointF


class Clicker:
    PROCESS_PER_MONITOR_DPI_AWARE = 2
    ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
    clickPoints: QPointF = []
    mouse = pynput.mouse.Controller()
    button = pynput.mouse.Button
    counter = 0

    @staticmethod
    def click(location: int):
        assert len(Clicker.clickPoints) == 4, print(f"clickPoints not length 4: {Clicker.clickPoints}")
        if location == -1:
            return
        Clicker.counter += 1
        print(f"[{Clicker.counter}] Clicking location {location}...")
        point = (Clicker.clickPoints[location].x(), Clicker.clickPoints[location].y())
        Clicker.mouse.position = point
        Clicker.mouse.click(Clicker.button.left)

    @staticmethod
    def coords():
        assert len(Clicker.clickPoints) == 4, print("clickPoints not length 4")
        for point in Clicker.clickPoints:
            yield point.x(), point.y()

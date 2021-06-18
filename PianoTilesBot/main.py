import sys

from PyQt5.QtWidgets import QApplication

from PianoTilesBot.gui import PianoTilesGui

app = QApplication(sys.argv)
widget = PianoTilesGui()
sys.exit(app.exec_())

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi("UI/settings_window.ui", self)

        self.start_monitoring_button.clicked.connect(self.go_to_detection)

    def displayInfo(self):
        self.show()

    def go_to_detection(self):
        print("Go to Detection")

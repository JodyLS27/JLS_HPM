import sys

from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow


def run():
    load_ui()


def load_ui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

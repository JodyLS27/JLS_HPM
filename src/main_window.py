from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JLS: Houdini package manager")

        self.setMinimumWidth(350)
        self.setMinimumHeight(400)
        
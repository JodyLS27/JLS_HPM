from PySide6.QtWidgets import QMainWindow


class UiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JLS: Houdini package manager")
        
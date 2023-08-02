from GUI import menu_bar
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window
        self.setWindowTitle("JLS: Package manager")

        self.setMinimumWidth(350)
        self.setMinimumHeight(400)

        # Load in widgets
        menu_bar_main = menu_bar.MenuBar()

        self.setMenuBar(menu_bar_main)

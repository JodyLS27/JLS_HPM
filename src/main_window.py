from PySide6.QtWidgets import QMainWindow

from GUI import menu_bar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JLS: Houdini package manager")

        self.setMinimumWidth(350)
        self.setMinimumHeight(400)
        
        
        self.menuBar = menu_bar.MenuBar()
        self.setMenuBar(self.menuBar)

        
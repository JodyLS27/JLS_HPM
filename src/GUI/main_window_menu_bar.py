from PySide6.QtWidgets import QMenuBar


class MainMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()        
        self.addMenu("file")

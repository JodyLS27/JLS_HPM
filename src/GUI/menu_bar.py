from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()        
        self.addMenu("file")

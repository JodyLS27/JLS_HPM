from GUI import file_dialog
from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        # Menu items
        self.menu_file = None

        # Methods
        self.add_menu_items()
        self.add_menu_actions()
        # TODO: Add seperate menu_actions per menu bard button

    def add_menu_items(self):
        self.menu_file = self.addMenu("File")

    def add_menu_actions(self):
        self.set_package_path = self.menu_file.addAction("Set Package Path")
        self.set_package_path.triggered.connect(self.set_package_path_clicked)

    @staticmethod
    def set_package_path_clicked():
        print("triggered")
        file_dialog.FileDialogPopup()

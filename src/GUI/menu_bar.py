from PySide6.QtWidgets import QMenuBar

from GUI import file_dialog


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.add_menu_items()
        self.add_menu_actions()

    def add_menu_items(self):
        self.menu_file = self.addMenu("File")

    def add_menu_actions(self):
        self.set_package_path = self.menu_file.addAction("Set Package Path")
        self.set_package_path.triggered.connect(self.set_package_path_clicked)

    def set_package_path_clicked(self):
        print("triggered")
        file_dialog.FileDialogPopup()

from PySide6.QtWidgets import QFileDialog


class FileDialogPopup(QFileDialog):
    def __init__(self):
        super().__init__()
        
        dialog = QFileDialog(self)
        folder_name = dialog.getExistingDirectory(self, "Please select a desired location", "/Home")
        
        print(folder_name)
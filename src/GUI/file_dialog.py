from pathlib import Path

from JLS import io
from PySide6.QtWidgets import QFileDialog

rw = io.IO()


class FileDialogPopup(QFileDialog):

    def __init__(self):
        super().__init__()

        dialog = QFileDialog(self)
        file_path = Path(dialog.getExistingDirectory(self, "Please select a desired location", str(Path.home())))

        text = "This is a test. \nWondering what will be stored and what will break."
        rw.write_text(file_path, text, "test")

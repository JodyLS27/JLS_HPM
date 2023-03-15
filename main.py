def main():
    import sys

    from PySide6.QtWidgets import QApplication

    from ui_window import UiWindow

    app = QApplication(sys.argv)
    window = UiWindow()
    window.show()

    app.exec()



if __name__ == "__main__":
    main()
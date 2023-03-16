#!/usr/bin/env python

def main():
    import sys

    from PySide6.QtWidgets import QApplication

    from main_window import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()



if __name__ == "__main__":
    main()
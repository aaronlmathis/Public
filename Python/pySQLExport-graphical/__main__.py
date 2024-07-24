from gui import LoginWindow, MainWindow
from PyQt6.QtWidgets import QApplication
import sys



def main():

    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()

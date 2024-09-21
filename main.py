
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("congnghe.ui", self)
      
# Define the main function
def main():
    # Create an instance of the QApplication
    app = QApplication(sys.argv)

    # Create an instance of the LoginSignUpWindow and show it
    window = HomeWindow()
    window.show()

    # Run the application and exit when done
    sys.exit(app.exec())

# Call the main function
if __name__ == "__main__":
    main()



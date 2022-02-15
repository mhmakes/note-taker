import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt6.QtCore import QSize, Qt

# QMainWindow subclass for custom behaviour on instantiation, etc.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("StormNote")

        label = QLabel("Welcome to StormNote!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Align text label w/ center

        self.setMinimumSize(QSize(320, 180)) 

        self.setCentralWidget(label) # makes label the central widget in the Qt layout
    pass

app = QApplication(sys.argv) # instantiate our app, pass command line args
    
window = MainWindow() 
window.show() # displays the window object we just instantiated

app.exec() 
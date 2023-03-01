from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import numpy as np
import pandas as pd
import random

score = 0

df = pd.read_csv("data.csv")

class myGUI(QMainWindow):
    
    global score 
    def __init__(self):
        super(myGUI, self).__init__()
        uic.loadUi("emojiGameGui.ui", self)
        self.show()
        
        
        self.textBrowser_3.setText(df["emoji"][i])
        self.textBrowser.setText(df["hint"][i])
        
        self.pushButton_2.clicked.connect(self.check_response)
        # self.pushButton_3.clicked.connect(self.play_next)
        self.pushButton.clicked.connect(self.show_answer)
        
    def play_next(self):
        pass
    
    def check_response(self):
        global score 
        myRes = self.textEdit.toPlainText().lower()
        if myRes in df["answer"][i].lower():
            score += 1
            self.textEdit.setText("Correct answer!")
            self.play_next()
        else:
            self.textEdit.setText("Incorrect answer...")

        
    
        
    def show_answer(self):
        self.textEdit.setText(df["answer"][i])

        
        
        
# def main():
    # app = QApplication([])
    # window = myGUI()
    # window.show()
    # app.exec_()
    
if __name__ == "__main__":
    while True:
        i = random.randint(0,len(df["emoji"]))
        app = QApplication([])
        window = myGUI()
        window.show()
        app.exec_()
        if window.pushButton_3.clicked :
            continue




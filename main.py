from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
import random

# Global variables
score = 0
attempts = 5
data_file = "data.csv"

# Load data
try:
    df = pd.read_csv(data_file)
    if df.empty or not {"emoji", "hint", "answer"}.issubset(df.columns):
        raise ValueError("Invalid data format in CSV.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

class EmojiGuessingGame(QMainWindow):
    def __init__(self):
        super(EmojiGuessingGame, self).__init__()
        uic.loadUi("GameGUI.ui", self)
        self.show()

        # Connect buttons to methods
        self.btn_check.clicked.connect(self.check_response)
        self.btn_next.clicked.connect(self.play_next)
        self.btn_show_answer.clicked.connect(self.show_answer)

        self.remaining_attempts = attempts
        self.current_index = None

        self.play_next()

    def play_next(self):
        """Load a new emoji and hint."""
        global score
        if self.remaining_attempts == 0:
            QMessageBox.information(self, "Game Over", f"Game Over! Your final score is {score}.")
            self.close()
            return

        self.current_index = random.randint(0, len(df) - 1)
        self.emoji_display.setText(df["emoji"][self.current_index])
        self.hint_display.setText(df["hint"][self.current_index])
        self.score_display.setText(f"Score: {score}")
        self.attempts_display.setText(f"Attempts Left: {self.remaining_attempts}")
        self.answer_input.clear()

    def check_response(self):
        """Check user's answer."""
        global score
        user_response = self.answer_input.text().strip().lower()

        if not user_response:
            QMessageBox.warning(self, "Input Error", "Please enter your guess.")
            return

        correct_answer = df["answer"][self.current_index].lower()
        if user_response in correct_answer:
            score += 1
            self.remaining_attempts = attempts  # Reset attempts for correct answer
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
        else:
            self.remaining_attempts -= 1
            QMessageBox.warning(self, "Incorrect", f"Wrong answer! Attempts left: {self.remaining_attempts}")

        self.play_next()

    def show_answer(self):
        """Display the correct answer."""
        correct_answer = df["answer"][self.current_index]
        self.answer_input.setText(correct_answer)

if __name__ == "__main__":
    app = QApplication([])
    window = EmojiGuessingGame()
    window.show()
    app.exec_()

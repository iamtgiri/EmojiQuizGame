# Emoji Guessing Game - README

## Overview
The Emoji Guessing Game is a desktop application built using Python and PyQt5. The game challenges users to guess the correct word or phrase associated with an emoji, based on a hint provided. Players have a limited number of attempts to guess correctly.

## Features
- Random emoji and hint selection from a CSV file.
- Interactive graphical user interface (GUI) designed using PyQt5.
- Score tracking and attempt management.
- Ability to view the correct answer if needed.
- Game over notification when attempts are exhausted.

## Requirements
- Python 3.6+
- Required Python Libraries:
  - PyQt5
  - pandas

## Installation
1. **Clone the repository or download the files.**
2. **Install dependencies using `pip`:**
   ```bash
   pip install PyQt5 pandas
   ```
3. **Ensure the following files are present in the project directory:**
   - `GameGUI.ui`: The GUI layout file.
   - `data.csv`: The data file containing emoji, hints, and answers. The file should have the following columns:
     - `emoji`: The emoji string.
     - `hint`: A hint related to the emoji.
     - `answer`: The correct answer.

## How to Play
1. Run the application:
   ```bash
   python main.py
   ```
2. A new window will open displaying an emoji and a hint.
3. Enter your guess in the input field and click **Check** to submit.
4. If your answer is correct:
   - Your score increases by 1.
   - Your attempts reset to 5.
5. If your answer is incorrect:
   - You lose one attempt.
6. Use the **Next** button to proceed to the next emoji or **Show Answer** to view the correct answer.
7. The game ends when all attempts are exhausted.

## Customization
You can modify the `data.csv` file to include your own set of emojis, hints, and answers. Ensure that the format matches the required structure.

## Example of `data.csv`
```csv
emoji,hint,answer
😀,A happy face,smile
🏠,Where you live,house
🌧️,Weather with rain,rain
```

## Error Handling
- The application checks if the `data.csv` file is missing or has an incorrect format. If an error occurs, an appropriate message is displayed, and the application exits.
- Warnings are provided for invalid user inputs, such as empty guesses.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Special thanks to the PyQt5 and pandas communities for providing excellent resources and support.
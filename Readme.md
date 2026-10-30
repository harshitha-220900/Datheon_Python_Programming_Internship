# 🎮 Hangman Game Using Python

## 📌 Project Description

The Hangman Game is a simple word-guessing game developed using Python. The program randomly selects a word from an external text file (`words.txt`), and the player must guess the hidden word one letter at a time.

The player gets a limited number of attempts to guess the correct word. If the player guesses all letters correctly before running out of attempts, they win. Otherwise, the game ends.

## 🎯 Project Objectives

- Develop a word-guessing game using Python.
- Read words dynamically from an external text file.
- Use Python's built-in file handling operations.
- Implement random word selection.
- Practice loops, conditional statements, strings, and lists.
- Improve logical thinking and problem-solving skills.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** File Handling, Loops, Conditional Statements, Lists, Strings
- **Modules:** `random`, `os` (optional)
- **Editor:** Visual Studio Code

## 📂 Project Structure

```text
Hangman_Game/
│
├── hangman.py
├── words.txt
└── README.md
```

### File Description

| File | Description |
|---|---|
| `hangman.py` | Main Python game program |
| `words.txt` | Contains words used in the game |
| `README.md` | Project documentation |

## ⚙️ Features

1. Random word selection from a text file.
2. Displays hidden letters using underscores.
3. Allows the player to guess one letter at a time.
4. Tracks the number of incorrect attempts.
5. Prevents repeated letter guesses.
6. Displays a winning message when the word is guessed.
7. Displays the correct word when the player loses.

## 🚀 Installation and Execution

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Clone or Download the Project

Download the project folder to your computer.

### Step 3: Open the Project

Open the `Hangman_Game` folder in Visual Studio Code.

### Step 4: Run the Program

Open the terminal and execute:

```bash
python hangman.py
```

## 🎮 How to Play

1. Run the Python program.
2. The system randomly selects a word from `words.txt`.
3. The hidden word is displayed as underscores.
4. Enter one letter at a time.
5. Correct guesses reveal the letters.
6. Incorrect guesses reduce the remaining attempts.
7. Guess the complete word to win the game.

## 💻 Sample Output

```text
===== WELCOME TO HANGMAN =====

Word: _ _ _ _ _ _
Attempts remaining: 6

Guess a letter: p
Correct guess!

Word: p _ _ _ _ _
Attempts remaining: 6

Guess a letter: y
Correct guess!

Congratulations! You won!
```

## 📚 Python Concepts Implemented

- **File Handling:** Reads words from `words.txt`.
- **Random Module:** Selects a random word.
- **While Loop:** Continues the game until the player wins or loses.
- **If-Else Statements:** Checks whether the guessed letter is correct.
- **Lists:** Stores previously guessed letters.
- **String Operations:** Displays the hidden word and revealed letters.

## 🔮 Future Enhancements

- Add difficulty levels (Easy, Medium, Hard).
- Display Hangman graphics using ASCII art.
- Add a score tracking system.
- Add a graphical user interface using Tkinter.
- Add multiple categories such as animals, countries, and technology.
- Allow users to play multiple rounds.

## 👩‍💻 Author

**Project Name:** Hangman Game Using Python

**Domain:** Python Programming

## 📝 Conclusion

The Hangman Game project demonstrates the practical implementation of Python programming concepts such as file handling, random selection, loops, conditional statements, and lists.

It provides an interactive word-guessing experience while helping beginners understand Python fundamentals and develop programming skills.
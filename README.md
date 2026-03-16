# 🎲 Visual Dice Rolling Simulator

A high-fidelity Command-Line Interface (CLI) simulation that models probability through random number generation and visualizes results using dictionary-based ASCII mapping.

## 📝 Project Description
The **Dice Rolling Simulator** is more than just a random number generator; it is a demonstration of efficient data structures and robust user-interaction logic. The program allows users to simulate rolling any number of six-sided dice. 

The core of the application uses a Python **Dictionary** to map integer results to multi-line ASCII art representations of dice faces. Furthermore, it implements a "Defensive Programming" approach by utilizing `try-except` blocks to handle invalid user inputs (like decimals or strings) without crashing the simulation.

## 🧠 What I Learned
As a BS Artificial Intelligence student, this project served as a deep dive into:
- **Dictionary Mapping:** Implementing $O(1)$ time-complexity lookups to replace inefficient $if-else$ ladders.
- **Exception Handling:** Using `try-except` blocks to manage `ValueErrors` and ensure a smooth User Experience (UX).
- **Control Flow:** Mastering the `continue` and `break` keywords to manage complex loop restarts and exits.
- **Cumulative Logic:** Managing state by calculating the sum of multiple random variables in a single session.

## 💻 Technical Highlights
- **Data Structure:** Python Dictionary for mapping keys (1-6) to multi-line string values.
- **Randomization:** Use of the `random` module for uniform distribution of dice rolls.
- **Input Sanitization:** Converting strings to integers with built-in error traps.

## 📄 Sample Output
```text
How many dice do you want to roll: 2

Roll 1:
-----------
|  O   O  |
|         |
|  O   O  |
-----------
Value: 4

Roll 2:
-----------
|  O      |
|    O    |
|      O  |
-----------
Value: 3

=========================
TOTAL SUM: 7
=========================

Roll again? (y/n): n
Goodbye, Syed! Happy coding.

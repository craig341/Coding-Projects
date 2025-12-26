## Project Challenges

### 1. Starter | Guessing Game

**Challenge Description:**
Develop a simple number guessing game. The program should randomly select a number between 1 and 100, and prompt the user to guess the number. After each guess, the program should provide feedback: "too high", "too low", or "correct". The game should track the number of attempts it takes for the user to guess the number correctly and display this count when the user guesses correctly.

**Requirements:**
- Use Python's `random` module to generate the random number.
- Ensure the user inputs are valid (i.e., no letters or symbols, and the numbers are within the valid range).
- The game should continue prompting the user until the correct guess is made.
- After the correct guess, the program should offer to restart the game or exit.

### 2. Intermediate | Game of Rock, Paper, Scissors

**Challenge Description:**
Create a Rock, Paper, Scissors game that a player can play against the computer. The player should be able to choose "rock", "paper", or "scissors" through user input, while the computer's choice should be generated randomly. The program should compare the choices, determine the winner of each round, and keep score for multiple rounds until the player decides to stop playing.

**Requirements:**
- Use the `random` module for the computer's choice.
- Implement rules to determine the winner: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
- Keep track of the score, including how many games have been won by the player and the computer.
- The program should handle invalid inputs gracefully and prompt the user to choose again.
- Provide an option to quit the game after each round.

### 3. Advanced | Password Generator

**Challenge Description:**
Develop a secure password generator that creates passwords according to user-specified criteria. The user should be able to specify the length of the password and whether to include uppercase letters, lowercase letters, numbers, and special symbols. The program should generate a random password that conforms to these specifications.

**Requirements:**
- Implement functionality to include/exclude uppercase letters, lowercase letters, numbers, and special characters based on user input.
- Ensure that the generated password respects the user’s length specification.
- Use a strong random number generator to ensure password security.
- The program should allow the user to generate a new password with the same or different criteria without restarting the program.
- Optionally, implement checks to ensure the password meets common security standards (e.g., must contain at least one number and one symbol).

These challenges are designed to cater to different skill levels and focus on fundamental programming concepts, user input handling, working with modules, and algorithmic thinking. Each project builds upon the previous one, offering a natural learning curve.
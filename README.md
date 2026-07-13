# Program Logic
The program starts by displaying Player 1 as the computer (AI). Then, it asks the user to enter their name and the starting number of sticks.
The AI starts the game first. The program uses a while loop to continue the game while there are still sticks remaining in the pile.
During each turn, the program checks whose turn it is using the turn variable:

- If turn = 1, the AI makes a move automatically by removing sticks.
   
-  If turn = 2, the user enters the number of sticks they want to remove. The program checks that the input is valid and allows only 1 or 2 sticks to be removed.

After a valid move, the program updates the number of remaining sticks. It then checks if all sticks have been removed. If a player removes the last stick, that player loses and the other player wins.
If the game is not finished, the program switches the turn to the other player and continues the loop.
The program ends when there are no sticks left and displays the final result.

# Turn Tracking
The program keeps track of the player's turn by using a variable called turn.
At the beginning of the game, the variable turn is set to 1, which represents the AI player. This allows the computer to make the first move.
After each player's move, the program changes the value of turn:

- If turn == 1, it changes to 2 so the human player can play.

- If turn == 2, it changes back to 1 so the AI can play.

This switching process continues inside the while loop until all sticks are removed. By using the turn variable, the program always knows which player should make the next move.

# How the Computer is Made Smart
The computer AI makes decisions automatically during its turn. The AI uses a simple strategy to choose its move.
When it is possible, the AI removes 2 sticks because removing more sticks helps reduce the number of remaining sticks faster. If there is only 1 stick left, the AI removes the remaining stick.
The AI decision is controlled by an if-else statement:

- If the number of remaining sticks is 2 or more, the AI removes 2 sticks.

- If only 1 stick remains, the AI removes 1 stick.

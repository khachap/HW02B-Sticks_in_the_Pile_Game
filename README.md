# Explanation of Turn Tracking
The program keeps track of the player's turn by using a variable called turn.
At the beginning of the game, the variable turn is set to 1, which represents the AI player. This allows the computer to make the first move.
After each player's move, the program changes the value of turn:
    If turn == 1, it changes to 2 so the human player can play.
    If turn == 2, it changes back to 1 so the AI can play.
This switching process continues inside the while loop until all sticks are removed. By using the turn variable, the program always knows which player should make the next move.

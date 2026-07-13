# HW02B-Sticks_in_the_Pile_Game

# Display Player 1 as the computer (AI)
print("Player 1 (COMPUTER): AI")

# Get Player 2's name from the user
player2 = input("Enter Player 2 name: ")

# Ask the user to enter the starting number of sticks
sticks = int(input("Enter starting number of sticks: "))

# Set Player 1 (AI) to take the first turn
turn = 1

# Continue the game while there are sticks remaining
while sticks > 0:

    # AI's turn
    if turn == 1:
        print("\nAI's turn")
        print("Sticks remaining:", sticks)

        # AI automatically chooses how many sticks to remove
        # Remove 2 sticks whenever possible, otherwise remove 1
        if sticks >= 2:
            remove = 2
        else:
            remove = 1

        # Show the AI's move
        print("AI removes", remove, "stick(s).")

    # Human player's turn
    else:
        print("\n" + player2 + "'s turn")
        print("Sticks remaining:", sticks)

        # Ask the player to remove 1 or 2 sticks
        remove = int(input("Remove 1 or 2 sticks: "))

        # Validate that the input is either 1 or 2
        while remove != 1 and remove != 2:
            print("Invalid input. Please enter 1 or 2.")
            remove = int(input("Remove 1 or 2 sticks: "))

        # Make sure the player does not remove more sticks than remain
        while remove > sticks:
            print("Invalid move. Not enough sticks remaining.")
            remove = int(input("Remove 1 or 2 sticks: "))

            # Check again that the new input is valid
            while remove != 1 and remove != 2:
                print("Invalid input. Please enter 1 or 2.")
                remove = int(input("Remove 1 or 2 sticks: "))

    # Remove the selected number of sticks from the pile
    sticks = sticks - remove

    # Check if all sticks have been removed
    if sticks == 0:
        # If AI removed the last stick, AI loses
        if turn == 1:
            print("\nAI removed the last stick.")
            print("AI loses!")
            print(player2, "wins!")
        # If the human player removed the last stick, the human loses
        else:
            print("\n" + player2 + " removed the last stick.")
            print(player2, "loses!")
            print("AI wins!")
        break

    # Switch turns between AI and the human player
    if turn == 1:
        turn = 2
    else:
        turn = 1
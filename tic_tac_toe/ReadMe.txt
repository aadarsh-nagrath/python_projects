The Tic Tac Toe game is a two-player game where each player takes turns marking a space on a 3x3 grid with their symbol (usually an "X" or an "O"). 
The goal is to place three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent does. 
If all of the spaces on the grid are filled and neither player has won, the game is a draw.

The code starts by creating an empty 3x3 grid represented as a list of 9 spaces, each represented by a space character ' '. 
The print_board function is used to display the current state of the board by formatting the contents of the board list into a 3x3 grid with vertical lines.

The player_move function takes a player's symbol as an input and prompts the player to enter their move by choosing a space on the grid (represented by a number from 1 to 9). 
If the chosen space is empty, the player's symbol is placed on that space. If the space is already taken, the function will prompt the player to choose another space.

The is_victory function checks if a player has won by checking if any of the win combinations (represented as a list of tuples of the indices of the spaces on the grid) are filled with the player's symbol. 
If a player has won, the function returns True.

The is_draw function checks if the game is a draw by checking if there are any empty spaces on the board. If all spaces are filled and there is no winner, the function returns True.

The game starts with player "X" taking the first turn and alternates between the two players until either a player wins or the game is a draw. 
The print_board function is called at the start of each turn to display the current state of the board, and the player_move function is used to get the player's move. 
If a player wins, a message is displayed to congratulate the winner. If the game is a draw, a message is displayed to indicate that the game has ended in a draw.
You can use jupyter notebooks to run the code or any compiler.
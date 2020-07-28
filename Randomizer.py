import random
modified_board = []

#The point of these functions is to generate a "random" sudoku board with enough possible variations that getting the same one twice in a row is unlikely.

#This function picks a random board out of five choices and then returns it. The starter_board variable is a list of a completed sudoku board that will be modified farther in.
def starter_board_picker():
    board = random.randint(1,5)
    if board == 1:
        starter_board = [5, 3, 4, 6, 7, 8, 9, 1, 2, 6, 7, 2, 1, 9, 5, 3, 4, 8, 1, 9, 8, 3, 4, 2, 5, 6, 7, 8, 5, 9, 7, 6, 1, 4, 2, 3, 4, 2, 6, 8, 5, 3, 7, 9, 1, 7, 1, 3, 9, 2, 4, 8, 5, 6, 9, 6, 1, 5, 3, 7, 2, 8, 4, 2, 8, 7, 4, 1, 9, 6, 3, 5, 3, 4, 5, 2, 8, 6, 1, 7, 9]
    if board == 2:
        starter_board = [4, 3, 5, 2, 6, 9, 7, 8, 1, 6, 8, 2, 5, 7, 1, 4, 9, 3, 1, 9, 7, 8, 3, 4, 5, 6, 2, 8, 2, 6, 1, 9, 5, 3, 4, 7, 3, 7, 4, 6, 8, 2, 9, 1, 5, 9, 5 , 1, 7, 4, 3, 6, 2, 8, 5, 1,9 ,3 ,2, 6, 8, 7, 4, 2, 4, 8, 9, 5, 7, 1, 3, 6, 7, 6, 3, 4, 1, 8, 2, 5, 9]
    if board == 3:
        starter_board = [5, 3, 4, 6, 7, 8, 9, 1, 2, 6, 7, 2, 1, 9, 5, 3, 4, 8, 1, 9, 8, 3, 4, 2, 5, 6, 7, 8, 5, 9, 7, 6, 1, 4, 2, 3, 4, 2, 6, 8, 5, 3, 7, 9, 1, 7, 1, 3, 9, 2, 4, 8, 5, 6, 9, 6, 1, 5, 3, 7, 2, 8, 4, 2, 8, 7, 4, 1, 9, 6, 3, 5, 3, 4, 5, 2, 8, 6, 1, 8, 9]
    if board == 4:
        starter_board = [4, 2, 3, 6, 9, 7, 8, 1, 5, 6, 9, 1, 5, 3, 8, 4, 7, 2, 5, 8, 7, 4, 2, 1, 6, 3, 9, 3, 1, 9, 8, 7, 5, 2, 6, 4, 2, 5, 6, 1, 4, 9, 3, 8, 7, 7, 4, 8, 3, 6, 2, 5, 9, 1, 9, 6, 4, 2, 1, 3, 7, 5, 8, 1, 3, 5, 7, 8, 4, 9, 2, 6, 8, 7, 2, 9, 5, 6, 1, 4, 3]
    if board == 5:
        starter_board = [1, 5, 2, 4, 6, 9, 3, 7, 8, 7, 8, 9, 2, 1, 3, 4, 5, 6, 4, 3, 6, 5, 8, 7, 2, 9, 1, 6, 1, 3, 8, 7, 2, 5, 4, 9, 9, 7, 4, 1, 5, 6, 8, 2, 3, 8, 2, 5, 9, 3, 4, 1, 6, 7, 5, 6, 7, 3, 4, 8, 9, 1, 2, 2, 4, 8, 6, 9, 1, 7, 3, 5, 3, 9, 1, 7, 2, 5, 6, 8, 4]
    return starter_board

'''This is the end function that utilizes every other in order to finish generating a "random" board. It first picks the starter board
 then has a 50/50 chance of rotating or not rotating the board. The final function board_reverse reverses the total order of the board
 and then returns the final board that the player will play, randomized_board.'''
def board_randomize():
    starter_board = starter_board_picker()
    rotate = random.randint(0,1)
    if rotate == 1:
        modified_board = board_rotate(starter_board)
    else:
        modified_board = starter_board
    randomized_board = board_reverse(modified_board)
    return randomized_board
    

#board_rotate takes the given sudoku board and rotates it 90 degrees around the center in order to generate a seemingly new board.
def board_rotate(starter_board):
	for a in range(8,81,9):
	   row_1_new = starter_board[a]
	   modified_board.append(row_1_new)
	for b in range(7,81,9):
	   row_2_new = starter_board[b]
	   modified_board.append(row_2_new)
	for c in range(6,81,9):
	   row_3_new = starter_board[c]
	   modified_board.append(row_3_new)
	for d in range(5,81,9):
	   row_4_new = starter_board[d]
	   modified_board.append(row_4_new)
	for e in range(4,81,9):
	   row_5_new = starter_board[e]
	   modified_board.append(row_5_new)
	for f in range(3,81,9):
	   row_6_new = starter_board[f]
	   modified_board.append(row_6_new)
   	for g in range(2,81,9):
	   row_7_new = starter_board[g]
	   modified_board.append(row_7_new)
   	for h in range(1,81,9):
	   row_8_new = starter_board[h]
	   modified_board.append(row_8_new)
	for i in range (0,81,9):
	   row_9_new = starter_board[i]
	   modified_board.append(row_9_new)
	return modified_board

#board_reverse takes the already previously modified board and takes it and fully reverses the position of each number: 1 becomes 81, 2 becomes 80, and so on.
def board_reverse(modified_board):
    reverse = random.randint(0,1)
    if reverse == 1:
        modified_board.reverse()
    else:
        return modified_board
        


#main

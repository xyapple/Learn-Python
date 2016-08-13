# Tic-Tac-Toe Game with Computer AI

import random
# print a board

def printBoard(board):
    print('  |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |   |')


#  request player to choose which letter
# Returns a list with the player’s letter as the first item,
# and the computer's letter as the second.
def chooseLetter():
    letter = ''
    while not (letter == 'X' or letter =='O'):
        print("Please choose a letter 'X' or 'O' to be your letter.")
        letter = input().upper()

#   if the X is player, O will be AI;
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'player'

# This function is only TRUE if player wants to play again!
def playAgain():
    print('Do you want to play again? (Y or N)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def winRule(bo, le):
     return((bo[7]==le and bo[8]==le and bo[9]==le) or  #across the top
           (bo[4]==le and bo[5]==le and bo[6]==le) or # across the mid
           (bo[1]==le and bo[2]==le and bo[3]==le) or #across the bottom
           (bo[1]==le and bo[5]==le and bo[9]==le) or #diagonal the (1,5,9)
           (bo[7]==le and bo[5]==le and bo[3]==le) or #diagonal the (3,5,7)
           (bo[1]==le and bo[4]==le and bo[7]==le) or #down the left
           (bo[2]==le and bo[5]==le and bo[8]==le) or #down the mid
           (bo[3]==le and bo[6]==le and bo[9]==le)) #down the right

#make a duplication of the board list and return it
def boardCopy(board):
    copyBoard = []

    for i in board:
        copyBoard.append(i)
    return copyBoard

#check to see if the space is available for the move
def spaceFree(board, move):
    return board[move] == ' '

#player move enter
def playerMove(board):

    move =' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceFree(board, int(move)):
        print('Please enter a number (1-9) for your next move?')
        move = input()
    return int(move)

# Returns a valid move from the passed list on the passed board.
#  Returns None if there is no valid move.

def validMove(board, movesList):

    possibleMoves =[]
    for i in movesList:
        if spaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#AI move enter
def AImove(board, AIle):
    if AIle == 'X':
        playerLe =='O'
    else:
        playerLe =='X'

# 1, check if AI win the next move
    for i in range(1, 10):
        copy = boardCopy(board)
        if spaceFree(copy, i):
            makeMove(copy, AIle, i)
            if winRule(copy, AIle):
                return i

# 2, check if player win the nex move
    for i in range(1, 10):
        copy = boardCopy(board)
        if spaceFree(copy, i):
            makeMove(copy, playerLe, i)
            if winRule(copy, playerLe):
                return i

# 3, try to get corner if there is a space
    move = validMove(board, [1, 3, 7, 9])
    if move != None:
        return move

# 4, try to take center if there is a space
    if spaceFree(board, 5):
        return 5

# 5, try to take the rest of the space:
    return validMove(board, [2, 4, 6, 8])

# check the board is full or not
def boardFull(board):
    for i in range(1, 10):
        if spaceFree(board, i):
            return False
    return True

# Game On!

print('Welcome to Tic-Tac-Toe!')

while True:
    #reset board
    theBoard = [' '] * 10
    playerLe, AIle = chooseLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameStart = True

    # Running the player's turn. Loop that'll go back and forth as long as
    # gameStart stays True
    while gameStart:
        # Players' turn

        if turn == 'player':
            printBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLe, move)

            if winRule(theBoard, playerLe):
               printBoard(theBoard)
               print('Yeah! You win the Game!')
               gameStart = False

            else:
                if boardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'AI'

        else:
            # AI turn

            move = AImove(theBoard, AIle)
            makeMove(theBoard, AIle, move)

            if winRule(theBoard, AIle):
                printBoard(theBoard)
                print('Sorry, you lose. AI win the Game!')
                gameStart = False

            else:
                if boardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break

                else:
                    turn = 'player'

        if not playAgain():
            break






















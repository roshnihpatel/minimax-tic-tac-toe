import random
import math


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]  )
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]  )
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]  )
    print("\n\n")
   
def insertLetter(board, pos, let):
    board[pos] = let
    
def isBoardFull(board):
    return board.count(' ') < 2

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le ) or
    (bo[7] == le and bo[8] == le and bo[9] == le ) or 
    (bo[1] == le and bo[4] == le and bo[7] == le ) or 
    (bo[2] == le and bo[5] == le and bo[9] == le ) or 
    (bo[3] == le and bo[6] == le and bo[9] == le ) or 
    (bo[1] == le and bo[5] == le and bo[9] == le ) or 
    (bo[3] == le and bo[5] == le and bo[7] == le ))

def isPostitionFree(board, pos):
    return board[pos] == ' '

def randomMove(board):
    run = True
    while run:
        if isBoardFull(board):
            return 0
        move = random.randrange(1,10)
        if isPostitionFree(board, move):
            return move

def bestMove(board):
    bestScore = -math.inf
    bestMove = None
    for i in range(1,10):
        if isPostitionFree(board, i):
            insertLetter(board, i, 'O') # make a potential move
            score = minimax(board, 0, True) # get score of the move
            insertLetter(board, i, ' ') # undo the move
            if score > bestScore:
                bestScore = score
                bestMove = i
    if not(bestMove):
        return 0
    
    return bestMove

def evaluate(state):
    """
    returns + 10 if computer wins, -10, if hunan wins and 0 otherwise
    """
    if isWinner(state, 'O'):
        return 1
    elif isWinner(state, 'X'):
        return -1
    else:
        return 0
        
def minimax(board, depth, isMax):
    score = evaluate(board)
    if isBoardFull(board) or score:
        return score


    if isMax:
        bestScore = -math.inf
        for i in range(1,10):
            if isPostitionFree(board, i):
                insertLetter(board, i, 'X') # make a potential move
                score = minimax(board, depth + 1, False) # get score of the move
                insertLetter(board, i, ' ') # undo the move
                bestScore = max(bestScore, score)
        return bestScore
        
    else:
        bestScore = math.inf
        for i in range(1,10):
            if isPostitionFree(board, i):
                insertLetter(board, i, 'O') # make a potential move
                score = minimax(board, depth + 1, True) # get score of the move
                insertLetter(board, i, ' ') # undo the move
                bestScore = min(bestScore, score)
        return bestScore

def playerMove(board):
    run = True
    while run:
        move = input("Chose a position from 1-9 to place 'X': ")
        try:
            move = int(move)
            if move > 0 and move < 10: # check number is between 1-9
                if isPostitionFree(board, move):
                    insertLetter(board, move, 'X')
                    run = False
                else:
                    print("space is occupied")
            else:
                print("input out of range")
        except:
            print("invalid input")
            

def main():
    c = 0
    board = [' ' for x in range(10)]
    print("Welcome to tic tac toe!\nPlay against the computer ('X')")
    printBoard(board)
    
    while not(isBoardFull(board)):
        if not isWinner(board, 'O'): # Check if computer won in thier turn
            playerMove(board) #player choses where to place X
            printBoard(board)
        else:
            print('Computer wins, good luck next time')
            break
        
        if not(isWinner(board, 'X')): # Check player has won in their turn
            move = bestMove(board)
            if move == 0:
                print("It's a Tie!!!")
            else:
                print(move)
                insertLetter(board, move, 'O')
                print(f"Computer has placed 'O' on postition {move}")
                printBoard(board)
        else:
            print('You won!!!!')
            break
                

main()

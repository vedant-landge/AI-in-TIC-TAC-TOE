board = [' ' for x in range(17)]


def inserts(X_O, pos):
    board[pos] = X_O


def isFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
    print('   |   |   |')
    print('----------------')
    print('   |   |   |')
    print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |   |')
    print('----------------')
    print('   |   |   |')
    print(' ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12])
    print('   |   |   |')
    print('----------------')
    print('   |   |   |')
    print(' ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ' + board[16])
    print('   |   |   |')


def isWinner(a1, a2):
    return (a1[1] == a2 and a1[2] == a2 and a1[3] == a2 and a1[4] == a2) or \
           (a1[5] == a2 and a1[6] == a2 and a1[7] == a2 and a1[8] == a2) or \
           (a1[9] == a2 and a1[10] == a2 and a1[11] == a2 and a1[12] == a2) or \
           (a1[13] == a2 and a1[14] == a2 and a1[15] == a2 and a1[16] == a2) or \
           (a1[1] == a2 and a1[5] == a2 and a1[9] == a2 and a1[13] == a2) or \
           (a1[2] == a2 and a1[6] == a2 and a1[10] == a2 and a1[14] == a2) or \
           (a1[3] == a2 and a1[7] == a2 and a1[11] == a2 and a1[15] == a2) or \
           (a1[4] == a2 and a1[8] == a2 and a1[12] == a2 and a1[16] == a2) or \
           (a1[1] == a2 and a1[6] == a2 and a1[11] == a2 and a1[16] == a2) or \
           (a1[4] == a2 and a1[7] == a2 and a1[10] == a2 and a1[13] == a2)

def youMove():
    run = True
    while run:
        Your_move = input('Where do you want to place an \'X\' (1-16): ')
        try:
            Your_move = int(Your_move)
            if Your_move > 0 and Your_move < 17:
                if isFree(Your_move):
                    run = False
                    inserts('X', Your_move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def AIMove():
    possibleMoves = [x for x, X_O in enumerate(board) if X_O == ' ' and x != 0]
    AI_move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                AI_move = i
                return AI_move

    winnings1 = []
    for i in possibleMoves:
        if i in [13, 6, 11, 4]:
            winnings1.append(i)
    if len(winnings1) > 0:
        AI_move = AISelectionMove(winnings1)
        return AI_move

    winnings2 = []
    for i in possibleMoves:
        if i in [16, 7, 10, 1]:
            winnings1.append(i)
    if len(winnings2) > 0:
        AI_move = AISelectionMove(winnings2)
        return AI_move

    edges = []
    for i in possibleMoves:
        if i in [2, 3, 5, 9, 14, 15, 12, 8]:
            edges.append(i)

    if len(edges) > 0:
        AI_move = AISelectionMove(edges)

    return AI_move


def AISelectionMove(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            youMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = AIMove()
            if move == 0:
                print('Tie Game!')
            else:
                inserts('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('You\'ve won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


while True:
    choice = input('Do you want to play again? (Y/N)')
    if choice.lower() == 'y' or choice.lower == 'yes':
        board = [' ' for x in range(17)]
        print('-----------------------------------')
        main()
    else:
        break
import math

def check_board(board):
    for row in board:
        if row[0]==row[1]==row[2]:
            if row[0]=="x":
                return 10
            elif row[0]=="O":
                return -10
    for column in range(3):
        if board[0][column]==board[1][column]==board[2][column]:
            if board[0][column]=="x":
                return 10
            elif board[0][column]=="O":
                return -10
    
    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0]=="x":
            return 10
        elif board[0][0]=="O":
            return -10
    return 0

def is_full(board):
    return all(cell != '_' for row in board for cell in row)

def minimax(board, depth, max_pl):
    score = check_board(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_full(board):
        return 0
    
    if max_pl:
        best= -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]=='_':
                    board[i][j]= 'X'
                    best = max(best, minimax(board, depth+1,False))
                    board[i][j] = '_'
        return best
    else:
        best= math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]=='_':
                    board[i][j]= 'O'
                    good = min(best, minimax(board, depth+1,True))
                    board[i][j] = '_'
        return best
def best_move(board):
    best_value = -math.inf
    best_move =(-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                board[i][j]= 'X'
                value = minimax(board,0,False)
                if value > best_value:
                    best_value= value
                    best_move= (i,j)
                board[i][j] = '_'
    return best_move

board=[
    ['X','O','X'],
    ['_','O','_'],
    ['X','_','_']
]
best_move= best_move(board)
print(f"Best move for AI: Row {best_move[0]+1}, Column {best_move[1]+1}")

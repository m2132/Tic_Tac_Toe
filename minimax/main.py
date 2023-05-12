import time

from tic_tac_toe import TicTacToe
from minimax import minimax

game = TicTacToe()

def computer(game):
    max_value = float('-inf')
    best_child = None
    for c in game.children():
        value = minimax(game, True)
        if value > max_value:
            max_value = value
            best_child = c
    return best_child

def user(game):
    index = input("enter index: ")
    while game.board[index] != ' ':
        index = input("invalid place, enter again: ")
    
    game.board[index] = game.turn
    return game

is_computer = True
while game.get_winner() is None:
    time.sleep(2)
    print(game)
    if is_computer:
        game = computer(game)
    else:
        game = user(game)

winner = game.get_winner()
if winner is not None:
    print(f'{winner} is the winner!')
else:
    print('It is a draw')

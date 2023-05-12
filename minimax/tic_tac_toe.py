class TicTacToe:
    
    def __init__(self):

        self.turn = 'X'

        self.board = [' '] * 9

    def value(self):
        pass

    def get_winner(self):
        board = self.board

        # row
        for i in range(3):
            if board[i * 3] == board[i * 3 + 1] and board[i * 3 + 1] == board[i * 3 + 2]:
                return board[i * 3]

        # col
        for i in range(3):
            if board[i] == board[i + 3] and board[i + 3] == board[i + 6]:
                return board[i]
        
        # diag
        if board[0] == board[4] and board[4] == board[8]:
            return board[0]
        
        if board[2] == board[4] and board[4] == board[6]:
            return board[2]
        
        return None


    def children(self):
        my_children = []
        for i, cell in enumerate(self.board):
            if cell == ' ':
                tic = TicTacToe()
                tic.board = [*self.board]

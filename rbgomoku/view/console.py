import re
from core import NotBlankSpaceException, OverwritePositionException
from core.board import Board, Piece
from core.player import HumanPlayer


def print_formatted(s):
    print("{0:#^50}".format(s))

class Gomoku:
    def __init__(self, board_size, sequence_victory):
        self.board = Board(board_size, sequence_victory)
        self.p1 = HumanPlayer(self.board, Piece.BLACK)
        self.p2 = HumanPlayer(self.board, Piece.WHITE, first=False)
        self.current_player = self.p1
        self.print_board()

    def print_board(self):
        print(self.board)
        print('\n\n')

    def run(self):
        running = True
        while running:
            move = input(
                '[{}] Enter with position [row,col] or "q" to quit game: '.format(self.current_player))
            print()

            if 'q' in move:
                print_formatted(' Quit game ')
                running = False

            row, col = re.findall('(\d+)', move)
            row, col = int(row), int(col)
            last_index = len(self.board.table) - 1
            if (row > last_index) or (col > last_index):
                print('Is permitted only row and col between 0 and {}\n\n'.format(last_index))
                continue

            try:
                winner = self.current_player.play(row, col)
            except OverwritePositionException:
                print("Position not allowed!!\n\n")
                continue
            except NotBlankSpaceException:
                print_formatted(' There was no winner!!! ')
                running = False

            self.print_board()

            if winner != Piece.NONE:
                print_formatted(' Congratulations!!! ')
                print_formatted(' {} is Winner! '.format(self.current_player))
                running = False

            self.current_player = self.p2 if self.current_player == self.p1 else self.p1

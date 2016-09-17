import re
from core.board import Board, Square, Piece
from core.exceptions import NotBlankSpaceException, OverwritePositionException
from core.player import HumanPlayer, MachinePlayer


def print_formatted(s):
    print("{0:#^50}".format(s))

class Gomoku:
    def __init__(self):
        self.board = Board()
        self.p1 = self.select_player()
        self.p2 = HumanPlayer(self.board, Piece.WHITE, first=False)
        self.current_player = self.p1
        self.print_board()

    def select_player(self):
        print('Who would like to play?\n\n')

        while True:
            a = input('The Human Player (1)\nThe Machine Player (2)\nQuit (q)\n\n')

            if a == '1':
                return HumanPlayer(self.board, Piece.BLACK)
            if a == '2':
                return MachinePlayer(self.board, Piece.BLACK)
            if a == 'q':
                print('Bye Bye!')
                exit(0)


    def print_board(self):
        print(self.board)
        print('\n\n')

    def run(self):
        running = True
        while running:
            square = None
            if not isinstance(self.current_player, MachinePlayer):
                move = input(
                    '[{}] Enter with position [row,col] or "q" to quit game: '.format(self.current_player))
                print()

                if 'q' in move:
                    print_formatted(' Quit game ')
                    exit(0)

                row, col = re.findall('(\d+)', move)
                square = Square(int(row), int(col))
                last_index = len(self.board.table) - 1
                if (square.row > last_index) or (square.col > last_index):
                    print('Is permitted only row and col between 0 and {}\n\n'.format(last_index))
                    continue

            winner = Piece.NONE
            try:
                print('Wait move...')
                winner = self.current_player.play(square)
            except OverwritePositionException:
                print("Position not allowed!!\n\n")
                continue
            except NotBlankSpaceException:
                print_formatted(' There was no winner!!! ')
                running = False

            self.print_board()
            print('Score: {}'.format(self.board.current_score))

            if winner != Piece.NONE:
                print_formatted(' Congratulations!!! ')
                print_formatted(' {} is Winner! '.format(self.current_player))
                running = False

            self.current_player = self.p2 if self.current_player == self.p1 else self.p1

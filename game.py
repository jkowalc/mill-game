from exceptions import WrongPawnNumberError
from game_boards.game_board import GameBoard
from game_boards.nine_pawn_board import NinePawnBoard
from game_boards.six_pawn_board import SixPawnBoard
from game_boards.three_pawn_board import ThreePawnBoard
from game_boards.twelve_pawn_board import TwelvePawnBoard
from player import ComputerPlayer, Player


class Game:
    def __init__(self, playerA, playerB, pawns_num):
        self.playerA = playerA
        self.playerB = playerB
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.game_phase = 1
        self.init_board()


    def init_board(self):
        if self.pawns_num == 12:
            self.board = TwelvePawnBoard()
        elif self.pawns_num == 9:
            self.board = NinePawnBoard()
        elif self.pawns_num == 6:
            self.board = SixPawnBoard()
        elif self.pawns_num == 3:
            self.board = ThreePawnBoard()

    def check_winning_conditions(self):
        pass

    def check_tie_conditions(self):
        pass

    def execute_turn(self, player: Player):
        if player.has_placed_all_pawns():
            moves = self.board.get_possible_moves_for_player(player)
            selected = player.select_move(moves)
            self.board.execute_move(selected)
            player.execute_move(selected)
            dest = selected[1]
            if self.board.check_if_pawn_in_mill(dest):
                pass  # remove one opponent's pawn
            self.check_tie_conditions()
            self.check_winning_conditions()
            if self.playerA == player:
                self.execute_turn(self.playerB)
            elif self.playerB == player:
                self.execute_turn(self.playerA)
        else:
            possible_destinations = self.board.get

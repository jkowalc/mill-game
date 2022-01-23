from exceptions import WrongPawnNumberError
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

    def execute_player_turn(self, player: Player):
        pass

    def execute_computer_turn(self, player: Player):
        pass

    def execute_turn(self, player: Player):
        if isinstance(player, ComputerPlayer):
            self.execute_computer_turn(player)
        else:
            self.execute_player_turn(player)
        if self.playerA == player:
            self.execute_turn(self.playerB)
        elif self.playerB == player:
            self.execute_turn(self.playerA)

from __future__ import annotations

from exceptions import WrongPawnNumberError


class Player:
    def __init__(self, name, symbol, pawns_num=9, pawns_on_board=None):
        self.name = name
        self.symbol = symbol
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.pawns_on_board = pawns_on_board

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

    def __str__(self):
        return self.symbol

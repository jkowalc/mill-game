from __future__ import annotations


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

    def __str__(self):
        return self.symbol

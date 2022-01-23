from __future__ import annotations


class Player:
    def __init__(self, name):
        self.name = name

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

from __future__ import annotations


class Player:
    def __init__(self, name):
        self.name = name

    def __eq__(self, __o: Player) -> bool:
        return self.name == __o.name

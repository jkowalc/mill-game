def get_game_variant() -> int:
    print("Possible variants:\n1. Three men's morris\n2. Six men's morris\n3. Nine men's morris\n4. Twelve men's morris")
    inp = input("Choose one:")
    if inp not in {"1", "2", "3", "4"}:
        print("Wrong value")
        return get_game_variant()
    else:
        return {"1": 3, "2": 6, "3": 9, "4": 12}[int(inp)]


def get_game_mode() -> str:
    print("Possible game modes:\n1. Player vs Player\n2. Player vs Computer\n3. Player vs Smart Computer")
    inp = input("Choose one:")
    if inp not in {"1", "2", "3"}:
        print("Wrong value")
        return get_game_mode()
    else:
        return int(inp)


def get_player_name(letter="") -> str:
    inp = input(f"Enter player{letter}'s name:")
    return inp

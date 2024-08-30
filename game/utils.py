from game.models import Player, Enemy
from settings import MODES, INVALID_MODE_MESSAGE, INVALID_NAME_MESSAGE


# Function to display the game menu
def show_menu() -> None:
    print("1. Start Game")
    print("2. View Scores")
    print("3. Exit")


# Function to get user input
def get_user_input(prompt: str) -> str:
    return input(prompt).strip()


# Function to print a message
def print_message(message: str) -> None:
    print(message)


# Function to create a player name
def create_player() -> tuple[Player, str]:
    name = ""
    while not name:
        name = get_user_input("Enter your name: ").strip()
        if not name:
            print(INVALID_NAME_MESSAGE)

    return Player(name)


# Function handles the selection of the game mode
def select_mode() -> str:
    mode_key = ""
    while mode_key not in MODES:
        mode_key = get_user_input("Select difficulty (1 - Normal, 2 - Hard): ").strip()
        if mode_key not in MODES:
            print(INVALID_MODE_MESSAGE)

    mode = MODES[mode_key]
    return mode


# Function to print the result of a fight
def print_fight_result(
    player_attack: str, enemy_attack: str, result_message: str
) -> None:
    print(
        f"You attacked with {player_attack}. Enemy attacked with {enemy_attack}. {result_message}"
    )


# Function to create an enemy
def create_enemy(level: int, difficulty_multiplier: int) -> Enemy:
    return Enemy(level, difficulty_multiplier)

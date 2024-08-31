from game.utils import (
    select_mode,
    show_menu,
    get_user_input,
    print_message,
    create_player,
)
from game.score import ScoreHandler
from game.game import Game
from settings import WELCOME_MESSAGE, GOODBYE_MESSAGE, INVALID_OPTION_MESSAGE


# Main function to run the game
def main():
    print_message(WELCOME_MESSAGE)
    score_handler = ScoreHandler()

    while True:
        show_menu()
        choice = get_user_input("Select an option: ")

        if choice == "1":
            play_game(score_handler)
        elif choice == "2":
            score_handler.display()
        elif choice == "3":
            print_message(GOODBYE_MESSAGE)
            break
        else:
            print_message(INVALID_OPTION_MESSAGE)


# Function to start the game
def play_game(score_handler):
    player = create_player()
    mode = select_mode()
    game = Game(player, mode, score_handler)
    game.play()


if __name__ == "__main__":
    main()

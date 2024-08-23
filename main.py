from game.utils import show_menu, get_user_input, print_message, create_player
from game.score import ScoreHandler
from game.game import Game
from settings import WELCOME_MESSAGE, GOODBYE_MESSAGE, INVALID_OPTION_MESSAGE


# Main function to run the game
def main():
    print_message(WELCOME_MESSAGE)  # Display the welcome message
    score_handler = ScoreHandler()  # Initialize the score handler

    while True:
        show_menu()  # Display the menu
        choice = get_user_input("Select an option: ")  # Get user input

        if choice == "1":
            play_game(score_handler)  # Start the game
        elif choice == "2":
            score_handler.display()  # Show the scores
        elif choice == "3":
            print_message(GOODBYE_MESSAGE)  # Display the goodbye message
            break  # Exit the loop
        else:
            print_message(INVALID_OPTION_MESSAGE)  # Show invalid option message


# Function to start the game
def play_game(score_handler):
    player, mode = create_player()  # Create a player and select a mode
    game = Game(player, mode, score_handler)  # Initialize the game
    game.play()  # Start playing the game


if __name__ == "__main__":
    main()  # Run the main function

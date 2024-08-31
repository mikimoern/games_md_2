# Modes settings
MODE_NORMAL = "Normal"
MODE_HARD = "Hard"
MODES = {"1": MODE_NORMAL, "2": MODE_HARD}

# Player settings
PLAYER_LIVES = 2

# Scores settings
POINTS_FOR_FIGHT = 1
POINTS_FOR_KILLING = 5
HARD_MODE_MULTIPLIER = 2

# Allowed attacks settings
PAPER = "Paper"
STONE = "Stone"
SCISSORS = "Scissors"
ALLOWED_ATTACKS = {"1": PAPER, "2": STONE, "3": SCISSORS}

# Fight result constants
WIN = 1
DRAW = 0
LOSE = -1

ATTACK_PAIRS_OUTCOME = {
    (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE,
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW,
}

# Score IO settings
SCORE_FILE = "scores.txt"
MAX_RECORDS_NUMBER = 5

# Text messages
WELCOME_MESSAGE = "Welcome to Rock, Paper, Scissors!"
INVALID_OPTION_MESSAGE = "Invalid option. Please choose 1, 2, or 3."
GOODBYE_MESSAGE = "Goodbye!"
INVALID_ATTACK_MESSAGE = "Invalid attack. Please select 1, 2, or 3."
INVALID_NAME_MESSAGE = "Name cannot be empty. Please enter a valid name."
INVALID_MODE_MESSAGE = "Invalid mode. Please select 1 or 2."

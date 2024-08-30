from settings import PLAYER_LIVES, ALLOWED_ATTACKS
from game.exceptions import GameOver, EnemyDown
from game.validation import is_valid_attack
import random


# Player class to represent a player in the game
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    # Method to select an attack from the user
    def select_attack(self) -> str:
        while True:
            attack = input("Choose your attack (1 - Paper, 2 - Stone, 3 - Scissors): ")
            if is_valid_attack(attack):
                return ALLOWED_ATTACKS[attack]
            else:
                print("Invalid attack. Please select 1, 2, or 3.")

    # Method to decrease the number of lives
    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives < 1:
            raise GameOver(f"Game Over! {self.name} is out of lives.")

    # Method to add points to the player's score
    def add_score(self, points: int) -> None:
        self.score += points

    # String representation of the player
    def __str__(self):
        return f"Player {self.name}: Lives = {self.lives}, Score = {self.score}"


# Enemy class to represent an enemy in the game
class Enemy:
    def __init__(self, level: int, difficulty_multiplier: int) -> None:
        self.level = level
        self.lives = level * difficulty_multiplier

    # Method to select a random attack
    def select_attack(self) -> str:
        return random.choice(list(ALLOWED_ATTACKS.values()))

    # Method to decrease the number of enemy lives
    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives < 1:
            raise EnemyDown("Enemy defeated!")

    # String representation of the enemy
    def __str__(self):
        return f"Enemy Level {self.level}: Lives = {self.lives}"

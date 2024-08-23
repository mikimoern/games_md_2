from game.utils import print_fight_result, create_enemy
from game.models import Player, Enemy
from game.exceptions import GameOver, EnemyDown
from settings import (
    ATTACK_PAIRS_OUTCOME,
    POINTS_FOR_FIGHT,
    POINTS_FOR_KILLING,
    HARD_MODE_MULTIPLIER,
    MODE_HARD,
    WIN,
    DRAW,
    LOSE,
)


# Game class to handle game logic
class Game:
    def __init__(self, player: Player, mode: str, score_handler) -> None:
        self.player = player
        self.mode = mode
        self.score_handler = score_handler
        self.enemy = create_enemy(1, self.get_difficulty())

    # Method to get the difficulty multiplier based on the game mode
    def get_difficulty(self) -> int:
        return HARD_MODE_MULTIPLIER if self.mode == MODE_HARD else 1

    # Method to create a new enemy with increased level
    def create_enemy(self) -> None:
        self.enemy = create_enemy(self.enemy.level + 1, self.get_difficulty())

    # Main method to play the game
    def play(self) -> None:
        while True:
            try:
                result = self.fight()  # Fight the enemy
                self.handle_fight_result(result)  # Handle the result of the fight
            except GameOver as e:
                print(e)  # Print game over message
                self.save_score()  # Save the player's score
                break
            except EnemyDown:
                print("You defeated the enemy!")  # Notify that the enemy is defeated
                self.player.add_score(
                    POINTS_FOR_KILLING
                )  # Add points for defeating the enemy
                self.create_enemy()  # Create a new enemy

    # Method to conduct a fight between the player and the enemy
    def fight(self) -> int:
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        result_message = (
            "You won this round!"
            if result == WIN
            else "It's a draw!" if result == DRAW else "You lost this round!"
        )
        print_fight_result(player_attack, enemy_attack, result_message)
        return result

    # Method to handle the result of the fight
    def handle_fight_result(self, result: int) -> None:
        if result == WIN:
            self.player.add_score(POINTS_FOR_FIGHT)
            try:
                self.enemy.decrease_lives()
            except EnemyDown:
                raise
        elif result == LOSE:
            self.player.decrease_lives()

    # Method to save the player's score using the score handler
    def save_score(self) -> None:
        self.score_handler.save(self.player.name, self.mode, self.player.score)

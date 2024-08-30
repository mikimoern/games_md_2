from game.utils import print_fight_result
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


class Game:
    def __init__(self, player: Player, mode: str, score_handler) -> None:
        self.player = player
        self.mode = mode
        self.score_handler = score_handler
        self.enemy = self.create_enemy()

    @property
    def difficulty(self) -> int:
        """Calculate difficulty based on the game mode."""
        return HARD_MODE_MULTIPLIER if self.mode == MODE_HARD else 1

    def create_enemy(self) -> Enemy:
        """Create a new enemy with the appropriate level and difficulty."""
        level = self.enemy.level + 1 if hasattr(self, "enemy") else 1
        return Enemy(level, self.difficulty)

    def play(self) -> None:
        """Main game loop where the player fights enemies."""
        while True:
            try:
                result = self.fight()
                self.handle_fight_result(result)
            except GameOver as e:
                print(e)
                self.save_score()
                break
            except EnemyDown:
                print("You defeated the enemy!")
                self.player.add_score(POINTS_FOR_KILLING)
                self.enemy = self.create_enemy()

    def fight(self) -> int:
        """Conduct a fight between the player and the enemy."""
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]

        if result == WIN:
            result_message = "You won this round!"
        elif result == DRAW:
            result_message = "It's a draw!"
        else:
            result_message = "You lost this round!"

        print_fight_result(player_attack, enemy_attack, result_message)
        return result

    def handle_fight_result(self, result: int) -> None:
        """Handle the result of a fight based on whether the player won, lost, or drew."""
        if result == WIN:
            self.player.add_score(POINTS_FOR_FIGHT)
            self.enemy.decrease_lives()
        elif result == LOSE:
            self.player.decrease_lives()

    def save_score(self) -> None:
        """Save the player's score using the score handler."""
        self.score_handler.save(self.player.name, self.mode, self.player.score)

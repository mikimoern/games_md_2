from settings import SCORE_FILE, MAX_RECORDS_NUMBER, MODES


# Class to store player records
class PlayerRecord:
    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name = name
        self.mode = mode if mode in MODES.values() else MODES[mode]  # Validate mode
        self.score = score

    # Comparison method to sort records by score
    def __gt__(self, other: "PlayerRecord") -> bool:
        return self.score > other.score

    # String representation of the player record
    def __str__(self) -> str:
        return f"{self.name} - {self.mode} - {self.score}"


# Class to manage a list of game records
class GameRecord:
    def __init__(self) -> None:
        self.records = []

    # Add a new record or update an existing one
    def add_record(self, player_record: PlayerRecord) -> None:
        existing_record = next(
            (
                record
                for record in self.records
                if record.name == player_record.name
                and record.mode == player_record.mode
            ),
            None,
        )
        if existing_record:
            if player_record > existing_record:
                self.records.remove(existing_record)
                self.records.append(player_record)
        else:
            self.records.append(player_record)
        self.prepare_records()

    # Prepare records: sort and limit to the maximum number of records
    def prepare_records(self) -> None:
        self.records = sorted(self.records, reverse=True)[:MAX_RECORDS_NUMBER]

    # Get the records formatted as a table
    def get_records_as_table(self) -> str:
        headers = ["Name", "Mode", "Score"]
        rows = [[record.name, record.mode, record.score] for record in self.records]
        table = (
            f"{headers[0]:<15} | {headers[1]:<10} | {headers[2]:<5}\n" + "-" * 35 + "\n"
        )
        for row in rows:
            table += f"{row[0]:<15} | {row[1]:<10} | {row[2]:<5}\n"
        return table


# Class to handle saving and loading scores
class ScoreHandler:
    def __init__(self) -> None:
        self.game_record = GameRecord()
        self.read_from_file()

    # Save a new score record
    def save(self, name: str, mode: str, score: int) -> None:
        player_record = PlayerRecord(name, mode, score)
        self.game_record.add_record(player_record)
        self.write_to_file()

    # Read score records from a file
    def read_from_file(self) -> None:
        try:
            with open(SCORE_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        name, mode, score = parts
                        player_record = PlayerRecord(name, mode, int(score))
                        self.game_record.add_record(player_record)
                    else:
                        print(f"Skipping invalid line: {line.strip()}")
        except FileNotFoundError:
            pass

    # Write the current score records to a file
    def write_to_file(self) -> None:
        with open(SCORE_FILE, "w") as f:
            for record in self.game_record.records:
                f.write(f"{record.name},{record.mode},{record.score}\n")

    # Display the scores
    def display(self) -> None:
        print(self.game_record.get_records_as_table())

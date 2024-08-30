from settings import SCORE_FILE, MAX_RECORDS_NUMBER, MODES


# Class to store player records
class PlayerRecord:
    def __init__(self, name: str, mode: str, score: int) -> None:
        if mode not in MODES.values():
            raise ValueError(f"Invalid mode: {mode}")
        self.name = name
        self.mode = mode
        self.score = score

    # Comparison method to sort records by score
    def __gt__(self, other: "PlayerRecord") -> bool:
        return self.score > other.score

    # String representation of the player record
    def __str__(self) -> str:
        return f"{self.name} - {self.mode} - {self.score}"

    # Method for comparing PlayerRecord instances based on name and mode
    def __eq__(self, other: "PlayerRecord") -> bool:
        return self.name == other.name and self.mode == other.mode


# Class to manage a list of game records
class GameRecord:
    def __init__(self) -> None:
        self.records = []

    # Add a new record or update an existing one
    def add_record(self, player_record: PlayerRecord) -> None:
        try:
            index = self.records.index(player_record)
            existing_record = self.records[index]
            if player_record > existing_record:
                self.records[index] = player_record
        except ValueError:
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

        # Create a list of valid record strings
        valid_records = [
            f"{record.name},{record.mode},{record.score}"
            for record in self.game_record.records
            if self.is_valid_record(record)
        ]

        # Join valid records as a single string with newline separation
        content = "\n".join(valid_records)

        # Write the content to the file
        with open(SCORE_FILE, "w") as f:
            f.write(content)

    # Method checks if the PlayerRecord instance has valid data
    def is_valid_record(self, record: PlayerRecord) -> bool:
        return (
            isinstance(record.name, str)
            and record.name.strip() != ""
            and record.mode in MODES.values()
            and isinstance(record.score, int)
            and record.score >= 0
        )

    # Display the scores
    def display(self) -> None:
        print(self.game_record.get_records_as_table())

from settings import ALLOWED_ATTACKS


def is_valid_attack(attack: str) -> bool:
    """
    Check if the provided attack is valid.

    Args:
        attack (str): The attack to validate.

    Returns:
        bool: True if the attack is valid, False otherwise.
    """
    return attack in ALLOWED_ATTACKS

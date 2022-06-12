""" This is docstring for the main module"""
# Docstring

class User:
    """This is a class for a user.

    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
        email (str): The email of the user.
    """

    def __init__(self, name: str, age: int, email: str):
        """Initialize the user.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.
            email (str): The email of the user.
        """
        self.name = name
        self.age = age
        self.email = email

def palindrome(sentence: str) -> bool:
    """Check if a sentence is a palindrome.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a palindrome, False otherwise.

    Examples:
        >>> palindrome("racecar")
        True
        >>> palindrome("arañara")
        True
        >>> palindrome("Hola mundo")
        False
        >>> sentence = "rotor"
        >>> palindrome(sentence)
        True
    """
    sentence = sentence.replace(" ", "").lower()
    return sentence == sentence[::-1]
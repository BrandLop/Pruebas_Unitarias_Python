# Docstring

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
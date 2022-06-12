# Docstring

def palindrome(sentence: str) -> bool:

    sentence = sentence.replace(" ", "").lower()
    return sentence == sentence[::-1]
#!/usr/bin/python3

def multiple_returns(sentence):
    """Return the length and the first character of a sentence."""
    # Use ternary operator to assign first_char
    first_char = sentence[0] if sentence else None
    return len(sentence), first_char

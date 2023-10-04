"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    string_items = [str(value) for value in items]
    for value in string_items:
        frequencies[value] = string_items.count(value)
    return frequencies
print(frequencies([100, 'hello', '100', '100', '100']))
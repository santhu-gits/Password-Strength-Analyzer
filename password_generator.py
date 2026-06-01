import random


import random


def generate_suggestion(password):

    replacements = {
        "a": "@",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "$"
    }

    result = ""

    for char in password:

        if char.lower() in replacements:
            result += replacements[char.lower()]
        else:
            result += char

    result += random.choice("!@#$%^&*")
    result += str(random.randint(1000, 9999))

    return result
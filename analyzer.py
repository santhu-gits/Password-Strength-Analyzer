import re
import math
def check_common_password(password):

    with open("common_passwords.txt", "r") as file:

        common_passwords = file.read().splitlines()

    return password.lower() in common_passwords
def calculate_entropy(password):

    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)
def analyze_password(password):

    score = 0

    report = []

    # Length Check
    if len(password) >= 12:
        score += 2
        report.append("✓ Length is strong (12+)")
    elif len(password) >= 8:
        score += 1
        report.append("✓ Length is acceptable")
    else:
        report.append("✗ Password too short")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
        report.append("✓ Uppercase present")
    else:
        report.append("✗ No uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
        report.append("✓ Lowercase present")
    else:
        report.append("✗ No lowercase letter")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
        report.append("✓ Number present")
    else:
        report.append("✗ No number")

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        score += 1
        report.append("✓ Special character present")
    else:
        report.append("✗ No special character")
    if check_common_password(password):
        report.append("✗ Common password detected")
    else:
        score += 1
        report.append("✓ Password is unique")
    return score, report


def classify_strength(score):

    if score <= 3:
        return "Weak"

    elif score <= 6:
        return "Medium"

    elif score <= 8:
        return "Strong"

    else:
        return "Very Strong"
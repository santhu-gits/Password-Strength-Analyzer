from analyzer import analyze_password
from analyzer import classify_strength
from password_generator import generate_suggestion
from analyzer import analyze_password
from analyzer import calculate_entropy
from hash_utils import hash_password
from database import create_database
from database import save_password
from database import password_exists
create_database()
username = input("Enter Username: ")
password = input("Enter Password: ")

score, report = analyze_password(password)

strength = classify_strength(score)
entropy = calculate_entropy(password)
hashed_password = hash_password(password)
already_used = password_exists(hashed_password)
print("\nPASSWORD REPORT")
print("-" * 40)

for item in report:
    print(item)

print("\n")
print("=" * 50)
print("PASSWORD SECURITY REPORT")
print("=" * 50)

for item in report:
    print(item)

print("\nScore:", score)
print("Strength:", strength)
print("Entropy:", entropy, "bits")

print("\nSHA-256 Hash:")
print(hashed_password)

print("=" * 50)
print(hashed_password)
if strength != "Strong":

    suggestion = generate_suggestion(password)

    print("\nSuggested Stronger Password:")
    print(suggestion)
if already_used:

    print("\nWARNING!")
    print("This password has been used before.")

else:

    save_password(username, hashed_password)

    print("\nPassword saved successfully.")
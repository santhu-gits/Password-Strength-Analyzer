import hashlib


def hash_password(password):

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    return hashed_password
print(hash_password("Hello123@"))
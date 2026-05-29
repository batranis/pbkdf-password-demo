from hashlib import pbkdf2_hmac
import secrets

# PBKDF2-HMAC-SHA512 password hashing demo

salt = secrets.token_bytes(16)

password = input("Password: ")

key = pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100_000)

print("Salt:", salt.hex())
print("Hash:", key.hex())

# simple login verification
attempt = input("Enter password again: ")

attempt_key = pbkdf2_hmac(
    "sha512",
    attempt.encode("utf-8"),
    salt,
    100_000
)

print("Match:", attempt_key == key)
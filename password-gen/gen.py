import random
import string

print("=== PASSWORD GENERATOR ===")

letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*"

try:
    length = int(input("How many characters? "))
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
except:
    print("Invalid input.")
    exit()

chars = letters + digits
if use_symbols:
    chars += symbols

password = ""
for i in range(length):
    password += random.choice(chars)

print(f"Generated password: {password}")

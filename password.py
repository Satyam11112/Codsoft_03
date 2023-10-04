import random
import string

# Function to generate a random password
def generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars):
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return "No characters selected for the password."

    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
print("Welcome to the Password Generator!")
length = int(input("Enter the length of the password: "))
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_digits = input("Include digits? (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

generated_password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)

print("Your generated password is:", generated_password)
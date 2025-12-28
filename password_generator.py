import random
import string
import hashlib

print("Password Generator")

length=int(input("Enter Password length(minimum 6):"))
if length<6:
    print("Password length must be atleast 6")
    exit()

use_upper = input("Include Uppercase Letter?(Y/N):").lower() == 'y'
use_lower = input("Include Lowercase Letter?(Y/N):").lower() == 'y'
use_digits = input("Include numbers?(Y/N):").lower() == 'y'
use_special = input("Include Special Character?(Y/N):").lower() == 'y'

characters=""

if use_upper:
    characters+=string.ascii_uppercase
if use_lower:
    characters+=string.ascii_lowercase
if use_digits:
    characters+=string.digits
if use_special:
    characters+=string.punctuation

if characters == "":
    print("You must select atleast one character type!")
    exit()

password =""
for _ in range(length):
    password+=random.choice(characters)

print("\nGenerated Password:",password)

encrypted_password = hashlib.sha256(password.encode()).hexdigest()

with open("password.txt","a") as file:
    file.write(encrypted_password+ "\n")
print("Encrypted password saved successfully.")
import re

name = input("Enter your name: ")

age = input("Enter your age: ")
if not age.isdigit():
    print("Invalid age format. Please enter a number.")
    exit()
age = int(age)

email = input("Enter your email: ")
def is_valid_email(email):
    return email.endswith("@gmail.com")
if not is_valid_email(email):
    print("Invalid email format. Please enter a valid email (e.g., user@example.com).")
    exit()

phone = input("Enter your phone number: ")
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10
if not is_valid_phone(phone):
    print("Invalid phone number. It must contain exactly 10 digits.")
    exit()

# display profile
print("\n--- Personal Profile ---")
print(f"Name   : {name}")
print(f"Age    : {age} years")
print(f"Email  : {email}")
print(f"Phone  : {phone}")

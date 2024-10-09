# Welcome message
print("Welcome to the bank! Please log in.")

# Get user input
username = input("Username: ").lower()
password = input("Password (0-6 characters): ")
while len(password) < 0 or len(password) > 6:
    password = input("Invalid password. Please enter a valid password (0-6 characters): ")

# Get first and last name
first_name = input("First Name: ").capitalize()
while not first_name.isalpha():
    first_name = input("Invalid first name. Please enter only letters: ")
last_name = input("Last Name: ").capitalize()
while not last_name.isalpha():
    last_name = input("Invalid last name. Please enter only letters: ")

# Get birthday
birthday = input("Birthdate (yyyy/mm/dd): ")
while not ("1980" <= birthday[:4] <= "2007") or not birthday[4:6].isdigit() or not birthday[6:8].isdigit():
    birthday = input("Invalid birthdate. Please enter a valid date (yyyy/mm/dd): ")

# Get digits
digits = input("Enter your digits (12 characters): ")
while not digits.isdigit() or len(digits)!= 12:
    digits = input("Invalid digits. Please enter 12 digits: ")

# Print user information
print(f"Mr. {first_name} {last_name}, your username is: [{username}] and passcode is: [{password}]")

# Ask if user wants to order a card
card_order = input("Do you want to order a card? (Y/N): ")
if card_order.upper() == "Y":
    print("Your order has been filed!")
    print("Processing...")
    print("Your card is ready!")
    print("-----------------------------------------------")
    print(f"Your card is: {digits[:4]}-{digits[4:8]}-{digits[8:12]}, Mr. {first_name} {last_name}, born {birthday[0:4]}-{birthday[4:6]}-{birthday[6:8]}")
else:
    print("No order.")
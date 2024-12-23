import os
import random
import string
import json

# Encryption and Decryption functions
def encrypt_password(password):
    chars = list(string.punctuation + string.digits + string.ascii_letters)
    key = chars.copy()
    random.shuffle(key)
    encryption_map = {chars[i]: key[i] for i in range(len(chars))}
    encrypted_password = ''.join([encryption_map[char] for char in password])
    return encrypted_password, encryption_map

def decrypt_password(encrypted_password, encryption_map):
    decryption_map = {v: k for k, v in encryption_map.items()}
    decrypted_password = ''.join([decryption_map[char] for char in encrypted_password])
    return decrypted_password

# File operations
def save_account_info(accounts):
    with open("accounts.txt", "w") as f:
        json.dump(accounts, f)  # Store the entire accounts dictionary as JSON

def load_account_info():
    if not os.path.exists("accounts.txt"):
        return {}
    
    with open("accounts.txt", "r") as f:
        accounts = json.load(f)  # Load the JSON data back into the accounts dictionary
    return accounts

# BankAccount class
class BankAccount:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def show_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

def create_account(accounts):
    username = input("Enter a new username: ")
    if username in accounts:
        print("Username already exists!")
        return
    
    password = input("Enter a password: ")
    encrypted_password, encryption_map = encrypt_password(password)
    
    account = BankAccount(username)
    accounts[username] = {"password": encrypted_password, "encryption_map": encryption_map, "balance": account.balance}
    save_account_info(accounts)
    print(f"Account created successfully for {username}!")

def login(accounts):
    username = input("Enter your username: ")
    if username not in accounts:
        print("Account does not exist.")
        return None
    
    password = input("Enter your password: ")
    encrypted_password = accounts[username]["password"]
    encryption_map = accounts[username]["encryption_map"]
    
    if decrypt_password(encrypted_password, encryption_map) == password:
        print("Login successful!")
        return BankAccount(username, accounts[username]["balance"])
    else:
        print("Incorrect password.")
        return None

def delete_account(accounts):
    username = input("Enter your username to delete: ")
    if username not in accounts:
        print("Account does not exist.")
        return
    
    password = input("Enter your password: ")
    encrypted_password = accounts[username]["password"]
    encryption_map = accounts[username]["encryption_map"]
    
    if decrypt_password(encrypted_password, encryption_map) == password:
        del accounts[username]
        save_account_info(accounts)
        print("Account deleted successfully.")
    else:
        print("Incorrect password.")

def edit_account(accounts, account):
    print("\n1. Change Username")
    print("2. Change Password")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        new_username = input("Enter a new username: ")
        if new_username in accounts:
            print("Username already exists!")
        else:
            accounts[new_username] = accounts.pop(account.username)
            account.username = new_username
            print("Username updated successfully.")
            save_account_info(accounts)
    
    elif choice == "2":
        current_password = input("Enter current password: ")
        if decrypt_password(accounts[account.username]["password"], accounts[account.username]["encryption_map"]) == current_password:
            new_password = input("Enter new password: ")
            encrypted_password, encryption_map = encrypt_password(new_password)
            accounts[account.username]["password"] = encrypted_password
            accounts[account.username]["encryption_map"] = encryption_map
            print("Password updated successfully.")
            save_account_info(accounts)
        else:
            print("Incorrect current password.")
    else:
        print("Invalid option.")

def main():
    accounts = load_account_info()
    
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Delete Account")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            account = login(accounts)
            if account:
                while True:
                    print("\n1. Show Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Edit Account")
                    print("5. Logout")
                    
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        account.show_balance()
                    elif user_choice == "2":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        accounts[account.username]["balance"] = account.balance
                        save_account_info(accounts)
                    elif user_choice == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        accounts[account.username]["balance"] = account.balance
                        save_account_info(accounts)
                    elif user_choice == "4":
                        edit_account(accounts, account)
                    elif user_choice == "5":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            delete_account(accounts)
        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()

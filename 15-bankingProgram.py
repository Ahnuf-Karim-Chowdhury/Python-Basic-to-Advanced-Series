class BankAccount:
    def __init__(self):
        self.balance = 0

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

def main():
    account = BankAccount()

    while True:
        print("\nBanking System Menu:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            account.show_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()

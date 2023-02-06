class ATM:
    def __init__(self, balance=0, user_name=None):
        self.balance = balance
        self.user_name = user_name
    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. Current balance: {self.balance}"

atm = ATM(user_name = input("Enter your name : "))
while True:
    print("Welcome to ATM machine")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        balance = atm.check_balance()
        print(f"{atm.user_name}, your current balance is {balance}")
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        print(atm.deposit(amount))
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        print(atm.withdraw(amount))
    elif choice == 4:
        print(f"Thank you {atm.user_name} for using our ATM machine!")
        break
    elif choice == 5:
        print(f"{atm.user_name} successfully logged out!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

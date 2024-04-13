from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter your full name: ")
        self.phone_number = int(input("Enter your phone number: "))
        self.balance = 0

    def show_info(self):
        print(f"\nAccount Number: {self.account}")
        print(f"Full Name: {self.full_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Current Balance: {self.balance}\n")

    def show_balance(self) -> None:
        print(f"\nCurrent Balance: {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("\nEnter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")

    def deposit(self) -> None:
        amount = int(input("\nEnter amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")


banks = []


def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("\nWelcome to the Bank Management System")
    print("1. Create Account")
    print("2. Show All Bank Account Details")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj = Bank()
            banks.append(obj)
            print("Account created successfully.")

        elif choice == 2:
            if len(banks) == 0:
                print("No accounts have been created yet.")
            else:
                for account in banks:
                    account.show_info()

        elif choice == 3:
            if len(banks) == 0:
                print("No accounts have been created yet.")
            else:
                acc_no = int(input("Enter account number to deposit: "))
                for obj in banks:
                    if obj.account == acc_no:
                        obj.deposit()
                        break
                else:
                    print("Account not found.")

        elif choice == 4:
            if len(banks) == 0:
                print("No accounts have been created yet.")
            else:
                acc_no = int(input("Enter account number to withdraw: "))
                for obj in banks:
                    if obj.account == acc_no:
                        obj.withdraw()
                        break
                else:
                    print("Account not found.")

        elif choice == 5:
            print("Thank you for using the Bank Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    except ValueError:
        print("Invalid input. Please enter a number.")

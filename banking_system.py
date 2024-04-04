from random import randint


# Bank class to manage bank account operations
class Bank:
    # Constructor to initialize bank account details
    def __init__(self) -> None:
        self.account = randint(100000, 999999)  # Generate a random account number
        self.full_name = input("Enter name = ")  # Ask for user's full name
        self.phone_number = int(
            input("Enter phone number = ")
        )  # Ask for user's phone number
        self.balance = 0  # Initialize balance to zero

    # Method to display account information
    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Full name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    # Method to display current balance
    def show_balance(self) -> None:
        print(f"Current balance = {self.balance}")

    # Method to withdraw money from the account
    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))  # Ask for withdrawal amount
        if amount > self.balance:
            print("Insufficient balance")  # Display message if balance is insufficient
        else:
            self.balance -= amount  # Deduct the withdrawal amount from balance

    # Method to deposit money into the account
    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))  # Ask for deposit amount
        self.balance += amount  # Add the deposit amount to balance


banks = []  # List to store bank objects


# Function to check if an account with a given account number exists
def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


# Main program loop
while True:
    print("1. Create account")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Exit")
    choice = int(input("Enter choice = "))  # Ask for user's choice

    # Create a new bank account
    if choice == 1:
        obj = Bank()  # Create a new Bank object
        banks.append(obj)  # Add the object to the banks list

    # Show all bank account details
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()

    # Deposit money into an account
    elif choice == 3:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break

    # Withdraw money from an account
    elif choice == 4:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to withdraw = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break

    # Transfer money between accounts
    elif choice == 5:
        from_acc_no = int(
            input("Enter account number from which you want to transfer = ")
        )
        to_acc_no = int(input("Enter account number to which you want to transfer = "))
        from_acc_obj = check_account_exists(
            from_acc_no
        )  # Check if sender's account exists
        to_acc_obj = check_account_exists(
            to_acc_no
        )  # Check if receiver's account exists
        if from_acc_obj is not None and to_acc_obj is not None:
            transfer_amount = int(
                input("Enter transfer amount = ")
            )  # Ask for transfer amount
            if from_acc_obj.balance < transfer_amount:
                print(
                    "Insufficient balance"
                )  # Display message if sender's balance is insufficient
            else:
                from_acc_obj.balance -= (
                    transfer_amount  # Deduct transfer amount from sender's balance
                )
                to_acc_obj.balance += (
                    transfer_amount  # Add transfer amount to receiver's balance
                )
        else:
            print(
                "Account does not exist"
            )  # Display message if one or both accounts don't exist

    # Exit the program
    elif choice == 6:
        break

    # Invalid choice
    else:
        print("Invalid Choice")

from OOP.bankaccount.bank import Bank
from OOP.exceptions.insufficient_funds_exception import InsufficientFundsException
from OOP.exceptions.invalid_amount_exception import InvalidAmountException
from OOP.exceptions.invalid_pin_exception import InvalidPinException

myBank = Bank("TIMI Bank")


def gotoMainMenu():
    while True:
        print("Welcome to TIMI Bank!")
        print("1. Create Account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Close Account")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            createAccount()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            deposit()
        elif choice == '4':
            transfer()
        elif choice == '5':
            checkBalance()
        elif choice == '6':
            closeAccount()
        elif choice == '7':
            exitApp()
            break
        else:
            print("Invalid option! Please try again.")


def createAccount():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    pin = input("Enter PIN: ")

    account = myBank.register_customer(firstName, lastName, pin)
    print("Account created successfully!")
    print("Your account number is", account.get_number())


def withdraw():
    accountNumber = int(input("Enter account number: "))
    pin = input("Enter PIN: ")
    amount = int(input("Enter amount to withdraw: "))

    try:
        myBank.withdraw(accountNumber, amount, pin)
        print("Withdrawal successful!")
    except (InvalidAmountException, InvalidPinException, InsufficientFundsException) as e:
        print("Withdrawal failed:", e)


def deposit():
    accountNumber = int(input("Enter account number: "))
    pin = input("Enter PIN: ")
    amount = int(input("Enter amount to deposit: "))

    try:
        myBank.deposit(amount, accountNumber)
        print("Deposit successful!")
    except (InvalidAmountException, InvalidPinException) as e:
        print("Deposit failed:", e)


def transfer():
    senderAccountNumber = int(input("Enter sender account number: "))
    senderPin = input("Enter sender PIN: ")
    receiverAccountNumber = int(input("Enter receiver account number: "))
    amount = int(input("Enter amount to transfer: "))

    try:
        myBank.transfer(amount, receiverAccountNumber, senderAccountNumber, senderPin)
        print("Transfer successful!")
    except (InvalidAmountException, InvalidPinException, InsufficientFundsException) as e:
        print("Transfer failed:", e)


def checkBalance():
    accountNumber = int(input("Enter account number: "))
    pin = input("Enter PIN: ")

    try:
        balance = myBank.check_balance(pin, accountNumber)
        print("Current balance:", balance)
    except InvalidPinException as e:
        print("Failed to check balance:", e)


def closeAccount():
    accountNumber = int(input("Enter account number: "))
    pin = input("Enter PIN: ")

    try:
        myBank.remove_account(accountNumber, pin)
        print("Account closed successfully!")
    except InvalidPinException as e:
        print("Failed to close account:", e)


def exitApp():
    print("Exiting TIMI Bank. Goodbye!")
    exit()


if __name__ == "__main__":
    gotoMainMenu()

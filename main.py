database = []

def addTransaction(amount, description, date):
    transaction = {
        "amount": amount,
        "description": description,
        "date": date
    }
    database.append(transaction)
    print("Transaction added successfully.")
    

def viewTransactions():
    print("Viewing all transactions...")
    for transaction in database:
        print(f"Amount: {transaction['amount']}, Description: {transaction['description']}, Date: {transaction['date']}")

def openMenu(option):
    match option:
        case "addTransaction":
            print("Adding a new transaction...")
            amount = float(input("Enter transaction amount:\n"))
            description = input("Enter transaction description:\n")
            date = input("Enter transaction date (DD/MM/YYYY):\n")
            addTransaction(amount, description, date)
        case "viewTransactions":
            viewTransactions()
        case "exit":
            exit()


def prompt():
    option = input("Enter an option:\n1. Add a transaction\n2. View all transactions\n3. Exit the program\n")

    match option:
        case "1":
            openMenu("addTransaction")
            prompt()
        case "2":
            openMenu("viewTransactions")
            prompt()
        case "3":
            openMenu("exit")

prompt()
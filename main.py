# Using a list to store transactions temporarily before adding file storage
database = [] 

def add_Transaction(amount: float, description: str, date: str):
    transaction = {
        "amount": amount,
        "description": description,
        "date": date
    }
    database.append(transaction)
    print("Transaction added successfully.")
    
def view_Transactions():
    print("Viewing all transactions...")
    for transaction in database:
        print(f"Amount: {transaction['amount']}, Description: {transaction['description']}, Date: {transaction['date']}")
        print("-----------------------------")
    total = sum(transaction['amount'] for transaction in database) # Calculating the total amount of all transactions
    print(f"Total: {total}")

def open_Menu(option): 
    match option:
        case "addTransaction":
            print("Adding a new transaction...")
            amount = float(input("Enter transaction amount:\n"))
            description = input("Enter transaction description:\n")
            date = input("Enter transaction date (DD/MM/YYYY):\n")
            add_Transaction(amount, description, date)
        case "viewTransactions":
            view_Transactions()
        case "exit":
            exit()


def prompt(): # Repeatedly prompts the user for an option until they choose to exit
    option = input("Enter an option:\n1. Add a transaction\n2. View all transactions\n3. Exit the program\n")

    match option:
        case "1":
            open_Menu("add_Transaction")
            prompt()
        case "2":
            open_Menu("viewTransactions")
            prompt()
        case "3":
            open_Menu("exit")

prompt()
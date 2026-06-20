import json

dataFile = "data.json"

def returnToMenu():
    userChoice = input("Returning to the main menu... Press Enter to continue.")
    if userChoice == "":
        prompt()

def loadData():
    try:
        with open(dataFile, "r") as file:
            content = file.read()
            if content == "":
                return {"income": None, "transactions": []}
            data = json.loads(content)
            return {"income": data.get("income"), "transactions": data.get("transactions", [])}
    except FileNotFoundError:
        return {"income": None, "transactions": []}

def saveData():
    json.dump({"income": income, "transactions": transactionsList}, open(dataFile, "w"), indent=4)

def addTransaction(amount: float, description: str, date: str, category: str = "General"):
    transaction = {
        "amount": amount,
        "description": description,
        "date": date,
        "category": category
    }
    transactionsList.append(transaction)
    saveData()
    print("Transaction added successfully.")
    returnToMenu()

def viewTransactions():
    print("Viewing all transactions...")
    if transactionsList == []:
        print("No transactions yet.")
        returnToMenu()
        return

    for transaction in transactionsList:
        print(f"Amount: {transaction['amount']}, Description: {transaction['description']}, Date: {transaction['date']}, Category: {transaction['category']}")

    returnToMenu()

def viewSummary():
    print("Calculating summary...")
    totalIncome = sum(transaction['amount'] for transaction in transactionsList if transaction['amount'] > 0)
    totalSpent = sum(-transaction['amount'] for transaction in transactionsList if transaction['amount'] < 0)  # Expenses are stored as negative amounts
    print(f"Total income logged: {totalIncome}")
    print(f"Total spent: {totalSpent}")
    print(f"Remaining income: {income + totalIncome - totalSpent}")
    returnToMenu()

def changeIncome():
    global income
    newIncome = float(input("Enter your new income for the month:\n"))
    income = newIncome
    saveData()
    print("Income updated successfully.")
    returnToMenu()

def openMenu(option):
    match option:
        case "addTransaction":
            print("Adding a new transaction...")
            entryType = input("Is this income or an expense? (i/e)\n")
            if entryType != "i" and entryType != "e":
                print("Invalid entry type. Please enter 'i' or 'e'.")
                returnToMenu()
                return

            amount = float(input("Enter transaction amount:\n"))
            if amount < 0:
                print("Invalid transaction amount. Please enter a positive value.")
                returnToMenu()
                return

            if entryType == "e":
                amount = -amount  # Storing expenses as negative so totals are just a sum

            description = input("Enter transaction description:\n")
            date = input("Enter transaction date (DD/MM/YYYY):\n")
            category = input("Enter transaction category (optional, press enter to skip):\n")
            if category == "":
                category = "General"
            addTransaction(amount, description, date, category)
        case "viewTransactions":
            viewTransactions()
        case "viewSummary":
            viewSummary()
        case "changeIncome":
            changeIncome()
        case "exit":
            exit()

def prompt():  # Prompt user for input and call the appropriate function based on their choice
    option = input("Enter an option:\n1. Add a transaction\n2. View all transactions\n3. View summary\n4. Change income\n5. Exit the program\n")
    match option:
        case "1":
            openMenu("addTransaction")
        case "2":
            openMenu("viewTransactions")
        case "3":
            openMenu("viewSummary")
        case "4":
            openMenu("changeIncome")
        case "5":
            openMenu("exit")
        case _:
            print("Invalid option, please try again.")
            prompt()

data = loadData()
transactionsList = data["transactions"]
income = data["income"]

if income is None:
    income = 0.0
    saveData()

prompt()
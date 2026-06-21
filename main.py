import json
import matplotlib.pyplot as plt


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

def visualiseTransactions():
    if not transactionsList:
        print("No transactions to visualize.")
        returnToMenu()
        return
 
    categories = {}
    for transaction in transactionsList:
        if transaction['amount'] >= 0:
            continue  # Skip income entries, pie chart is for spending breakdown only
        category = transaction['category']
        amount = -transaction['amount']  # Flip back to positive for chart sizing
        categories[category] = categories.get(category, 0) + amount
 
    if not categories:
        print("No expenses to visualize.")
        returnToMenu()
        return
 
    labels = list(categories.keys())
    sizes = list(categories.values())
 
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Spending Distribution by Category')
    plt.show()
    returnToMenu()

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

def removeTransaction(index: int):
    if 0 <= index < len(transactionsList):
        transactionsList.pop(index)
        saveData()
        print("Transaction removed successfully.")
    else:
        print("Invalid transaction index.")
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
        case "visualiseTransactions":
            visualiseTransactions()
        case "changeIncome":
            changeIncome()
        case "exit":
            exit()

def prompt():  # Prompt user for input and call the appropriate function based on their choice
    option = input("Enter an option:\n1. Add a transaction\n2. Remove a transaction\n3. View all transactions\n4. View summary\n5. Visualise spending\n6. Change income\n7. Exit the program\n")
    match option:
        case "1":
            openMenu("addTransaction")
        case "2":
            openMenu("removeTransaction")
        case "3":
            openMenu("viewTransactions")
        case "4":
            openMenu("viewSummary")
        case "5":
            openMenu("visualiseTransactions")
        case "6":
            openMenu("changeIncome")
        case "7":
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
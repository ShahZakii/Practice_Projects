# ====================================
# Project : Expense Tracker
# Author  : MOHD ZAKI SHAH SAIFI
# Language: Python
# ====================================


# Function to add new expense
def add_expense():
    print("-" * 40)
    date = input("Enter Date (DD/MM/YYYY): ")
    category = input("Enter Expense Category: ").title()
    add_info = input("Enter Additional Information: ").upper()
    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please enter a valid number: ")

    expense = {
        "date": date,
        "category": category,
        "add_info": add_info,
        "amount": amount
    }

    expense_list.append(expense)

    print("Expense Added Successfully: ")

# Function to display all saved expenses
def view_expenses():
    if (len(expense_list) == 0):
            print("No Expense Added.")
    else:
        count = 1
        for expense in expense_list:
            print("-" * 40)
            print(f"Expense   : {count}")
            print(f"Dated     : {expense["date"]}")
            print(f"Category  : {expense["category"]}")
            print(f"Add_Info  : {expense["add_info"]}")
            print(f"Amount    : {expense["amount"]}")
            count += 1

# Function to calculate total expenses 
def total_expenses():
    print("=" * 40)
    amount = 0
    for money in expense_list:
        amount += money["amount"]
        
    print(f"Total Expenses: ${amount}")

# Function to delete an expense
def delete_expense():
    print("-" * 40)
    if len(expense_list) == 0:
        print("No expense to delete")
        return
    
    delete = int(input("Enter expense number: "))
    try:
        if 1 <= delete <= len(expense_list):
            del expense_list[delete - 1]
            print("Expense deleted successfully.")
        
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")
    

# list of expenses in form of dictionary.
expense_list = [] 

print("Welcome to Expense Tracker: ")

print() # Print for space between lines.

# Main program starts from here
while True:
    print("======MENU======")
    print() # for space

    print("1. Add Expenses: \n2. View All Expenses: \n3. Total All Expenses: \n4. Delete Expense: \n5.Exit: ")

    print("-" * 40)
    choice = int(input("Enter Your Choice: "))

    if(choice == 1):
        add_expense()

    elif(choice == 2):
        view_expenses()

    elif(choice == 3):
        total_expenses()

    elif(choice == 4):
        delete_expense()
    
    elif(choice == 5):
        break
    else:
        print("Invalid Input.")

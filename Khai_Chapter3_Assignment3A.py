#In this assignment, the program is designed to analyze the user's monthly expenses. Once the expenses are recorded, the program will then display the highest and lowest expense, as well as the total amount.



#Create function for entering expense type and dollar amount
from functools import reduce

def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    return expenses

#Add invalidation for incorrect user input
def analyze_expenses(expenses):
    if not expenses:
        print("No expenses highlighted.")
        return


#Add formula for gathering the highest and lowest expenses
    amounts = [amount for _, amount in expenses]

    total_expense = reduce(lambda x, y: x + y, amounts)
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

#Produce the final result of input data
    print(f"\nTotal Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

def main():
    expenses = get_expenses()
    analyze_expenses(expenses)

if __name__ == "__main__":
    main()

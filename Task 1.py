import json
from datetime import datetime

FILE_NAME = "expenses.json"


# Load expenses from the JSON file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Expense file contains invalid data.")
        return []


# Save expenses to the JSON file
def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except IOError:
        print("Error: Unable to save expense data.")


# Get a valid positive amount
def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


# Get a valid date
def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")


# Add a new expense
def add_expense(expenses):
    print("\n--- Add Expense ---")

    amount = get_amount()

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()

    while not description:
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    date = get_date()

    expense_id = 1

    if expenses:
        expense_id = max(expense["id"] for expense in expenses) + 1

    expense = {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


# Display all expenses
def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 75)
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<15}{'Description'}")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['description']}"
        )

    print("-" * 75)


# Search expenses by category
def search_by_category(expenses):
    print("\n--- Search by Category ---")

    category = input("Enter category: ").strip().lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"ID: {expense['id']} | "
                f"Date: {expense['date']} | "
                f"Category: {expense['category']} | "
                f"Amount: ₹{expense['amount']:.2f} | "
                f"Description: {expense['description']}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")


# Calculate total expenses
def total_expenses(expenses):
    print("\n--- Total Expenses ---")

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total amount spent: ₹{total:.2f}")


# Delete an expense
def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses available to delete.")
        return

    try:
        expense_id = int(input("Enter expense ID to delete: "))

        for expense in expenses:
            if expense["id"] == expense_id:
                expenses.remove(expense)
                save_expenses(expenses)
                print("Expense deleted successfully.")
                return

        print("Expense ID not found.")

    except ValueError:
        print("Invalid ID. Please enter a number.")


# Display the main menu
def show_menu():
    print("\n")
    print("=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. View Total Expenses")
    print("5. Delete Expense")
    print("6. Exit")
    print("=" * 40)


# Main program
def main():
    expenses = load_expenses()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense(expenses)

            elif choice == 2:
                view_expenses(expenses)

            elif choice == 3:
                search_by_category(expenses)

            elif choice == 4:
                total_expenses(expenses)

            elif choice == 5:
                delete_expense(expenses)

            elif choice == 6:
                print("\nThank you for using the Expense Tracker.")
                break

            else:
                print("Invalid choice. Please select 1 to 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
if __name__ == "__main__":
    main()

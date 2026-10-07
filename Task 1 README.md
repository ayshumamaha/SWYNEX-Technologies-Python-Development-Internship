# Expense Tracker

A simple command-line Expense Tracker developed using Python. The application allows users to record, view, search, calculate, and delete expenses while storing the data persistently in a JSON file.

## Project Overview

The Expense Tracker is a menu-driven Python CLI application designed to demonstrate fundamental Python programming concepts through a practical real-world application.

Users can add expenses by providing the amount, category, description, and date. The application stores the expense records in a JSON file, allowing the data to remain available even after the program is closed.

The project also includes input validation and exception handling to ensure that invalid inputs are handled properly without causing the application to crash.

## Features

* Add new expenses
* View all recorded expenses
* Search expenses by category
* Calculate total expenses
* Delete an expense using its ID
* Persistent storage using JSON
* Input validation
* Exception handling
* Menu-driven command-line interface
* Automatic creation of the expense data file

## Technologies Used

* **Python 3**
* **JSON** – for persistent data storage
* **datetime** – for date validation
* **Command Prompt / Terminal** – for running the application
* **Git & GitHub** – for version control and project hosting

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.json
└── README.md
```

### `main.py`

Contains the complete Python application, including:

* Main menu
* Expense management functions
* Input validation
* Exception handling
* JSON file handling
* Expense calculations

### `expenses.json`

Stores the expense records created by the user. This file is automatically created when the application saves the first expense.

### `README.md`

Contains project information, features, setup instructions, usage instructions, and documentation.

## Requirements

Make sure Python 3 is installed on your system.

You can check the installed Python version using:

```bash
python --version
```

## Installation

1. Clone the repository:

```bash
git clone <your-github-repository-url>
```

2. Open the project folder:

```bash
cd Expense-Tracker
```

3. Run the application:

```bash
python main.py
```

No external Python libraries are required because the application uses only built-in Python modules.

## How to Use

After running the program, the main menu will be displayed:

```text
========================================
          EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. View Total Expenses
5. Delete Expense
6. Exit
========================================
```

### 1. Add Expense

Select option `1` and enter:

* Expense amount
* Category
* Description
* Date

Example:

```text
Enter amount: 500
Enter category: Food
Enter description: Lunch
Enter date (YYYY-MM-DD): 2026-10-07

Expense added successfully.
```

### 2. View Expenses

Select option `2` to display all stored expenses.

Example:

```text
ID   Date           Category       Amount         Description
1    2026-10-07     Food            ₹500.00       Lunch
2    2026-10-06     Travel          ₹250.00       Bus ticket
```

### 3. Search by Category

Select option `3` and enter a category to view matching expenses.

Example:

```text
Enter category: Food
```

The application displays all expenses recorded under that category.

### 4. View Total Expenses

Select option `4` to calculate the total amount spent.

Example:

```text
Total amount spent: ₹750.00
```

### 5. Delete Expense

Select option `5` and enter the ID of the expense that should be deleted.

Example:

```text
Enter expense ID to delete: 2

Expense deleted successfully.
```

### 6. Exit

Select option `6` to close the application.

```text
Thank you for using the Expense Tracker.
```

## Input Validation

The application validates user input before processing it.

It prevents:

* Negative expense amounts
* Zero-value expenses
* Non-numeric amounts
* Empty categories
* Empty descriptions
* Invalid dates
* Invalid menu selections
* Invalid expense IDs

For example:

```text
Enter amount: -500

Amount must be greater than zero.
```

## Exception Handling

Exception handling is implemented to prevent common errors from terminating the program.

The application handles situations such as:

* Invalid numerical input
* Invalid date format
* Missing JSON file
* Invalid JSON data
* File read/write errors
* Invalid expense IDs

This improves the reliability and usability of the application.

## Data Persistence

Expense information is stored in `expenses.json`.

Example:

```json
[
    {
        "id": 1,
        "amount": 500.0,
        "category": "Food",
        "description": "Lunch",
        "date": "2026-10-07"
    }
]
```

Because the data is stored in a file, previously recorded expenses remain available when the application is started again.

## Concepts Demonstrated

This project demonstrates the following Python concepts:

* Variables and data types
* Functions
* Conditional statements
* Loops
* Lists and dictionaries
* JSON file handling
* Input validation
* Exception handling
* Date validation
* Menu-driven programming
* Persistent data storage

## Future Enhancements

Possible improvements for future versions include:

* Monthly and weekly expense reports
* Budget tracking
* Income tracking
* Expense statistics
* Expense filtering by date
* Sorting expenses
* CSV or Excel export
* Graphical user interface
* SQLite database integration
* User authentication
* Data visualization

## Project Purpose

This project was developed as part of a Python Developer Internship task to demonstrate the practical application of Python programming concepts in a simple command-line application.

## Author

**M. Ayshwarya**

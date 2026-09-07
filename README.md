# Expense Tracker

A simple command-line Expense Tracker built using Python.

This project was created to practice and strengthen core Python concepts such as dictionaries, functions, loops, modules, exception handling, and input validation.

---

## Features

### V1 Features

- Add expenses
- View all expenses
- Calculate total expenses
- Calculate spending by category
- Search expenses
- Delete expenses
- Exit the application

### V2 Features

- Menu input validation
- Amount validation
- Prevents zero and negative amounts
- Empty input validation
- Date format validation
- `y/n` validation when adding multiple expenses
- Expense ID validation
- Handles non-existent expense IDs
- Exception handling using `try/except`
- Handles invalid user inputs without crashing the program

---

## Expense Structure

Each expense contains:

- Amount
- Category
- Date
- Description

Example:

```python
{
    "Amount": 500,
    "Category": "Food",
    "Date": "2026-09-07",
    "Description": "Lunch"
}

Each expense is assigned a unique ID.

Menu
==============EXPENSE TRACKER==============

-----1.Add Expense -----
-----2.View Expense -----
-----3.Total Expense -----
-----4.Spending by Category ----
-----5.Search Expense -----
-----6.Delete Expense -----
-----7.Exit ----
Validation and Error Handling

The application validates user input before accepting it.

Menu Validation

The user must enter a number between 1 and 7.

Invalid inputs such as:

abc
0
8

are rejected.

Amount Validation

The amount:

Must be a number
Must be greater than zero

Examples:

abc   → Invalid
0     → Invalid
-500  → Invalid
500   → Valid
Empty Input Validation

Category, date, and description cannot be empty or contain only whitespace.

Date Validation

Dates must follow the format:

YYYY-MM-DD

Example:

2026-09-07

Invalid dates such as:

07-09-2026
2026/09/07
2026-02-30

are rejected.

y/n Validation

When adding multiple expenses, the user must enter either:

y

or

n

Invalid inputs are rejected until a valid option is entered.

Delete ID Validation

The application checks:

Whether the ID is a number
Whether the ID exists

Invalid or non-existent IDs are handled without crashing the program.

Python Concepts Used

This project helped me practice:

Variables
Data types
Input and output
Conditional statements
for and while loops
Lists
Dictionaries
Functions
String methods
Modules
datetime
Exception handling
try
except
else
raise
Dictionary methods
User input validation
Technologies
Python
Command Line / Terminal
Git
GitHub
Project Structure
python_projects_2026/
│
├── expenses.py
└── README.md
Version History
V1

Implemented the basic Expense Tracker functionality.

V2

Added input validation and exception handling to make the application more reliable and prevent crashes caused by invalid user input.

Future Improvements

Possible improvements for future versions:

Store expenses in a JSON file
Load expenses when the program starts
Save expenses when the program exits
Add expense editing
Add date-based searching
Add monthly expense summaries
Improve the command-line interface
```

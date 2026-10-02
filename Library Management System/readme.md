# 📚 Library Management System

A beginner-friendly **Library Management System built using Python**.

This project manages books and library members and supports basic library operations such as adding books, issuing and returning books, searching books, and deleting records.

## 🚀 Version 1 — Basic Library Management

### Features

- ➕ Add books
- 📖 View all books
- 🔍 Search books by:
  - Book ID
  - Book title
- 👤 Add members
- 👥 View all members
- 📤 Issue books to members
- 📥 Return books
- 🗑️ Delete books
- ❌ Delete members
- 🔄 Track book availability
- 👤 Track which member currently has a book

## 🗂️ Data Structure

The project uses Python dictionaries to store data.

### Books

Each book is stored using its Book ID:

```python
books = {
    101: {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "status": "available",
        "borrowed_by": None
    }
}
```

### Members

Each member is stored using their Member ID:

```python
members = {
    1: {
        "name": "Keerthi"
    }
}
```

## ⚙️ Library Rules

- A book can be issued only if it is available.
- A book cannot be issued to another member while already issued.
- A book must be returned before it can be deleted.
- A member cannot be deleted while they have a borrowed book.
- Returning a book changes its status back to `available`.
- `borrowed_by` stores the Member ID when a book is issued.

## 🧠 Python Concepts Used

- Variables
- Data Types
- Dictionaries
- Nested Dictionaries
- Functions
- Loops
- Conditional Statements
- `input()` and `print()`
- Dictionary traversal using `.items()`
- Dictionary modification
- Boolean flags
- `break`
- `return`
- Basic program flow and state management

## 🧪 Testing

The following operations were tested:

- Adding multiple books
- Adding multiple members
- Viewing books and members
- Searching by Book ID
- Searching by title
- Issuing available books
- Preventing already-issued books from being issued again
- Returning books
- Reissuing returned books
- Preventing deletion of members who currently have books
- Deleting members after returning their books

## 📌 Current Version

**V1 — Basic Library Management System ✅**

This version focuses on understanding the core logic and integrating multiple operations into one working application.

## 🔮 Future Versions

### V2 — Validation & Exception Handling
- Handle invalid inputs
- Prevent duplicate Book IDs
- Prevent duplicate Member IDs
- Validate empty names/titles
- Handle invalid Book/Member IDs
- Improve error handling

### V3 — Library Analysis
- Available vs issued books
- Member borrowing statistics
- Most-issued books
- Library statistics
-

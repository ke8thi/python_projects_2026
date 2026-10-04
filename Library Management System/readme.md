# 📚 Library Management System

A beginner-friendly **Library Management System built using Python**.

This project manages books and library members and supports library operations such as adding books, issuing and returning books, searching books, deleting records, input validation, and exception handling.

The project is developed **version-by-version** to gradually improve functionality and strengthen Python programming skills.

---

## 🚀 Version 1 — Basic Library Management

### Features

- ➕ Add books
- 📖 View all books
- 🔍 Search books by:
  - Book ID
  - Book title
- 👤 Add members
- 👥 View members
- 📤 Issue books to members
- 📥 Return books
- 🗑️ Delete books
- ❌ Delete members
- 🔄 Track book availability
- 👤 Track which member currently has a book

---

## 🛡️ Version 2 — Validation & Exception Handling

V2 improves the reliability of the application by handling invalid user input and preventing invalid operations.

### Input Validation

- Validate Book IDs
- Validate Member IDs
- Handle non-integer IDs using `try/except`
- Prevent duplicate Book IDs
- Prevent duplicate Member IDs
- Prevent empty book titles
- Prevent empty author names
- Prevent empty member names
- Reject spaces-only input using `.strip()`
- Validate menu/search choices
- Validate `y/n` continuation input

### Search Validation

- Validate Book ID search input
- Handle non-existent Book IDs
- Validate title search input
- Handle non-existent book titles

### Issue & Return Validation

- Validate Book ID before issuing
- Validate Member ID before issuing
- Prevent issuing non-existent books
- Prevent issuing books to non-existent members
- Prevent issuing an already-issued book
- Validate Book ID before returning
- Handle non-existent books during return

### Delete Validation

- Validate Book ID before deletion
- Prevent deletion of non-existent books
- Prevent deletion of books that are currently issued
- Validate Member ID before deletion
- Prevent deletion of non-existent members
- Prevent deletion of members who currently have borrowed books

---

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

---

## ⚙️ Library Rules

- A book can be issued only if it is available.
- A book cannot be issued to another member while already issued.
- A book must be returned before it can be deleted.
- A member cannot be deleted while they have a borrowed book.
- Returning a book changes its status back to `available`.
- `borrowed_by` stores the Member ID when a book is issued.
- Duplicate Book IDs and Member IDs are not allowed.

---

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
- `try/except`
- `ValueError`
- Input validation
- `.strip()`
- Basic program flow and state management

---

## 🧪 Testing

V2 was tested using invalid inputs, edge cases, and normal library operations.

### Validation Testing

- Non-integer Book IDs
- Non-integer Member IDs
- Duplicate Book IDs
- Duplicate Member IDs
- Empty titles
- Spaces-only titles
- Empty author names
- Spaces-only author names
- Empty member names
- Spaces-only member names
- Invalid menu choices
- Invalid `y/n` input

### Functional Testing

- Adding multiple books
- Adding multiple members
- Searching by Book ID
- Searching by title
- Issuing books
- Preventing duplicate issuance
- Returning books
- Preventing deletion of issued books
- Deleting available books
- Preventing deletion of members with borrowed books
- Deleting members after returning their books

**Testing Status:** ✅ Passed

---

## 📌 Current Version

**V2 — Validation & Exception Handling ✅**

V2 focuses on making the application more reliable by handling invalid user input, preventing duplicate records, validating operations, and protecting existing library data.

---

## 🔮 Future Versions

### V3 — Library Analysis

- Available vs issued books
- Member borrowing statistics
- Most-issued books
- Library statistics
- Search and filtering improvements

### V4 — Reports & Display

- Formatted library reports
- Improved output organization
- Better user interaction
- Enhanced reporting

### V5 — JSON Persistence

- Save books and members to JSON
- Load library data when the program starts
- Automatically save changes
- Persistent library records

### V6 — Final Polish

- Code refactoring
- Additional testing
- Improved structure
- Final documentation
- GitHub-ready release

---

## 🎯 Learning Goal

The goal of this project is to strengthen Python programming through practical development.

Instead of building the entire application at once, each version introduces new concepts and improvements while maintaining the functionality developed in previous versions.

**Current Progress:**

```text
V1 → Basic Functionality ✅
        ↓
V2 → Validation & Exception Handling ✅
        ↓
V3 → Analysis 🔜
        ↓
V4 → Reports & Display
        ↓
V5 → JSON Persistence
        ↓
V6 → Final Polish
```

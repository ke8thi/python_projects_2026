# 📚 Library Management System

A beginner-friendly **Library Management System built using Python**.

This project manages books and library members and supports library operations such as adding books, issuing and returning books, searching and filtering books, deleting records, library statistics, borrowing analysis, borrowing history, activity reports, input validation, and exception handling.

The project is developed **version-by-version** to gradually improve functionality and strengthen Python programming and problem-solving skills.

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
- 🛡️ Prevent deletion of issued books
- 🛡️ Prevent deletion of members who have borrowed books

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
- Prevent returning non-existent books
- Prevent returning a book that is already available

### Delete Validation

- Validate Book ID before deletion
- Prevent deletion of non-existent books
- Prevent deletion of books that are currently issued
- Validate Member ID before deletion
- Prevent deletion of non-existent members
- Prevent deletion of members who currently have borrowed books

---

## 📊 Version 3 — Library Analysis & Statistics

V3 adds analysis features that provide useful information about the library and its borrowing activity.

### Library Statistics

- Total number of books
- Total number of members
- Number of available books
- Number of issued books

### Book Status Filtering

- View available books
- View issued books
- Display borrower information for issued books
- Handle cases where no books match the selected status

### Member Borrowing Statistics

- Display each member's ID
- Display each member's name
- Count the number of books currently borrowed by each member
- Handle libraries with no members

### Issue Count Tracking

Each book maintains an `issue_count`.

- New books start with an issue count of `0`
- Issue count increases after every successful issue
- Returning a book does not change the issue count
- Re-issuing a book increases the count again

### Most-Issued Books

- Find the book with the highest issue count
- Display all books tied for the highest issue count
- Handle libraries with no books
- Handle cases where no books have been issued yet

### Search Improvements

Books can now be searched by:

- Book ID
- Book title
- Author

Author search supports multiple books written by the same author.

### V3 Testing

- Statistics testing
- Available/issued book filtering
- Member borrowing statistics
- Issue-count testing
- Most-issued book testing
- Tie-case testing
- Author search testing
- Invalid input testing
- Edge-case testing
- Full functional testing

**Testing Status:** ✅ Passed

---

## 📜 Version 4 — Borrowing History & Activity Tracking

V4 adds detailed borrowing history and activity tracking without duplicating the analysis features introduced in V3.

### Borrowing History

Each book now maintains a `history` list containing borrowing activity.

Each history record stores:

- Member ID
- Action

Example:

```python
"history": [
    {"member_id": 1, "action": "issued"},
    {"member_id": 1, "action": "returned"}
]
```

### Issue History Tracking

- Record every successful book issue
- Store the Member ID who borrowed the book
- Store the action as `"issued"`
- Preserve all previous borrowing records

### Return History Tracking

- Record every successful book return
- Store the Member ID who previously borrowed the book
- Store the action as `"returned"`
- Preserve the history after the book is returned

### Book History

Books can now be viewed individually by Book ID.

The report displays:

- Book ID
- Member ID
- Action

It also handles books with no borrowing history.

### Member History

Members can now view their complete borrowing activity across books.

The report displays:

- Member ID
- Book ID
- Action

It also handles members with no borrowing history.

### Recent Library Activity

Displays borrowing activity across all books, including:

- Book ID
- Member ID
- Action

The report handles libraries with no recorded activity.

### Book Activity Report

Provides activity information for every book:

- Book ID
- Book title
- Total times issued
- Number of history records

This differs from the V3 Most-Issued Books feature because it reports activity for **every book** rather than only identifying the most-issued book.

### V4 Testing

- Issue history testing
- Return history testing
- Re-issue history testing
- Book history testing
- Member history testing
- Recent activity testing
- Book activity report testing
- Empty-history testing
- Existing V3 feature regression testing
- Full functional testing

**Testing Status:** ✅ Passed

---

## 🗂️ Data Structure

The project uses Python dictionaries to store books and members.

### Books

Each book is stored using its Book ID:

```python
books = {
    101: {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "status": "available",
        "borrowed_by": None,
        "issue_count": 0,
        "history": []
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
- `borrowed_by` becomes `None` after a book is returned.
- `issue_count` tracks the total number of successful issues.
- `history` stores the issue and return activity of a book.
- Duplicate Book IDs and Member IDs are not allowed.

---

## 🧠 Python Concepts Used

- Variables
- Data Types
- Dictionaries
- Nested Dictionaries
- Lists
- Dictionaries inside Lists
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
- `len()`
- `max()`
- `.append()`
- Nested loops
- Searching and filtering
- Counting and statistics
- History tracking
- Menu-driven applications
- Basic program flow and state management
- Edge-case testing

---

## 🧪 Testing

The application was tested using invalid inputs, edge cases, and normal library operations.

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
- Searching by author
- Issuing books
- Preventing duplicate issuance
- Returning books
- Tracking issue counts
- Recording issue history
- Recording return history
- Viewing book history
- Viewing member history
- Viewing recent library activity
- Viewing book activity reports
- Viewing available books
- Viewing issued books
- Viewing member borrowing statistics
- Finding most-issued books
- Handling tied most-issued books
- Preventing deletion of issued books
- Deleting available books
- Preventing deletion of members with borrowed books
- Deleting members after returning their books
- Library statistics verification
- Empty-history testing
- Edge-case testing
- V3 regression testing after V4 changes

**V4 Testing Status:** ✅ Passed

---

## 📌 Current Version

**V4 — Borrowing History & Activity Tracking ✅**

V4 extends the library system with detailed borrowing history, member activity tracking, recent library activity, and book-level activity reports while preserving all functionality developed in V1–V3.

The project currently contains:

```text
V1 → Basic Library Management ✅
V2 → Validation & Exception Handling ✅
V3 → Library Analysis & Statistics ✅
V4 → Borrowing History & Activity Tracking ✅
```

---

## 🔮 Future Versions

### V5 — JSON Persistence

- Save books and members to JSON
- Load library data when the program starts
- Automatically save changes
- Persistent library records
- Preserve borrowing history between program runs

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

### Current Progress

```text
V1 → Basic Functionality ✅
        ↓
V2 → Validation & Exception Handling ✅
        ↓
V3 → Analysis & Statistics ✅
        ↓
V4 → Borrowing History & Activity Tracking ✅
        ↓
V5 → JSON Persistence
        ↓
V6 → Final Polish
```

---

## 📁 Project Files

```text
Library Management System/
│
├── version-1.py
├── version-2.py
├── version-3.py
├── version-4.py
└── README.md
```

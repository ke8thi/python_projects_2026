# Student Grade Management System

A console-based Python project for managing student details and marks.

This project was built to practice Python dictionaries, nested dictionaries, loops, conditions, functions, calculations, input validation, and exception handling.

## Features

### V1 – Basic Student Management
- Add students
- View all students
- Calculate total marks
- Calculate average marks
- Calculate grades
- Search for a student
- Delete a student
- Exit the program

### V2 – Validation & Error Handling
- Menu option validation
- Student ID validation
- Duplicate ID prevention
- Positive ID validation
- Empty name validation
- Marks validation
- Marks restricted to `0–100`
- Handles non-integer input
- Search validation for non-existing IDs
- Delete validation for non-existing IDs
- `y/n` continuation validation
- Exception handling using `try-except`

## Data Structure

Student information is stored using a nested dictionary:

```python
students = {
    1: {
        "name": "Keerthi",
        "marks": {
            "math": 90,
            "science": 80,
            "english": 80
        }
    }
}
## 🚀 Version 3

Version 3 focuses on **student performance analysis** and adds several useful academic statistics.

### ✨ Features

- ➕ Add student
- 👀 View all students
- 🧮 Calculate total marks
- 📊 Calculate average marks
- 🏆 Calculate grades
- 📈 Calculate percentage
- 🥇 Find top-performing student
- 📉 Find lowest-performing student
- 🏫 Calculate class average
- 📋 Display grade distribution
- ✅ Pass/Fail statistics
- 🔍 Search student by ID
- 🗑️ Delete student
- 🚪 Exit application

---

## 📚 Grade System

| Average | Grade |
|--------:|:-----:|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

Students with an average of **60 or above are considered passed**.

---

## 🛡️ Validation & Exception Handling

The application includes input validation for:

- Student ID
- Duplicate student IDs
- Student name
- Marks between 0–100
- Integer-only inputs
- Menu options
- Search operations
- Delete operations
- Yes/No (`y/n`) inputs

Invalid inputs are handled using Python exception handling.

---

## 🧠 Concepts Practiced

This project helped strengthen my understanding of:

- Python dictionaries
- Nested dictionaries
- Loops
- Conditional statements
- Functions
- User input
- Exception handling
- Data validation
- Searching
- Deleting dictionary records
- Mathematical calculations
- Basic data analysis
- Menu-driven applications

---

## 🗂️ Data Structure

Student information is stored using a nested dictionary:

```python
students = {
    1: {
        "name": "Keerthi",
        "marks": {
            "math": 90,
            "science": 80,
            "english": 80
        }
    }
}
🧪 Testing

The application was tested with multiple scenarios, including:

Empty student list
Invalid menu input
Invalid student IDs
Duplicate IDs
Marks outside the 0–100 range
Zero marks
Exact grade boundaries
Pass/Fail boundaries
Multiple students
Tied top performers
Tied lowest performers
Boundary Testing
90 → A
80 → B
70 → C
60 → D
59 → F

All tested cases produced the expected results.

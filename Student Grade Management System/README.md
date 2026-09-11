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

# Student Grade Management System

A console-based Python project for managing student details, marks, grades, and academic performance.

This project was built step-by-step to practice Python dictionaries, nested dictionaries, loops, conditions, functions, calculations, input validation, exception handling, sorting, and basic data analysis.

---

## 🚀 Features

### V1 – Basic Student Management

- ➕ Add students
- 👀 View all students
- 🧮 Calculate total marks
- 📊 Calculate average marks
- 🏆 Calculate grades
- 🔍 Search for a student
- 🗑️ Delete a student
- 🚪 Exit the program

---

### V2 – Validation & Error Handling

Added input validation and exception handling.

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

---

### V3 – Performance Analysis

Version 3 focuses on student performance analysis and academic statistics.

- 📈 Calculate percentage
- 🥇 Find top-performing student
- 📉 Find lowest-performing student
- 🏫 Calculate class average
- 📋 Grade distribution
- ✅ Pass/Fail statistics

---

### V4 – Reports, Ranking & Display

Version 4 focuses on generating detailed reports and improving the application's presentation.

- 📄 Individual student report
- 📊 All students report
- 🏆 Performance ranking
- 🔍 Enhanced student search using the student report
- 🧹 Improved menu and report display
- ✨ Consistent headings and output formatting
- 🧪 Full functional and edge-case testing

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

The application validates:

- Student IDs
- Duplicate student IDs
- Positive student IDs
- Student names
- Marks between `0–100`
- Integer-only inputs
- Menu options
- Search operations
- Delete operations
- Student report IDs
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
- Sorting
- `lambda`
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
Each student has:

A unique student ID
Student name
Math marks
Science marks
English marks
📊 Reports
Student Report

Displays complete information for an individual student:

Student ID
Name
Subject marks
Total marks
Average
Percentage
Grade
Pass/Fail status
All Students Report

Displays a summary of all students including:

ID
Name
Total marks
Average
Grade
Status
Performance Ranking

Students are ranked according to their average marks, from highest to lowest.

🧪 Testing

The application was tested with multiple scenarios, including:

Empty student list
Invalid menu input
Invalid student IDs
Duplicate IDs
Empty student names
Marks outside the 0–100 range
Non-integer marks
Zero marks
Exact grade boundaries
Pass/Fail boundaries
Multiple students
Student deletion
Recalculation after deletion
Invalid search IDs
Invalid report IDs
Tied top performers
Tied lowest performers
Boundary Testing

The following grade boundaries were tested:

90 → A
80 → B
70 → C
60 → D
59 → F

Pass/Fail boundary:

60 → PASS
59 → FAIL

All tested cases produced the expected results.

📁 Project Versions
Student Grade Management System/
│
├── student_grade_v1.py
├── student_grade_v2.py
├── student_v3.py
├── student_v4.py
└── README.md
🔮 Future Improvements

Planned improvements for future versions:

V5 – JSON Persistence
Save student data to JSON
Load student data when the program starts
Automatically save changes
Handle missing or empty JSON files
V6 – Final Polish
Further improve the user interface
Improve code organization
Final testing and cleanup
👨‍💻 Project Status
Version	Status
V1 – Basic Management	✅ Complete
V2 – Validation	✅ Complete
V3 – Performance Analysis	✅ Complete
V4 – Reports & Ranking	✅ Complete
V5 – JSON Persistence	🔜 Planned
V6 – Final Polish	🔜 Planned
🎯 Learning Goal

The main goal of this project is to strengthen Python fundamentals by building a complete console-based application step-by-step, while gradually introducing more practical programming concepts.

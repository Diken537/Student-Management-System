# Student Management System

## 📌 About the Project

The **Student Management System** is a beginner-friendly Python project designed to manage student records efficiently. It allows users to add new students, update existing student information, and display student names and their corresponding grades.

The project uses Python's built-in data structures and JSON file handling to store and retrieve student information. This ensures that student records remain saved even after the program is closed and can be accessed again when the program is executed.

## ✨ Features

- **Add Student:** Add new students along with their grades.
- **Update Student Name:** Modify the name of an existing student.
- **Update Student Grade:** Update the academic marks of a student.
- **Display Student Records:** View all stored student names and grades.
- **Data Persistence:** Store student records in a JSON file so that data is not lost after program termination.
- **Input Validation:** Handle invalid numerical inputs when entering student grades.

## 🛠️ Technologies Used

- **Python 3**
- **JSON:** For storing and retrieving student records.
- **PyCharm:** Development environment.
- **Git and GitHub:** Version control and project hosting.

## 📂 Project Structure

```text
Student_management_system/
│
├── main.py
├── add_update_student.py
├── data_storage.py
├── student_data_collection.py
├── student.json
└── README.md
```

## ⚙️ How to Run the Project

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd Student_management_system
```

**3. Run the program**

```bash
python main.py
```

## 💾 Data Storage

The project uses a JSON file (`student.json`) to store student information.

Student records are maintained in the following format:

```json
[
    ["Ram", 85],
    ["Shyam", 90],
    ["Hari", 78]
]
```

Whenever student information is updated or added, the data can be saved to the JSON file and retrieved during the next execution.

## 🎯 Learning Objectives

This project helped me understand and practice several fundamental Python programming concepts:

- Functions and modular programming
- Lists and tuples
- Loops and conditional statements
- Tuple unpacking
- The `enumerate()` function
- Exception handling (`try-except`)
- File handling
- JSON serialization and deserialization
- Data persistence

## 🚀 Future Improvements

- Implement student record deletion.
- Add student ID for unique identification.
- Improve input validation.
- Introduce a graphical user interface (GUI).
- Integrate a database such as SQLite for more advanced data management.

## 👨‍💻 Author

**Diken Lamichhane**

Computer Engineering Student

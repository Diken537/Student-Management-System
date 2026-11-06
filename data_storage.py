
import json

FILE_NAME = "student.json"


def save_students(students):
    with open(FILE_NAME, 'w') as f:
        json.dump(students, f, indent=4)


def load_students():
    try:
        with open(FILE_NAME, 'r') as f:
            students = json.load(f)

        valid_students = []

        for student in students:
            if isinstance(student, (list, tuple)) and len(student) == 2: #checking wether the data contain two values or not
                name, grade = student
                valid_students.append((name, grade))
            else:
                print("Invalid student record:", student)

        return valid_students

    except FileNotFoundError:
        return []

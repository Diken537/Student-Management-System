def display_sorted_students(students):
    students_sorted_by_name = sorted(students, key= lambda student: student[0])
    students_sorted_by_grade = sorted(students, key = lambda student: student[1])

    print("\nStudent sorted by name:")
    for name, grade in students_sorted_by_name:
        print(f"{name}: {grade}")

    print("\nStudent sorted by grade:")
    for name, grade in students_sorted_by_grade:
        print(f"{name}: {grade}")


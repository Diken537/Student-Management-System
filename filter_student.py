
def display_pass_fail(students):

    passed_students = list(
        filter(lambda student: student[1] >= 40, students)
    )

    failed_students = list(
        filter(lambda student: student[1] < 40, students)
    )

    print("\nPassed Students:")
    for name, grade in passed_students:
        print(f"{name}: {grade}")

    print("\nFailed Students:")
    for name, grade in failed_students:
        print(f"{name}: {grade}")

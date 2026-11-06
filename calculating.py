
def display_statistics(students):

    if not students:
        print("No student records available.")
        return

    grades = list(map(lambda student: student[1], students))

    average = sum(grades) / len(grades)

    highest_grade_student = max(students, key=lambda student: student[1])
    lowest_grade_student = min(students, key=lambda student: student[1])

    print(f"\nAverage grade: {average:.2f}")

    print(
        f"Highest grade: {highest_grade_student[0]} "
        f"with {highest_grade_student[1]}"
    )

    print(
        f"Lowest grade: {lowest_grade_student[0]} "
        f"with {lowest_grade_student[1]}"
    )

def clear_all_student_data(students):
    if not students:
        print("\n student data is empty")
        return

    confirmation = input("\n Are you sure you want to clear all student data? (y/n)").strip().lower()
    if confirmation == 'y':
        students.clear()
        print("\n student data is cleared")

    else:
        print('operation cancelled')
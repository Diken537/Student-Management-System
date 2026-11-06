
import add_update_student
import filter_student
import calculating
import displaying_data
import sorting_student
import student_data_collection
import clear_data
import data_storage


def display_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Filter students")
    print("4. Sort student records")
    print("5. Perform calculations")
    print("6. Update student records")
    print("7. Clear all student records")
    print("8. Exit")


def main():
    student_data = data_storage.load_students()

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        print(f"You selected: {choice}")  # Debugging line

        if choice == "1":
            new_students = student_data_collection.student_datae()
            student_data.extend(new_students)
            data_storage.save_students(student_data)

        elif choice == "2":
            displaying_data.displaying_data(student_data)

        elif choice == "3":
            filter_student.display_pass_fail(student_data)

        elif choice == "4":
            sorting_student.display_sorted_students(student_data)

        elif choice == "5":
            calculating.display_statistics(student_data)

        elif choice == "6":
            add_update_student.update_student(student_data)
            data_storage.save_students(student_data)

        elif choice == "7":
            clear_data.clear_all_student_data(student_data)
            data_storage.save_students(student_data)

        elif choice == "8":
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()

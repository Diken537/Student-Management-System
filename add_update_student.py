
def update_student(students):
    while True:
        name = input("Enter student name: ")

        x = input(
            "Enter '1' to update name, "
            "'2' to update grade, '3' to exit: "
        )

        if x == "1":
            for index, student in enumerate(students):
                if student[0].lower() == name.lower():

                    new_name = input("Enter new name: ")

                    students[index] = (new_name, student[1])

                    print("Student name updated successfully!")
                    break
            else:
                print("Student not found!")

        elif x == "2":
            for index, student in enumerate(students):
                if student[0].lower() == name.lower():

                    grade = float(input("Enter updated marks: "))

                    students[index] = (student[0], grade)

                    print("Student marks updated successfully!")
                    break
            else:
                print("Student not found!")

        elif x == "3":
            print("Exit")
            return

        else:
            print("Invalid option! Please choose 1, 2, or 3.")

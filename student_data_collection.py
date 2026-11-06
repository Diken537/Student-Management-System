def student_datae():
    students = []
    while True:
        name = input("enter name of student(or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for{name}: "))
            students.append((name, grade)) #storing the data as tuple
        except ValueError:
            print("Invalid input. please enter a valid grade (numeric value).")
    return students
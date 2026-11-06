def displaying_data(students):
    if not students:
        print("data is empty")
    else:
        print("\n student grades:")
        for name, grade in students:
            print(f"{name}: {grade}")
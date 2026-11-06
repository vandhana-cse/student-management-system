students = []

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        reg_no = input("Enter register number: ")
        department = input("Enter department: ")

        students.append([name, reg_no, department])
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            print("\nAll students:")
            for student in students:
                print("Name:", student[0])
                print("Register number:", student[1])
                print("Department:", student[2])

    elif choice == "3":
        search_reg = input("Enter register number: ")
        found = False

        for student in students:
            if student[1] == search_reg:
                print("Student found!")
                print("Name:", student[0])
                print("Register number:", student[1])
                print("Department:", student[2])
                found = True

        if not found:
            print("Student not found!")

    elif choice == "4":
        update_reg = input("Enter register number: ")
        found = False

        for student in students:
            if student[1] == update_reg:
                student[0] = input("Enter new name: ")
                student[2] = input("Enter new department: ")
                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "5":
        delete_reg = input("Enter register number: ")
        found = False

        for student in students:
            if student[1] == delete_reg:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

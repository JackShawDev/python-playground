def display_menu(menu_options):
    for index, choice in enumerate(menu_options):
        print(str(index + 1) + ".", choice)

    print()

def run_student_register(menu_options, students):
    menu_choice = 0

    display_menu(menu_options)

    while menu_choice != 4:
        menu_choice = int(
            input("What would you like to do? Please enter a number between 1 and 4: ")
        )

        if menu_choice == 1:
            view_register(students)
            display_menu(menu_options)
        elif menu_choice == 2:
            add_students(students)
            display_menu(menu_options)
        elif menu_choice == 3:
            remove_students(students)
            display_menu(menu_options)
        elif menu_choice == 4:
            print()
            print("Closing Student Register...")
        else:
            print("Invalid input")
            print()

def display_register(students):
    if len(students) == 0:
        print("The student register is currently empty.")
        print()
    else:
        print("Total students: " + str(len(students)))
        print()

        for index, student in enumerate(students):
            print(str(index + 1) + ".", student)

def view_register(students):
    print()
    display_register(students)
    
    print()
    input("Press Enter to return to the main menu...")
    print()

def add_students(students):
    student = "Loop Start"
    
    print()
    print("Enter student names.")
    print("Leave blank to finish.")
    print()

    while student != "":
        student = input("Student name: ")

        if student != "":
            students.append(student)
            print("Name added, please enter next name.")
            print()
        else:
            print("Name entry complete.")
            print()
        
    display_register(students)

    print()
    input("Press Enter to return to the main menu...")
    print()

def remove_students(students):
    if len(students) == 0:
        print("There are no students to remove.")
        print()
        input("Press Enter to return to the main menu...")
        print()
        return
    
    print()
    display_register(students)

    remove_choice = "Loop start"

    while remove_choice != "":
        print()
        print("Leave blank to finish.")
        print()

        remove_choice = input("Which student would you like to remove? ")
        print()

        if remove_choice != "":
            remove_choice = int(remove_choice)

            if 1 <= remove_choice <= len(students):
                student_index = remove_choice - 1
                removed_student = students.pop(student_index)
                print(removed_student + " was removed from the register.")
                print()

                display_register(students)

                if len(students) == 0:
                    remove_choice = ""

            else:
                print("Please enter a valid student number.")

students = ["Alice", "Bob"]
menu_options = ["View register", "Add students", "Remove students", "Exit"]

print("Welcome to the student register!")
print()

run_student_register(menu_options, students)

""" Week 3 Day 3 Update
Currently reuses the student variable in both `student = input("Student name: ")` and `for student in students:`
This is because they currently represent the same idea of a single student, but if this project was to expand then it may be approrpriate to change the input variable to something like current_student
"""

""" Week 3 Day 4 Update
Redesigned the initial exercise into a menu based program, adding each function into it's own branch
This allowed me to learn how to handle loops in a basic menu system alongside identifying reused code between functions
Also learned how to remove items from a list
"""
students = []

print("Student Register")
print()

print("Enter student names.")
print("Leave the name blank to finish.")
print()

student = "Loop Start"

while student != "":
    student = input("Student name: ")

    if student != "":
        students.append(student)
        print("Name added, please enter next name.")
    else:
        print("Name entry complete.")

if len(students) == 0:
        print()
        print("No students were added.")
else:
    print()
    print("Total students: " + str(len(students)))
    print()

    for student in students:
        print(student)

"""
Currently reuses the student variable in both `student = input("Student name: ")` and `for student in students:`
This is because they currently represent the same idea of a single student, but if this project was to expand then it may be approrpriate to change the input variable to something like current_student
"""
def add_student(students, student_name):
    if student_name in students:
        print(f'{student_name} already exists in students.')
    else:
        students[student_name] = {}

def add_grade(students, student, subject, grade):
    if student not in students:
        print(f'{student} is not in students. Please add them first.')
    else:
        if subject in students[student]:
            print(f"Grade for subject '{subject}' already exists for {student}.")
        else:
            students[student][subject] = grade
            print(f"Added grade {grade} for subject '{subject}' to {student}.")

def update_grade(students, student, subject, grade):
    if student not in students:
        print(f'{student} is not in students. Please add them first.')
    else:
        if subject in students[student]:
            students[student][subject] = grade 
            print(f"Updated {student} with grade: {grade} for subject '{subject}'.")
        else:
            print(f"Grade for subject '{subject}' does not exist for {student}.")

def delete_grade(students, student, subject):
    if student not in students:
        print(f'{student} is not in students. Please add them first.')
    else:
        if subject in students[student]:
            del students[student][subject]
            print(f"Deleted {subject} grade for {student}.")
        else:
            print(f"Grade for subject '{subject}' does not exist for {student}.")

def view_grades(students, student):
    if student not in students:
        print(f'{student} is not in students. Please add them first.')
    else:
        print(f'Grades for {student}:')
        if not students[student]:
            print("No grades available.")
        else:
            for subject, grade in students[student].items():
                print(f"{subject}: {grade}")

def calculate_gpa(students, student):
    if student not in students:
        print(f'{student} is not in students. Please add them first.')
    else:
        grades = students[student].values()
        if grades:
            gpa = sum(grades) / len(grades)
            return gpa
        else:
            print(f'{student} has no grades yet.')
            return None

# Initial student management system
students = {}

# Add students
add_student(students, 'Alice')
add_student(students, 'Bob')

# Add grades
add_grade(students, 'Alice', 'Math', 90)
add_grade(students, 'Alice', 'Science', 85)
add_grade(students, 'Bob', 'Math', 78)

# Update grades
update_grade(students, 'Alice', 'Math', 95)

# Delete grades
delete_grade(students, 'Bob', 'Math')

# View grades
view_grades(students, 'Alice')

# Calculate GPA
gpa = calculate_gpa(students, 'Alice')
if gpa is not None:
    print(f"Alice's GPA: {gpa}")

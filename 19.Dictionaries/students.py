students_info = {}
command = input()

while ":" in command:

    current_student = command.split(":")
    student_name = current_student[0]
    student_id = current_student[1]
    student_course = current_student[2]

    if student_course not in students_info:
        students_info[student_course] = {}

    students_info[student_course][student_id] = student_name
    command = input()

course = " ".join(command.split("_"))

for key, value in students_info.items():
    if key == course:
        for student_id, student_name in value.items():
            print(f"{student_name} - {student_id}")
            

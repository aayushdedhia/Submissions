students = input("Enter student names separated by space: ").split()
subjects = input("Enter subjects separated by space: ").split()

student_subject_map = {students[i]: subjects[i] for i in range(len(students))}
print(student_subject_map)

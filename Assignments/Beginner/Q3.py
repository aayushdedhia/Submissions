subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
marks = [float(input(f"Enter marks for {subject}: ")) for subject in subjects]

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

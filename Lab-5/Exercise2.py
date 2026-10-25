students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


# Task 1: Calculate average
def calculate_average(marks):
    if not marks:
        raise ValueError("No marks available")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Invalid marks")

    return sum(marks) / len(marks)


# Task 2: Classify performance
def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# Task 3: Display student report
def display_report(students):
    if not students:
        print("No student records")
        return

    for student in students:
        student_id, name, marks = student

        try:
            average = calculate_average(marks)
            performance = classify_performance(average)

            print("ID:", student_id)
            print("Name:", name)
            print("Average:", round(average, 2))
            print("Performance:", performance)
            print("---------------------")

        except ValueError as error:
            print(name, "Error:", error)


display_report(students)
print("EQUAL MARKS TEST")
print(calculate_average([80, 80, 80]))

print("\nTIED AVERAGE TEST")
print(calculate_average([70, 80]))
print(calculate_average([75, 75]))

print("\nINVALID MARK TEST")
display_report([
    [206, "Invalid", [50, 110, 70]]
])

print("\nMISSING MARKS TEST")
display_report([
    [207, "NoMarks", []]
])
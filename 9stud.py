


def calculate_total(marks):
    return sum(marks)



def calculate_average(marks):
    return sum(marks) / len(marks)



def find_highest(marks):
    return max(marks)



def find_lowest(marks):
    return min(marks)



def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"



n = int(input("Enter number of students: "))

students = []


for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input("Enter mark for subject " + str(j + 1) + ": "))
        marks.append(mark)

    
    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = get_grade(average)

    
    student = {
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    }

    students.append(student)



students.sort(key=lambda x: x["total"], reverse=True)



print("\n----- Student Performance Details -----")

for student in students:
    print("\nName     :", student["name"])
    print("Total    :", student["total"])
    print("Average  :", round(student["average"], 2))
    print("Highest  :", student["highest"])
    print("Lowest   :", student["lowest"])
    print("Grade    :", student["grade"])
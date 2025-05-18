student_name = "Oluyi Adetomiwa"
matric_number = "22CK031255"

def score_to_grade_point(score):
    if score >= 70:
        return 5  # A
    elif score >= 60:
        return 4  # B
    elif score >= 50:
        return 3  # C
    elif score >= 45:
        return 2  # D
    elif score >= 40:
        return 1  # E
    else:
        return 0  # F

# Input for 6 courses
courses = []
total_units = 0
total_weighted_points = 0

print(f"Enter details for {student_name} (Matric No: {matric_number})")

for i in range(1, 7):
    print(f"\nCourse {i}:")
    course_code = input("Course Code: ")
    score = int(input("Score (0-100): "))
    unit = int(input("Credit Unit: "))

    grade_point = score_to_grade_point(score)
    weighted_point = grade_point * unit

    courses.append({
        "course_code": course_code,
        "score": score,
        "unit": unit,
        "grade_point": grade_point,
        "weighted_point": weighted_point
    })

    total_units += unit
    total_weighted_points += weighted_point

# Calculate CGPA
cgpa = total_weighted_points / total_units if total_units > 0 else 0

# Display Result
print("\n--- CGPA RESULT ---")
print(f"Student Name: {student_name}")
print(f"Matric Number: {matric_number}\n")

print("Course Results:")
print("{:<10} {:<6} {:<6} {:<12}".format("Course", "Score", "Unit", "Grade Point"))
for course in courses:
    print("{:<10} {:<6} {:<6} {:<12}".format(course["course_code"], course["score"], course["unit"], course["grade_point"]))

print(f"\nTotal Units: {total_units}")
print(f"CGPA: {cgpa:.2f}")
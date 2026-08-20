def calculate_statistics(*grades, **student_info):
    if not grades:
        return None

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    # Calculate letter grade distribution
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return minimum, maximum, average, distribution, student_info


# -------------------------
# Example
# -------------------------

minimum, maximum, average, distribution, info = calculate_statistics(
    85, 92, 76, 64, 90, 55,
    subject="Python",
    semester=4
)

print("Subject:", info["subject"])
print("Semester:", info["semester"])
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", round(average, 2))
print("Grade Distribution:", distribution)

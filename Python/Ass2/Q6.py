def assign_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 70 <= marks <= 89:
        return 'B'
    elif 50 <= marks <= 69:
        return 'C'
    elif 40 <= marks <= 49:
        return 'D'
    elif 0 <= marks <= 39:
        return 'F'
    else:
        return 'Invalid Input: Marks should be between 0 and 100'

# Example usage:
marks = float(input("Enter the student's marks: "))
grade = assign_grade(marks)
print(f"Grade: {grade}")

# Employee data with current salary and performance rating
employees = {
    "Alice": {"current_salary": 50000, "rating": "Excellent"},
    "Bob": {"current_salary": 40000, "rating": "Good"},
    "Charlie": {"current_salary": 45000, "rating": "Average"},
    "David": {"current_salary": 35000, "rating": "Poor"}
}

# Increment percentages based on performance rating
increments = {
    "Excellent": 20,
    "Good": 15,
    "Average": 10,
    "Poor": 5
}

print("Updated Employee Salaries:")

# Loop through employees and calculate new salary
for name, details in employees.items():
    salary = details["current_salary"]
    rating = details["rating"]
    increment_percentage = increments[rating]
    new_salary = salary + (salary * increment_percentage / 100)

    print(f"{name}: Current Salary = ${salary}, Rating = {rating}, "
          f"New Salary = ${new_salary:.2f}")

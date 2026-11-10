# Remember these three things:
# Dictionary = stores key-value pairs.
# .items() = gives both key and value.
# Nested loop = loops through each employee inside each department.

departments = {
    "IT": ["Ravi", "Hari"],
    "HR": ["Priya", "Kiran"]
}

for department, employees in departments.items():
    print("Department:", department)

    for employee in employees:
        print("Employee:", employee)
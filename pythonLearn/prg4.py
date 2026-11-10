# Imagine your manager gives you a list of employees and asks you to print each employee along with their serial number.
# Instead of manually managing the index, Python gives you enumerate().



employees = ["Priya", "Kiran", "Ravi", "Hari", "Arun"]

for index, employee in enumerate(employees):
    print(index, employee)
    
print("Employee List")
for index, employee in enumerate(employees, start=1):
    print(index, employee)


# Remember these three things:
# Dictionary = stores key-value pairs.
# .items() = gives both key and value.
# Nested loop = loops through each employee inside each department.
# range , for loop
for i in range(5):
    print("Hello, World!")
    print(i)  
    print("This is iteration number:", i)

#range(start, stop)
for i in range(1, 10):
    print("Iteration number:", i)


# #range(start, stop, intervals)
for i in range(1, 10, 2):
    print("Iteration number:", i)


#5. Real-world example: Employee attendance   
    
employees1 = ["Ravi", "Priya", "Kiran", "Anita", "Suresh", "Priya", "Ravi"] # list allows duplicate

for i in range(len(employees1)): 
    print("Employee ID:", i + 1)
    print("Employee Name:", employees1[i])    

# break, continue and pass — three keywords that control how loops execute.

# 1. break – Stop the loop




print("===== EMPLOYEE SEARCH PROGRAM =====")

employees = ["Priya", "Kiran", "Ravi", "Hari", "Arun"]

fname = input("Enter employee name: ").strip()

found = False

for employee in employees:

    if employee.lower() == fname.lower():

        print("Employee found!")
        print("Employee Name:", employee)

        found = True
        break

if not found:
    print("Employee not found!")

print("===== SEARCH COMPLETED =====")







# continue – Skip the current iteration
    
employees = [
    {"name": "Hola", "department": "IT"},
    {"name": "Bola", "department": "HR"},
    {"name": "kola", "department": "IT"},
    {"name": "Mola", "department": "Finance"}
]

for employee in employees:

    if employee["department"] != "IT":
        continue

    print(employee["name"])



# pass - Does nothing; acts as a placeholder.
def calculate_bonus():
 pass

print("Employee application started") 



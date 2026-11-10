class Employee:
    def display(self):
        print("This is an Employee class method.")

    def displayDetails(self, name, age):
        print("Employee Name:", name)
        print("Employee Age:", age)   

employee = Employee()
employee.name = "John"
employee.age = 30

employee.display()
employee.displayDetails(employee.name, employee.age)
employee.displayDetails("Alice", 25)
employee.displayDetails("Bob", 35)

# constructors
class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


employee1 = Employee("Ravi", 28, "IT")
employee2 = Employee("Priya", 32, "HR")
employee3 = Employee("Amit", 25, "Finance")

employee1.display_details()
employee2.display_details()
employee3.display_details()




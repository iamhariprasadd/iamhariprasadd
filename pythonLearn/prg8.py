# Day 2: Instance Variables vs Class Variables

# Imagine a company has 500 employees.
#
# Every employee has:
# - Name
# - Age
# - Department
# - Salary
#
# But the company also has common information:
# - Company name
# - Company location
#
# Should we store the company name separately
# for all 500 employees?
#
# No. We can use a class variable.

class Employee:

    # Class variable: Shared by all employees
    company_name = "Ellucian"

    def __init__(self, name, department, salary):

        # Instance variables: Different for each employee
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):

        print("Company:", self.company_name)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


# Creating employee objects
employee1 = Employee("Ravi", "IT", 50000)
employee2 = Employee("Priya", "HR", 40000)

employee1.display_details()
employee2.display_details()
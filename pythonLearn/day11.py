# ============================================================
# PYTHON OOP - ABSTRACTION
# ============================================================

# 1. WHAT IS ABSTRACTION?
#
# REAL-WORLD STORY:
#
# Imagine you are using an ATM.
#
# You insert your card.
# You enter your PIN.
# You select Withdraw.
# You enter an amount.
# You receive your money.
#
# Do you know what happens internally?
#
#   - How the ATM connects to the bank server?
#   - How it verifies your PIN?
#   - How it checks your account balance?
#   - How it communicates with the cash dispenser?
#
# No! You only need to know how to use the ATM.
#
# The ATM hides its internal implementation and exposes
# only the operations you need.
#
# This concept is called ABSTRACTION.
#
# DEFINITION:
# Abstraction means hiding internal implementation details
# and exposing only the essential functionality to the user.
#
# MEMORY TRICK:
# ABSTRACTION = WHAT TO DO, NOT HOW IT IS DONE.
#
# REAL-WORLD EXAMPLES:
#   ATM       -> Withdraw money without knowing internal logic.
#   Car       -> Press accelerator without knowing engine logic.
#   Mobile    -> Make a call without knowing network internals.
#   Application -> Click Login without knowing server internals.


# ============================================================
# 2. UNDERSTAND THE PROBLEM WITHOUT ABSTRACTION
# ============================================================

# Imagine a banking application.
#
# A user wants to withdraw money.
#
# The user should not need to understand:
#   - Balance validation
#   - Transaction processing
#   - Bank server communication
#   - Cash dispensing
#
# If we expose every internal operation directly,
# the user has to understand too much.
#
# We need a simple interface:
#
#       withdraw(amount)
#
# The internal implementation can handle the remaining work.


# ============================================================
# 3. ABSTRACTION USING ABSTRACT CLASSES
# ============================================================

# Python provides the abc module for abstraction.
#
# abc = Abstract Base Classes
#
# Important components:
#
# ABC:
#   Base class used to create abstract classes.
#
# abstractmethod:
#   Decorator used to declare a method that child classes
#   must implement.
#
# An abstract class cannot be instantiated directly
# when it contains abstract methods.


from abc import ABC, abstractmethod


# Create an abstract class.

class Payment(ABC):

    # This is an abstract method.
    # It defines WHAT every payment method must provide.
    # It does not define HOW each payment is processed.

    @abstractmethod
    def pay(self, amount):
        pass


# ============================================================
# 4. CHILD CLASS IMPLEMENTATION
# ============================================================

# Every payment type must implement pay().
#
# But each payment type can implement it differently.


class CreditCardPayment(Payment):

    def pay(self, amount):
        print("Processing credit card payment:", amount)


class UPIPayment(Payment):

    def pay(self, amount):
        print("Processing UPI payment:", amount)


class NetBankingPayment(Payment):

    def pay(self, amount):
        print("Processing net banking payment:", amount)


# Create objects of the child classes.

credit_card = CreditCardPayment()
upi = UPIPayment()
net_banking = NetBankingPayment()

# Call the same method.

credit_card.pay(1000)
upi.pay(2000)
net_banking.pay(3000)


# EXPECTED OUTPUT:
#
# Processing credit card payment: 1000
# Processing UPI payment: 2000
# Processing net banking payment: 3000
#
# IMPORTANT:
#
# Payment defines a common contract.
#
# CreditCardPayment, UPIPayment and NetBankingPayment
# provide their own implementation.
#
# This is abstraction combined with polymorphism.


# ============================================================
# 5. WHY CAN'T WE CREATE AN ABSTRACT CLASS OBJECT?
# ============================================================

# Payment is an abstract class.
#
# It contains an abstract method called pay().
#
# Try this:
#
# payment = Payment()
#
# Python will raise TypeError.
#
# WHY?
#
# Because Payment has an abstract method that has not
# been implemented.
#
# Python expects a concrete child class to implement it.
#
# The child class becomes instantiable after implementing
# all inherited abstract methods.


# ============================================================
# 6. PRACTICAL COMPANY APPLICATION EXAMPLE
# ============================================================

# Imagine ABC Technologies has different types of employees.
#
# Every employee must perform a task.
#
# But the task implementation differs:
#
# Developer     -> Write code
# Analyst       -> Analyze requirements
# Scrum Master  -> Manage sprint
#
# We define a common contract using an abstract class.


class CompanyEmployee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_task(self):
        pass

    def show_name(self):
        print("Employee Name:", self.name)


class CompanyDeveloper(CompanyEmployee):

    def perform_task(self):
        print(self.name, "is developing software")


class CompanyAnalyst(CompanyEmployee):

    def perform_task(self):
        print(self.name, "is analyzing requirements")


class CompanyScrumMaster(CompanyEmployee):

    def perform_task(self):
        print(self.name, "is managing sprint activities")


# Create objects.

developer = CompanyDeveloper("Hari")
analyst = CompanyAnalyst("Ravi")
scrum_master = CompanyScrumMaster("Priya")

# Common method inherited from the parent.

developer.show_name()
analyst.show_name()
scrum_master.show_name()

# Each child provides its own implementation.

developer.perform_task()
analyst.perform_task()
scrum_master.perform_task()


# EXPECTED OUTPUT:
#
# Employee Name: Hari
# Employee Name: Ravi
# Employee Name: Priya
# Hari is developing software
# Ravi is analyzing requirements
# Priya is managing sprint activities


# ============================================================
# 7. UNDERSTANDING @abstractmethod
# ============================================================

# @abstractmethod is a decorator.
#
# A decorator modifies or adds behavior to a function or method.
#
# Here, @abstractmethod tells Python:
#
# "This method must be implemented by a concrete child class."
#
# Example:
#
# @abstractmethod
# def perform_task(self):
#     pass
#
# pass means:
# There is no implementation here.
#
# The child class is responsible for implementing it.


# ============================================================
# 8. ABSTRACTION vs ENCAPSULATION
# ============================================================

# These two concepts are often confused.
#
# ABSTRACTION:
# Hides implementation details and exposes essential operations.
#
# Example:
# You call withdraw(1000).
# You do not need to know the internal transaction process.
#
# ENCAPSULATION:
# Bundles data and methods together and controls access
# to the internal state.
#
# Example:
# A bank account keeps balance inside the class and validates
# deposits and withdrawals before changing it.
#
# MEMORY TRICK:
#
# Abstraction    = Hiding HOW something works.
# Encapsulation  = Protecting HOW data is accessed or changed.


# ============================================================
# 9. ABSTRACTION vs INHERITANCE vs POLYMORPHISM
# ============================================================

# INHERITANCE:
# A child class reuses functionality from a parent class.
#
# Example:
# Developer inherits from Employee.
#
# POLYMORPHISM:
# The same method behaves differently for different objects.
#
# Example:
# Developer.perform_task() writes code.
# Analyst.perform_task() analyzes requirements.
#
# ABSTRACTION:
# Defines what a class must do without specifying
# every implementation detail.
#
# Example:
# Payment requires every payment type to implement pay().
#
# MEMORY TRICK:
#
# Inheritance   = Reuse
# Polymorphism  = Many forms
# Abstraction   = Hide implementation details


# ============================================================
# 10. ABSTRACT CLASS vs NORMAL CLASS
# ============================================================

# NORMAL CLASS:
#
# - Can generally be instantiated.
# - Can contain implemented methods.
# - Child classes may inherit from it.
#
# ABSTRACT CLASS:
#
# - Used to define a common contract.
# - Can contain abstract and normal methods.
# - Cannot be instantiated while abstract methods remain.
# - Concrete child classes must implement inherited
#   abstract methods.


# ============================================================
# 11. CAN AN ABSTRACT CLASS HAVE NORMAL METHODS?
# ============================================================

# YES!
#
# An abstract class can contain:
#   1. Abstract methods
#   2. Normal methods
#   3. Constructors
#   4. Variables and properties
#
# Example:


class EmployeeRules(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

    # Normal method with implementation.

    def company_policy(self):
        print("Follow company policies")


class DeveloperRules(EmployeeRules):

    def work(self):
        print(self.name, "is writing code")


dev = DeveloperRules("Hari")

dev.work()
dev.company_policy()


# EXPECTED OUTPUT:
#
# Hari is writing code
# Follow company policies


# ============================================================
# 12. WHERE IS ABSTRACTION USED IN REAL PROJECTS?
# ============================================================

# 1. PAYMENT SYSTEMS
#    Common payment interface, different payment providers.
#
# 2. DATABASE SYSTEMS
#    Common database operations with different database engines.
#
# 3. NOTIFICATION SYSTEMS
#    Common send() method for email, SMS and Teams.
#
# 4. API DEVELOPMENT
#    Expose API endpoints while hiding internal business logic.
#
# 5. SOFTWARE FRAMEWORKS
#    Define expected methods that developers must implement.
#
# 6. CLOUD APPLICATIONS
#    Expose common interfaces for different cloud services.


# ============================================================
# 13. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is abstraction?
# Answer:
# Abstraction hides implementation details and exposes
# essential functionality.
#
# Q2. How do you implement abstraction in Python?
# Answer:
# Using abstract base classes from the abc module
# and the @abstractmethod decorator.
#
# Q3. What is ABC?
# Answer:
# ABC is a base class provided by Python's abc module
# for creating abstract classes.
#
# Q4. What is @abstractmethod?
# Answer:
# It marks a method that concrete child classes must implement.
#
# Q5. Can we create an object of an abstract class?
# Answer:
# Not while it has unimplemented abstract methods.
#
# Q6. Can an abstract class have normal methods?
# Answer:
# Yes. It can have abstract methods, normal methods,
# constructors and variables.
#
# Q7. Difference between abstraction and encapsulation?
# Answer:
# Abstraction hides implementation details.
# Encapsulation bundles data and methods and controls
# access to internal state.
#
# Q8. Is abstraction related to inheritance?
# Answer:
# Yes. Concrete child classes commonly inherit from
# an abstract base class and implement its abstract methods.


# ============================================================
# 14. PRACTICE EXERCISES
# ============================================================

# EXERCISE 1:
#
# Create an abstract class Vehicle.
#
# Add an abstract method start().
#
# Create child classes:
#   Car
#   Bike
#
# Implement start() differently in both classes.


# EXERCISE 2:
#
# Create an abstract class Shape.
#
# Add an abstract method area().
#
# Create child classes:
#   Circle
#   Rectangle
#
# Implement area() in each child class.
#
# Hint:
# Circle area = 3.14 * radius * radius
# Rectangle area = length * breadth


# EXERCISE 3:
#
# Create an abstract class Notification.
#
# Add an abstract method send(message).
#
# Create child classes:
#   EmailNotification
#   SMSNotification
#   WhatsAppNotification
#
# Implement send() in each class.


# EXERCISE 4:
#
# Create an abstract class Employee.
#
# Add:
#   Constructor for name
#   Normal method show_name()
#   Abstract method perform_task()
#
# Create Developer and BusinessAnalyst child classes.
#
# Implement perform_task() differently.


# ============================================================
# FINAL SUMMARY
# ============================================================

# Imagine using an ATM:
#
# You know WHAT to do:
#   - Insert card
#   - Enter PIN
#   - Withdraw money
#
# You do not need to know HOW the ATM internally
# communicates with the bank or dispenses cash.
#
# That is ABSTRACTION.
#
# In Python:
#   from abc import ABC, abstractmethod
#
#   class Payment(ABC):
#       @abstractmethod
#       def pay(self, amount):
#           pass
#
# ONE-LINE MEMORY TRICK:
#
# ABSTRACTION = SHOW WHAT IS NECESSARY,
#               HIDE HOW IT WORKS INTERNALLY.
#
# ============================================================
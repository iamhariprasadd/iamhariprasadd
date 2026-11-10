
# ==========================================================
# DAY 2: OOP PILLAR 1 - ENCAPSULATION
# ==========================================================

# 1. REAL-WORLD EXAMPLE
#
# Imagine you have a bank account.
#
# Your account balance is Rs. 10,000.
#
# You can:
#   1. Check your balance.
#   2. Deposit money.
#   3. Withdraw money.
#
# But you should not be able to directly change your
# balance to Rs. 10,00,000.
#
# The bank controls how your balance is modified.
#
# This is the basic idea of ENCAPSULATION.
#
# Encapsulation means:
# Combining data (variables) and methods (functions)
# inside a class and controlling how the data is accessed
# or modified.
#
#
# ==========================================================
# 2. WITHOUT ENCAPSULATION
# ==========================================================
#
# Here, balance is publicly accessible.
# Anyone with access to the object can directly change it.
#
# PROBLEM:
# There is no validation before changing the balance.


class BankAccountWithoutEncapsulation:

    def __init__(self, balance):
        self.balance = balance


account1 = BankAccountWithoutEncapsulation(10000)

print("Original Balance:", account1.balance)

# Directly changing the balance
account1.balance = 1000000

print("Updated Balance:", account1.balance)


# OUTPUT:
#
# Original Balance: 10000
# Updated Balance: 1000000
#
# Notice:
# We directly changed the balance.
# There was no validation or control.


# ==========================================================
# 3. WITH ENCAPSULATION
# ==========================================================
#
# Now we will control how the balance is accessed
# and modified.
#
# We will use:
#   __balance  -> Name-mangled attribute
#   get_balance() -> Method to view balance
#   deposit()     -> Method to deposit money
#   withdraw()    -> Method to withdraw money
#
# The methods validate the transactions.


class BankAccount:

    def __init__(self, balance):

        # Double underscore indicates name mangling.
        # It discourages accidental direct access.
        self.__balance = balance

    # Method to view balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):

        if amount > 0:

            self.__balance = self.__balance + amount

            print("Deposit successful!")

        else:

            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal amount!")

        elif amount > self.__balance:

            print("Insufficient balance!")

        else:

            self.__balance = self.__balance - amount

            print("Withdrawal successful!")


# Create bank account object
account2 = BankAccount(10000)

# Check balance
print("Original Balance:", account2.get_balance())

# Deposit money
account2.deposit(2000)

# Withdraw money
account2.withdraw(3000)

# Try invalid deposit
account2.deposit(-500)

# Check final balance
print("Final Balance:", account2.get_balance())


# OUTPUT:
#
# Original Balance: 10000
# Deposit successful!
# Withdrawal successful!
# Invalid deposit amount!
# Final Balance: 9000


# ==========================================================
# 4. UNDERSTANDING UNDERSCORES IN PYTHON
# ==========================================================
#
# Python has different naming conventions.
#
# A. PUBLIC ATTRIBUTE
#
#     self.name = "Ravi"
#
# Meaning:
# Public attribute.
# It can be accessed directly from outside the class.
#
# Example:
# employee.name
#
#
# B. SINGLE UNDERSCORE
#
#     self._salary = 50000
#
# Meaning:
# Conventionally indicates internal use.
# Other developers are advised not to access it directly.
#
# IMPORTANT:
# Python does NOT block access.
#
# Example:
# employee._salary
#
#
# C. DOUBLE UNDERSCORE
#
#     self.__salary = 50000
#
# Meaning:
# Python applies NAME MANGLING.
#
# If the class name is Employee:
#
#     self.__salary
#
# Internally becomes:
#
#     self._Employee__salary
#
# This discourages accidental access and name conflicts.
# It is NOT encryption or absolute security.


# ==========================================================
# 5. NAME MANGLING EXAMPLE
# ==========================================================


class Employee:

    def __init__(self, salary):

        self.__salary = salary


employee = Employee(50000)

# This normally raises AttributeError:
# print(employee.__salary)

# Name-mangled form can still access the attribute:
print(employee._Employee__salary)


# OUTPUT:
#
# 50000


# ==========================================================
# 6. QUICK REVISION
# ==========================================================
#
# name       -> Public attribute
#
# _name      -> Internal-use convention
#
# __name     -> Name-mangled attribute
#
# ENCAPSULATION:
# Keep data and related methods together.
# Control how data is accessed or modified.
# Validate changes through methods when needed.
#
# WITHOUT ENCAPSULATION:
# Direct changes can happen without validation.
#
# WITH ENCAPSULATION:
# Methods provide controlled ways to work with data.
#
# IMPORTANT:
# Double underscore does not make data completely private.
# Python does not provide absolute private access control.
#
# ==========================================================
# END OF ENCAPSULATION NOTES
# ==========================================================

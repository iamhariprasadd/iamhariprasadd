# 1. first Python program
# 2. variables — the storage boxes




# 1. first Python program 
print(" ******************** 1. first Python program *********************** ")
print("Hello, Hari!")
print("I am learning Python for AI.")
print(10 + 20)


# 2. variables — the storage boxes
print(" *********************** 2. variables — the storage boxes *********************** ")
name = "Hari"
price = 249
quantity = 17

print(name)
print(price)
print(quantity)


# 3. = Assignment vs == Comparison
print(" *********************** 3. = Assignment vs == Comparison *********************** ")
price = 249       # Assignment
print("price  : " ,price)
print(price == 249)  # Comparison: True

# 4. 
#Part 4: Data types — what kind of value?
# Python values come in different types.
# Type	  Example	      Used for
# str	  "Hello"	      Text
# int	    25	          Whole numbers
# float    25.5	          Decimal numbers
# bool	   True	          True/false conditions



print(" *********************** 4: Data types — what kind of value? *********************** ")
name = "Hari"
experience = 9
salary = 20.5
is_learning_ai = True

print(type(name))
print(type(experience))
print(type(salary))
print(type(is_learning_ai))



#5. inputs and if else
print(" *********************** #5. inputs and if else? *********************** ")
name = input("ENter Your name  : ")
password = input("ENter Your Password  : ")

if name== "Hari" or  password=="@123":
    print("yes logged IN ");
else : 
    print("Invalid Creditials ")


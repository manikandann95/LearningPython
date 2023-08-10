**Rules for Python variable names**

A variable name can only contain alpha-numeric characters and underscores (ie. A-Z, a-z, 0-9, and _ ).
A variable name cannot start with a number.
Variable names are case-sensitive (age, Age and AGE are three different variables).

**Numeric variables - hold integers and decimal values**
age = 25
temperature = 98.6

**String variables - Stores a sequence of characters enclosed in single or double quotes**
name = "John Doe"
message = 'Hello, world!'

**Boolean variables - only hold the values true and false**
is_true = True
is_false = False

**List variables - Stores a collection of items, which can be of different types.**
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

**Tuple variables**
coordinates = (10, 20)

**Dictionary variables**
person = {'name': 'Alice', 'age': 30}

**Set variables**
unique_numbers = {1, 2, 3}

**None variable**
empty_value = None
    
    The purpose of the **def()** keyword is to define a new function. 

    Best practices for writing code that is **readable and reusable** :

        Create a reusable function - Replace duplicate code with one reusable function to make the code easier to read and repurpose.

        Refactor code - Update code so that it is self-documenting and the intent of the code is straightforward.

        Add comments # - Adding comments is part of creating self-documenting code.

```Python
# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user-provided parameter values. 
print(find_total_days(2,5,23))
```
Maths Priorities:
You can remember by saying **"Please Excuse My Dear Aunt Sally"**

The **comparison operators** include: 

    ==    (equality) 
    !=     (not equal to) 
    >       (greater than)
    <      (less than)
    >=    (greater than or equal to)
    <=    (less than or equal to)

```python
print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
False               # is false. So, Python returns a False value.

print(12/3 == 4)
var = 4.0000000
print(str(var) == str(4)) # is False because the int str value is not as same as the float str
```
**Exponentiate with list comprehension - cubes example**

```Python
# Some random values
values = [
    12, 89, -12.5, 0.443,
    1310, 3110, 125, 54
]

# Raise each number to the power 3
exponents = [pow(value, 3) for value in values]

# Output both lists
print("Original list:\n", values)
print("Raised to the power 3:\n", exponents)
```

The Greater Than > and Less Than < Operators

The comparison operators greater than > and less than < can be used to alphabetize words in Python. 
The letters of the alphabet have numeric codes in Unicode (also known as ASCII values). 

The **uppercase** letters A to Z are represented by the Unicode values **65 to 90.**
The **lowercase** letters a to z are represented by the Unicode values **97 to 122.**
The value for a **space** is **32**
a string **“1”** has a Unicode value of **49** and **“2”** has a Unicode value of **50 and so on**

    To check if the **first letter(s) of a string has a larger Unicode** value (meaning the letter is closer to 122 or lowercase z) than the first letter of another string, use the greater than operator: >

    To check if the **first letter(s) of a string has a smaller Unicode** value (meaning the letter is closer to 65 or uppercase A) than the first letter of another string, use the less than operator: < 

Like numeric comparisons with the greater than > and less than < operators, comparisons between strings also return Boolean True or False results.  

```Python
# comparison is the same as 66 < 98, which is true. So, Python will 
# return a True result.
print("Brown" < "brown")
True
```

Find the ASCII value of any char/str with ord()

```python
c = input (“Enter the number whose ASCII code needs to be found: “)

print (“The ASCII value of given character is”, ord(c))
```
**Lambdas are useful when you need the functionality for a short period of time**. A practical example is filtering a list. Python’s built-in filter method takes two parameters:
    **A filtering function (this is a lambda function)**
    A list to be filtered

As an example, let’s filter even numbers from a list by passing a lambda function into the **filter() method** to check if a number is even:
```Python
numbers = [1, 2, 3, 4, 5, 6]
n = list(filter(lambda x : x % 2 == 0 , numbers))
print(n)
```
**Avoid Infinite Loops and not initializing variables.**

Example of Infinite loop: while loop doesn't change because condition never met. Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

**Common Errors in while Loops**

If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:

    **Failure to initialize variables**. Make sure all the variables used in the loop’s condition are initialized before the loop.

   ** Unintended infinite loops.** Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by adding end criteria to the condition part of the while loop.

 
**while Loop Terms**

    **while loop** - Tells the computer to execute a set of instructions while a specified condition is True. In other words, while loops keep executing the same group of instructions until the condition becomes False.

    **infinite loop** - Missing a method for exiting the loop, causing the loop to run forever.

    **break** - A keyword that can be used to end a loop at a specific point. 
    **continue** - A keyword used to skip an iteration in the loop at a specific case.

Try to recall how Python interprets the truth of a condition, and note that these two forms are equivalent:

while number != 0: and while number:.

The condition that checks if a number is odd can be coded in these equivalent forms, too:

if number % 2 == 1: and if number % 2:.

Classes and Instances

    Classes define the behavior of all instances of a specific class.

    Each variable of a specific class is an instance or object.

    Objects can have attributes, which store information about the object.

    You can make objects do work by calling their methods.

    The first parameter of the methods (self) represents the current instance.

    Methods are just like functions, but they can only be used through a class.

Special methods

    Special methods start and end with __.

    Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.

Documenting classes, methods and functions

    You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:
'''Python
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function
'''

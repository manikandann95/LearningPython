    The purpose of the **def()** keyword is to define a new function. 

    Best practices for writing code that is **readable and reusable**:

        Create a reusable function - Replace duplicate code with one reusable function to make the code easier to read and repurpose.

        Refactor code - Update code so that it is self-documenting and the intent of the code is clear.

        Add comments # - Adding comments is part of creating self-documenting code. 
        Using comments allows you to leave notes to yourself and/or other programmers to make the purpose of the code clear.

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

# LearningPython
My Journey of Python Learning from Scratch

#GoogleITAutomation Course from #Coursera


Commas separate the arguments. We've surrounded them with spaces to make them more visible, but it's unnecessary, and we won't be doing it anymore.

```python
print("'Greg's book.'") 
print('"Greg's book."')
```
These are not the same.

A literal is data whose values are determined by the literal itself. Ex: int, str

For example, the number eleven million one hundred eleven thousand one hundred eleven. If you took a pencil in your hand right now, you would write the number like this: 11,111,111, or like this: 11.111.111, or even like this: 11 111 111.

This provision makes it easier to read, especially when the number consists of many digits. However, Python doesn't accept things like these. It's prohibited. What Python does allow, though, is the **use of underscores in numeric literals**.* **ex: 11_111_111 or simply 11111111** 
Note: Python 3.6 has introduced underscores 

**Octal and hexadecimal numbers**
integer number is preceded by an 0O or 0o prefix (zero-o)
ex: **0o123 is an octal number** with a (decimal) value equal to **83**.

Hexa decimal numbers should be preceded by the prefix 0x or 0X (zero-x).

**0x123** is a hexadecimal number with a (decimal) value equal to **291**
```python
print(0x123) #output provides integer value of hexadecimal i.e. 291
print(0o123) #Output provides integer value of Octal i.e. 83
```
Can write value 0.4 as: **.4**
Also can write the value of 4 as **4.**

Scientific Notation : 3 x 10<sup>8<\sup> as **3e8** or **3E8**

```Python
print(0.0000000000000000000001) #Output would be : 1e-22
```

1. Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").

2. The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number comprises 0s and 1s only, e.g., 1010 is 10 in decimal.
Similarly, octal and hexadecimal numeration systems employ 8 and 16 as their bases. The hexadecimal system uses decimal numbers and six extra letters.

3. Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., 256, or -1 (negative integers).

4. Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or can contain) a fractional component, e.g., 1.27.

5. To encode an apostrophe or a quote inside a string, you can either use the escape character, e.g., 'I\'m happy.', or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, and 'He said "Python", not "typhoon"' to encode a (double) quote.

6. Boolean values are the two constant objects True and False used to represent truth values (in numeric contexts 1 is True, while 0 is False.

**The None literal**. This literal is a NoneType object, and it is used to represent the absence of a value.

The result produced by the division operator is **always a float** But this is not the case in  Floor Division / Multiplication / Addition, if both are integers, the result is also an integer.

In **Floor Division**, rounding always goes to the **lesser integer**.

How **Modulo** Works:

This is why: example **(14 % 4)**

    14 // 4 gives 3 → this is the integer quotient;
    3 * 4 gives 12 → as a result of quotient and divisor multiplication;
    14 - 12 gives 2 → This is the remainder.

```Python
print(12 % 4.5) #Result is in fraction
```

Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted **from left to right.**
**exponentiation** operator **uses the right-sided binding.**

**Priority 	Operator**
1 	        ** 	(exponentiation)
2 	        +, - (note: unary operators located next to the right of the power operator bind more strongly) 	unary
3 	        *, /, //, % 	
4 	        +, - 	binary

1. An expression is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.

2. Operators are special symbols or keywords which can operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others - the hierarchy of priorities:

    the ** operator (exponentiation) has the highest priority;
    then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example, 4 ** -1 equals 0.25)
    then: *, /, and %,
    and finally, the lowest priority: binary + and -.

7. Subexpressions in **parentheses are always calculated first**, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.

```python
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) #Outputs are -0.5 0.5 0 -1 (because floor division takes a lesser integer (-0.5 ~ -1))
print((2 % -4), (2 % 4)) #Outputs are -2 2 (Because 4 * 0 = 0 and remainder is  2)
```


These **variable** names are also correct:

**_** This is also a variable

**Adiós_Señora
    sûr_la_mer
    Einbahnstraße
    переменная.**
    
Python lets you use not only Latin letters but also characters specific to languages that use other alphabets.

**Reserved Keywords**
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'round', 'try', 'while', 'with', 'yield']

But since Python is a case-sensitive lang, we can use **Import**
**Variable:**
The value of a variable is what you have put into it. It can vary as often as you need or want. It can be **an integer one moment, and a float a moment later, eventually becoming a string.**. We don't need to declare in Python.

**Commenting**
```Python
#This program computes the number of seconds in a given number of hours
#This program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour
```
Uncomment : **CTRL + /** (Windows)

 **Type casting (type conversions)**


 String Operations
**add and multiply**
 Add - Concatenation
 Multiply - Replication

Concatenation is not commutative

Replication:
 string * number
number * string

 ```Python
#Simple Square Program
print("+" + 10 * "-" + "+") #
print(("|" + " " * 10 + "|\n") * 5, end = "")
print("+" + 10 * "-" + "+")
```

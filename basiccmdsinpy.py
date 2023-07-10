"""Basic Python print fn and positioning Arguments & Keyword Arguments"""
"Python 3.8 comes with 69 built-in functions"

print("Hello World!")

#print(Hello World) - Invalid sytax error
#print"Hello World" - Parantheses missing error

#print() - Empty print fn. with args gives empty line
# Positioning Args :- Escape Characters print("\n") - New Line
# Escape Characters print("\\") - print esc char \ wihtout any error
# Keyword Args :- 1. print("Hello World",end = " ")
#print("This is Manik") without producing new line, only use space in the end.

print("My","name","is","Manik",sep="-")

print("My", "name", "is", sep="_", end="*") # Underscore comes btn stmts and Ends with *
print("Monty", "Python.", sep="*", end="*\n") # * comes btn Monty and Python

#print(sep="&", "fish", "chips") SyntaxError: positional argument follows keyword argument

#print("'Greg's book.'") will print alright due to 3 quotations
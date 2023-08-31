These are whitespace characters in strings.
● Newline:​ \n
● Space:​ \s 
● Tab:​ \t

A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.

(lambda​ x: x + ​3)(3) # Takes x=3 first and process function as x + 3 = 6.

# List comprehension

l = [(​'Hi'​ + x) ​for​ x ​in​ [​'Alice'​, ​'Bob'​, ​'Pete'​]]
print(l) ​# ['Hi Alice', 'Hi Bob', 'Hi Pete']
l2 = [x * y ​for​ x ​in​ range(​3​) ​for​ y ​in​ range(​3​) ​if​ x>y]
print(l2) ​# [0, 0, 2]

# Set comprehension

squares = { x**​2 ​​for​ x ​in​ [​0​,​2​,​4​] ​if​ x < ​4​ } ​# {0, 4}

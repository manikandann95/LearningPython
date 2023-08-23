'''
    take any non-negative and non-zero integer number and name it c0;
    if it's even, evaluate a new c0 as c0 ÷ 2;
    otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    if c0 ≠ 1, go back to point 2.

The hypothesis says that regardless of the initial value of c0, it will always go to 1.
'''

steps = 0
c0 = int(input("Enter Natural Number : "))

while (c0 <= 0):
    c0 = int(input("Please enter the natural number : "))
while (c0 != 1):
    if c0 % 2 == 0:
        c0 /= 2
        steps += 1
    else:
        c0 = 3 * c0 + 1
        steps += 1
    if c0 == 1:
        print("steps =",steps)
        break
    
else:
    print("steps = 1")

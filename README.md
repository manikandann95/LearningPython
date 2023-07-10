# LearningPython
My Journey of Python Learning from Scratch

#GoogleITAutomation Course from #Coursera


The arguments are separated by commas. We've surrounded them with spaces to make them more visible, but it's not really necessary, and we won't be doing it anymore.

```python
print("'Greg's book.'") 
print('"Greg's book."')
```
These are not the same.

A literal is data whose values are determined by the literal itself. Ex: int, str

Take, for example, the number eleven million one hundred eleven thousand one hundred eleven. If you took a pencil in your hand right now, you would write the number like this: 11,111,111, or like this: 11.111.111, or even like this: 11 111 111.

It's clear that this provision makes it easier to read, especially when the number consists of many digits. However, Python doesn't accept things like these. It's prohibited. What Python does allow, though, is the **use of underscores in numeric literals**.* **ex: 11_111_111 or simply 11111111** 
Note : Python 3.6 has introduced underscores 

**Octal and hexadecimal numbers**
integer number is preceded by an 0O or 0o prefix (zero-o)
ex: **0o123 is an octal number** with a (decimal) value equal to **83**.

Hexa decimal numbers should be preceded by the prefix 0x or 0X (zero-x).

**0x123** is a hexadecimal number with a (decimal) value equal to **291**
```python
print(0x123) #output provides integer value of hexadecimal i.e. 291
print(0o123) #Output provides integer value of Octal i.e. 83
```

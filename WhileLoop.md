The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by **break**

Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:

https://skillsforall.com/content/pe1/1.0/m3/course/en-US/assets/3fe9e03670b96fc65999f8d7ba1a478ac1812790.png
![image](https://github.com/manikandann95/LearningPython/assets/24749083/a07fa7f2-8649-4776-8dc7-34f9f5474931)

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
**Note:** the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
Test your code using the data we've provided.

Sample input:6
Expected output: The height of the pyramid: 3
Sample input: 20
Expected output: The height of the pyramid: 3
Sample input: 1000
Expected output: The height of the pyramid: 44
Sample input: 2
Expected output: The height of the pyramid: 1

```Python
blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1
while layer <= blocks: #Top-Down Block Arrangements
    height += 1 #1 Layer completion
    blocks -= layer #Used Blocks is removed from Block Count
    layer += 1 #Increasing Layer

print("The height of the pyramid:", height)
```

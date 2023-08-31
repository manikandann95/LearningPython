Compiler: Languages like C, C++, Go and Rust, feds the source code into the compiler, which is Architecture specific. The compiler translates this code into Machine Language. Then computer reads and executes the program.
But in this, the compilation process takes time. 
Programs written in interpreted language generally rely on an intermediatory program called an **interpreter**. 
The tradeoff is that interpreted languages generally run slower than the compiled ones. Python, Ruby, Javascript, **bash**, and **Powershell**
Lastly, C# and Java are mixed up, In this first code get compiled to intermediate code. 
This can run in different OS, the execute code based on OS-specific JVM for Java and common language runtime for C#.

Interpreted Language: 

PIL - Python Image Library for Image processing in python

Pillow and its predecessor, PIL, are the original Python libraries for dealing with images. 
Even though there are other Python libraries for image processing, 
Pillow remains a vital tool for understanding and dealing with images.

in terminal (sudo apt install python3-pip)
PIP - Package Installer for Python

**SYNTAXes : shutil.disk_usage(path) ,   psutil.cpu_percent(interval)  in seconds,  pandas.DataFrame(data, index)**

in python terminal :
```Python
import PIL.Image # Imported sub-module Image from PIL
image = PIL.Image.open("houses.jpg") # opening image: /usr/lib/python3/dist-packages/PIL/Image.py 
print(image.size) # Displays Attribute (size) of an image : (4032,3024)
print(image.format) # Image format : JPEG
```
**PIL Image Rotation in Windows**
```Python
from PIL import Image  
#Open image using Image module  
im = Image.open(r"C:\Users\Manik\Downloads\car.jpg")  
#Show actual Image  
im.show()  
#Show rotated Image  
imim = im.rotate(45)  # Rotates 45 degree clockwise
im.show()
```

pandas library for Data Science
Data Frame is a method in Pandas

Terminal : pip3 install pandas

Installing pandas includes - numpy-1.24.4 pandas-2.0.3 python-dateutil-2.8.2 pytz-2023.3 tzdata-2023.3
Let's create a DataFrame with pandas for Visitors on our site and Errors in the site during the week
```Python
import pandas
visitors = [1235, 3455, 8321, 4357, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame( {"Visitors": visitors, "Errors": errors}, index= ["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)
df["Errors"].mean()

```
**Output:**
     Visitors  Errors
Mon      1235      23
Tue      3455      45
Wed      8321      33
Thu      4357      45
Fri      2345      76

Usually in Linux/ Mac Pipeline Interpreter is named before the filename (python3 Hello_world.py)

If you don't want to use an interpreter every time, you can add (**shebang - #!**) with Interpreter location in the first line of the code and make sure give permission to execute file
chmod +x clas.py
./clas.py 
Open file just like all executable file

```Python
#!/usr/bin/env python3
import pandas
visitors = [1235, 3455, 8321, 4357, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame( {"Visitors": visitors, "Errors": errors}, index= ["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)
df["Errors"].mean()

```

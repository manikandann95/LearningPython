Python provides an abstraction called a module. 
**Modules can be used to organize functions, classes, and other data together in a structured way.**
Internally, modules are set up through separate files containing the necessary classes and functions. 

Python already comes with a bunch of ready-to-use modules. 
All these modules are contained in a group called the Python standard library.
Example : random, datetime (syntax : import module_name)

```Python
import random
print(random.randint(1,10)) # Random integer Value in between 1 to 10

import datetime
now1 = datetime.datetime.now() # now() method which belongs to the datetime class contained within the datetime module
print(type(now1)) # <class 'datetime.datetime'> 
print(now1) # 2023-08-17 10:58:24.076147 Behind the scenes, the print function is calling the __str__ method of the datetime class
print(now1.year()) # 2023 (We can also access the instance through its attributes and methods)
```

```Python
from datetime import datetime

# Now 'datetime' refers to the class, not the module.
now1 = datetime.now()

print(datetime.timedelta(days=28)) # 28 days, 0:00:00
print(day + datetime.timedelta(days=28)) # 2023-09-14 10:58:24.076147 we added 28 days with current date and result came as 14th September
```
The official Python documentation lists all the modules included in the standard library.
Pypi is the Python repository and index of an impressive number of modules developed by Python programmers around the world. 
(https://pypi.org/)

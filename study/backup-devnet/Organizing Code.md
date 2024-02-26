# Python Functions
- Blocks of code that only run when called/referenced
```python
def func1(weekday: str):
	print("Today is " + weekday)

func1("Monday")
```

# Classes
Objects are anything that you want to manipulate or change in code.  Classes are groupings of objects

Works similarly to JS classes

```python
class Number:
	x: int = 10

p1 = Number()
print(p1.x)

# INIT FUNCTION EXAMPLE - CONSTRUCTOR
class Date:
	def __init_(self, month: str, day: int, year: int):
		self.month = month
		self.day = day
		self.year = year

p1 = Date("February", 11, 2022)
print(p1.month)
print(p1.day)
print(p1.year)
```


# Modules
Allow us to import chunks of files into another file using `import` statements

There are many modules built into python, such as `math`, `json`, `yaml`, etc
```python
import math
print(math.sqrt(25))

## OR
import calendar
print(calendar.month(2024, 2))
```

Creating our own module
```python
# modules.py file - can be any filename
def hello(name):
	print("Hello, " + name + "!")

employee1: dict(str, str) = {
	"firstname": "John",
	"lastname": "Smith",
	"location": "United States"
}

# in another file
import modules
modules.hello("John")

# OR import specific dict
from modules import employee1

print(employee1["lastname"])
```
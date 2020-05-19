# Control Statements
Control statements are mechanisms that allow you to control what pieces  of the program are being executed at certain times.

In a program, depending on certain conditions, we want certain sections of code to be executed.

## If Statements
In Python, there is support for a variety of logical conditions
- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`
- Modulo: `a % b`

These condtions can be used within **if statements**

An if statement can be written with the `if` keyword\
E.g. 
```
a = 20
b = 21
if b > a:
    print("b is greater than a")
```

### Indentation
Python uses indentation to define sections or blocks of code.\
Anything within an if-statement should be indented so Python can distinguish each block.

## Elif
The `elif` keyword represents an "else if" logic condition. This will check the condition if the previous conditions were false.

E.g.
```
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
```

## Else
The `else` keyword catches anything that isn't caught by preceding conditions.

E.g.
```
a = 42
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is less than a")
```
## Logical Operators
### And
The `and` keyword is a logical operator that allows you to combine conditional statements\
Just as the name implies, it checks that multiple conditions are true.

E.g
```
a = 23
b = 23
c = 23
if a == b and b == c:
    print("All values are equal")
```

### Or
The `or` keyword is a logical operator that allows you to combine conditional statements.\
It checks that at least one condition is true.

E.g
```
a = 23
b = 23
c = 21
if a == b or b == c:
    print("At least two of the numbers are equal")
```

## Exercises
1. even.py (basic if statement)
2. range.py (logical operators)
2. grade.py (multiple if-elif statements)
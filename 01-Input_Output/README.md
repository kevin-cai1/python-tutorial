# Input & Output
## Output
To print a message to the screen we use the `print()` function.

The `print()` function prints the specified message to the screen.

E.g.
```
    print("Hello")
```
Output:
```
>   Hello
```

## Variables
Variables are containers for storing data values.

A variable is created in Python by assigning a value to it.

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

You can access the value of a variable by referencing the variable by name.

### Setting Variables:
```
x = 5
name = "Kevin"
print(x)
print(name)
```
Output:
```
>   5
>   Kevin
```

## Data Types
Variables can store data of different types, and different types can do different things.
Python has the following built-in data types:
> Text Type: `str`\
> Numeric Types: `int`, `float`, `complex`\
> Sequences Types: `list`, `tuple`, `range`\
> Mapping Type: `dict`\
> Set Types: `set`, `frozenset`\
> Boolean Type: `bool`\
> Binary Types: `bytes`, `bytearray`, `memoryview`

Note: When starting out, you only need to familiarise yourself with `str`, `int`, `float` and `bool`.

- `int`: data type used to represent whole numbers (integers)
- `float`: data type used to represent numbers with fractional parts (decimals)
- `str`: data type used to represent text
- `bool`: data type that can be true or false. Used in logic operations

### Numeric Types
#### Basic Arithmetic
You can perform basic arithmetic on `int` or `float` types in Python using generic arithmetic operators:
- `+` : addition
- `-` : subtraction
- `*` : multiplication
- `/`  : division
- `**` : power of
### Strings
Strings are surrounded by either single quotation or double quotation marks.\
`'hello'` is the same as `"hello"`

You can also combine two strings using the + operator.

E.g.
```
a = "Hello"
b = "World"
print(a + b)
```
Output:
```
>   HelloWorld
```
## Input
Input can be taken from a user using the `input()` function.

The format for this function is: `input(<prompt>)`

E.g.:
```
    x = input("Enter your name: ")
    print(x)
```
Output:
```
>   Enter your name: Kevin
>   Kevin
```
Note: `input()` returns the user input as a string.

## Casting
You can specify or change a type of a variable with casting.
These functions are `int()`, `float()`, `str()`

This is useful when you need variables to be a specific data type for specific operations, e.g. doing arithmetic with an integer. 

# Exercise Order:
1. hello<span>.p</span>y
2. hello_you.py
3. circle_calc.py
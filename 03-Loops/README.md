# Loops
Loops are a basic control structure which allows us to execute sections of code multiple times.

Within Python we will look at the two main types of loops.

## While Loop
While loops are used to execute a block of code repeatedly based on a given condition.\
If this condition becomes false, the loop stops and the program continues execution after the loop block.

E.g.
```
count = 0
while (count < 3):
    print("Hello")
    count = count + 1
```

The conditions within these loops operate same as conditions for `if` statements
## For Loop
`For` loops are used to traverse through sequences. In Python, we can use `for` loops to iterate through lists or arrays.\
Generally in programming, `for` loops are used to iterate through a fixed count. In python this can be done with the use of `range()`

`range()` is a function that gives a sequence of numbers between a range

E.g.
```
for x in range(5):
    print("Hello")
```
Note: this will print "Hello" 5 times

```
for x in range(5):
    print(x)
```
Note: this will print out the numbers 1, 2, 3, 4, 5
## Break
`break` is used to exit a loop.
## Continue
`continue` is used to skip the current loop and go back to the top of the loop.

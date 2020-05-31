# Creating an array
array = []
array1 = [1, 2, 3, 4]
array2 = ["hello", "hi", "asdfa"]
var1 = 1
var2 = 2
var3 = 3
array3 = [var1, var2, var3]

print(array)
print(array1)
print(array2)

# Appending to array
array.append(1)
array.append(4)

i = 0
while (i < 5):
    array.append(i)
    i += 1

print(array)

# Removing from array
# remove() and pop()

array.remove(4)
print(array)

array.pop(3)
print(array)

# Length of array
length = len(array)

# Looping through arrays
i = 0
while (i < len(array)):
    print(array[i])
    i += 1

print("FOR LOOP")
for i in array:
    print(i)
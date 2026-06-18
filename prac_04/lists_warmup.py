numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])
print(numbers[-1])
print(numbers[:-1])
print(numbers[3:4])
print(numbers.index(5))
# print(numbers.index(7)) not in list therefore ValueError message
print(5 in numbers)
# print(numbers.index("3")) the string '3' is not in list therefore ValueError
print(7 in numbers)
print(numbers + [6, 5, 3])
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
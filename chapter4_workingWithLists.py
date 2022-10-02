motorcycles = ["Romet", "aAbb", 'simson', 'MZ', "suzuki"]
for m in motorcycles:
    print(m)
for i in range(0, 5):
    print(i)
numbers = list(range(1, 5))
print(numbers)
numberStep = list(range(1, 7, 2))
print(numberStep)

squares = []
for v in range(1, 4):
    x = v**2
    squares.append(x)
print(squares)
print(min(squares))
print(sum(squares))
squares = [value**2 for value in range(1, 11)]  # in lines
print(squares)
split = squares[1:-1]  # like for RANGE omit last value in list
print(split)
split = squares[1:]  # all
print(split)

for x in squares[1:0]:  # same as for range
    x=x

squares_copy = squares[:]

# Tuples
dims = (1, 2)  # tuples are unchangeable
# dims[0] = 3 - this kind of assignment is not allowed
dims = (3, 4)
print(dims)
print(len(dims))
tuplesInList = [(1, 2), (3, 4, 5), (6, 7)]
print(tuplesInList)

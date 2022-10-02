name = input("Please enter name: ")
name = f"Hello {name}"

age = input("Enter age:")
age = int(age)
if age >= 18:
    message = "All fine"
else:
    message = "You are under"

# operator modulo
message = 7.5 % 5
if age % 2 == 0:
    message = f"age {age} is even"
else:
    message = f"age {age} is odd"

# while Loops
number = 1
while number <= 5:
    message = message + str(number)
    number += 1

inpString = ""
while inpString != "quit":
    inpString = input()
    if inpString != "quit":
        print(f"You enter: {inpString}\nYou are still in loop.")

# using break in loop
inpString = ""
while True:
    inpString = input()
    if inpString != "quit":
        print(f"You enter: {inpString}\nYou are still in loop.")
    else:
        break

# using loop to move items from one list to another
sourceList = ["cat", "dog", "cat", "fish"]
destinationList = []
while sourceList:
    destinationList.append(sourceList.pop())

# keep loop running until there is cat is list
while "cat" in destinationList:
    destinationList.remove("cat")

printVal = destinationList
print(printVal)


import chapter9_classes
import chapter10_filesAndExceptions as chapter10
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


my_dog = chapter9_classes.Dog("psiabik", 3)
print(my_dog.name)

myTesla = chapter9_classes.ElectricCar('elec', "electr", 2021)
myTesla.battery.describe_battery()
print(myTesla.battery.get_range())

chapter10.openFileHandleErrorSilent()

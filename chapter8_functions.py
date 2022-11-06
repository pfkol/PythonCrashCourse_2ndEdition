import chapter2_variables
from chapter3_lists import motorcycles
from chapter3_lists import moto_sorted as moto
from chapter3_lists import *  # import all functions

# func without params and return
def hello():
    print("Hello world")


# func with one param - you can put ="Default" to pas Default as a name if it not given then func is called
def helloName(name):
    print(f"Hello {name.title()}")


def nameFirstLast(name, lastName):
    return f"name: {name.title()}, last name: {lastName.title()}"

def nameFirstLast2(name, lastName):
    return {'name': name, 'last': lastName}


def person(name, lastName, age=None):
    if age:
        return {'name': name, 'last': lastName, 'age': age}
    else:
        return {'name': name, 'last': lastName}

# arbitrary number of params store as a tuple
def pizza(*toppings):
    """pizza func with """
    for topping in toppings:
        print(f"{topping}")

# we can mixing positional and arbitrary
def pizza(size, *toppings):
    print(f"making {size} -inch size")
    for topping in toppings:
        print(f"{topping}")


def personBuild(first, last, **person_info):
    # we can manipulate **
    person_info['first name'] = first
    person_info['last name'] = last
    print(person_info)


helloName("Piotr")
helloName(name="Piotr")  # if there is multiple args we can call func with params names
print(nameFirstLast("Piotr", "Kolodziej"))
print(nameFirstLast2("Piotr", "Kolodziej"))
print(person("Piotr", "Kolodziej", 25))
pizza(12, "pep", "onion")
personBuild("Pio", 'Kolodz', localization="Wroclaw", street="gradowa")

print(chapter2_variables.string1)
print(motorcycles)
print(moto)

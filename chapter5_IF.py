cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car in ('audi', 'bmw'):
        print(car.upper())
    elif car == "subaru":
        print(car.lower())
    else:
        print(car.title())

age1, age2, age3 = 18, 30, 33
if age3 >= age2 and age1 != age2:  # => this causing error
    print("all conditions are meet")
else:
    print("not all")
if age3 >= age2 or age1 != age2:
    print("all conditions are meet")

users = ['andrew', 'carolina', 'david']
user = "Piotr"
if user not in users:
    print("user is NOT on the list")

emptyList = []
# if list contain at least one item IF return True
if not emptyList:
    print("1 - list is empty")
if emptyList == []:
    print("2 - list is empty")
if not len(emptyList):
    print("3 - list is empty")
if len(emptyList) == 0:
    print("4 - list is empty")

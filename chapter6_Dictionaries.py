alien0 = {'color': "green", "points": 5}
printValue = alien0['color']

alien0['x_position'] = 1
alien0['y_position'] = 100

alien1 = {}  # create empty dict
alien1['color'] = "blue"
alien1['points'] = 3

alien0["points"] = alien0["points"] + 1  # modify value

del alien0["points"]  # del pair in dict

programing_language = {
    1: "C#",
    2: "java",
    3: "Python",
    4: "Python",
}
language = programing_language.get(4, "no key")
# get() handle exception missing key, if default value in not set "None"

combined = ""
for key, value in programing_language.items():
    x = key
    y = value
    combined = combined + f"{x} - {y}\n"

# only for keys, same can be done for values - .values()
combined = ""
for key in programing_language.keys():
    combined = combined + f"{key}\n"

# only for sorted desc unique (set()) values
combined = ""
for key in set(sorted(programing_language.values(), reverse=True)):
    combined = combined + f"{key}\n"


aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
    print("...")

# in dict others objects ca be stored
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
printValue = combined
print(printValue)

string1 = 'single  quotes is fine'
string2 = "also double is fine for strings"
string3 = "to type of quotes is useful when we want to use one of them in string"

string1.title()  # method: first latter is upper
string1.upper()
string1.lower()

combined1 = f"{string1} {string2}"  # this is called f-string - only >=python3.6
combined2 = "{} {}".format(string1, string2)  # for <= python3.5

whiteSpace = " String "
whiteSpace.rstrip().lstrip().strip()  # stripping

# divide two whole numbers/integers give as float
print(3/2)
# underscore in numbers are ignored
underscore = 1_0000_000
x, y, z = 0, 0, 0
print(z)

def readPI():
    with open('files/pi_digits.txt') as file_object:
        contents = file_object.read()
    return(contents)
# with - closes file when its not needed anymore, its better than using open()/close()

def readPILines():
    with open("files/pi_digits.txt") as file_object:
        for line in file_object:
            print(line)
# above func will return blank lines after each line from file
def readPILines2():
    with open("files/pi_digits.txt") as file_object:
        for line in file_object:
            print(line.strip())


def readPILines3():
    with open("files/pi_digits.txt") as file_object:
        lines = file_object.readlines();
    return lines

filename = 'files/pi_digits.txt'
def write2file():
    with open(filename, 'a') as file_object:
        file_object.write("\nabove is PI")


def divideBy0():
    try:
        return 5/0
    except ZeroDivisionError:
        return "can't divide by zero!"


def errorWithElse():
    try:
        ret = 5/1
    except:
        return "can't do that"
    else:
        print("can do something because try block succeed and else can be called")


filename = 'files/pi_digits2.txt' # file not exist
def openFileHandleError():
    try:
        with open(filename) as obj:
            content = obj.read()
    except FileNotFoundError:
        print(f"file '{filename}' doesn't exist")


def openFileHandleErrorSilent():
    try:
        with open(filename) as obj:
            content = obj.read()
    except FileNotFoundError:
        pass # silently handle error

        
def introdue(variable):
    print("Hello, I'm Gittie!")
    try:
        int(variable)
    except ValueError:
        return "Error"
    return "Success"


def add(a, b):
    print(a + b)


def joke():
    print("Why is an egg funny?\nBecause it has a yoke.")ű
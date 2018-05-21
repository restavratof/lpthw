from collections import OrderedDict

# this goes in my test module


def argPreCheck(arg):
    if type(arg) is not dict:
        print("ERROR: Input argument is not a dict!")
        exit(1)

# dictionary sorted by key
def sortByKeys(d):
    print("Sort by Keys:")
    argPreCheck(d)
    s = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    print(f"RESULT: {s}")

def sortByValue(d):
    print("Sort by Values:")
    argPreCheck(d)
    s = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print(f"RESULT: {s}")


def sortByKeyStringLength(d):
    print("Sort by Values:")
    argPreCheck(d)
    s = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
    print(f"RESULT: {s}")
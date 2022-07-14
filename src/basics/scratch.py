# Funktionen

def function1():
    print("no param")

def function1(name):
    print("one param")


function1("egal")

def function2():
    return 42

def function3(*names):
    for element in names:
        print(element)

function3()
function3("Hugo")
function3("A", "B", "C", 42, True)

def function4(p1, p2, p3):
    pass

function4(p2 = 42, p1 = 4711, p3 = True)
# Keyword Argument, **kwargs
def function5(**kwargs):
    print(kwargs["number"])

function5(dies = "Das", number=9, state = False)

def function6(name = "Sawitzki"):
    print(name)

function6()
function6("Hugo")
#function6("Hugo", 42) Syntax-Fehler
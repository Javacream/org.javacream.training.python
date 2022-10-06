name = "Hugo"

def myFunc():
    global name2
    name2 = 'Emil'
    print("in myFunc: " + name)

print("before myFunc: " + name)

myFunc()

print("after myFunc name: " + name)
print("after myFunc:name2 " + name2)

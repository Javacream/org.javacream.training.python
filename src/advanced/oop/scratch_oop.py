# object, str sind immutable objects
# p = object()
# print(p)
# m = "Hugo"
# m.egal = 42

# new style class, erzeugt mutable objects
class Simple:
    pass

s = Simple()
print(s)
s.lastname = "Meier"
s.firstname = "Hugo"
print(f"{s.firstname} {s.lastname}")


names = ["A", "B"]
names[0] = "Hugo"
print(names)

# list ist immutable
# names.egal = 42
# print(names.egal)


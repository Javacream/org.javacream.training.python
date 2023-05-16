def simple(x):
    return x * 2


simpleLambda = lambda x : x * 2


print(simple(2))
print(simpleLambda(21))


names = {"Emil", "Hugo"}

result = filter(lambda name: name + "!", names)
for r in result:
    print(r)
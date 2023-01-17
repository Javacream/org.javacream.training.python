def func1(p1:str) -> int|str:
    if True:
        return p1
    else:
        return 42

print(func1("Hugo"))
print(func1(42))

result: int|str = func1("")
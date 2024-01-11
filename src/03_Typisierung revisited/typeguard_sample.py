from typeguard import typechecked

@typechecked
def add(a: int, b: int) -> int:
    return a + b

print(add(1,4))
print(add(1.5, 6.6))
from contextlib import contextmanager

class MyContextManager:
    def __enter__(self):
        print("entering...")
        return 42
    def __exit__(self, ex_type, ex, ex_trace):
        print(f"in __exit__: {ex_type}")

with MyContextManager() as number:
    print(f"in sequence, {number}")
    #raise Exception("Error")

@contextmanager
def function_based_context_manager():
    print("enter")
    yield ("Hugo")
    print("exit")


with function_based_context_manager() as value:
    print(f"Hello with value {value}")
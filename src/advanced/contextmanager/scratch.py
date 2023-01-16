class MyContextManager:
    def __enter__(self):
        print("entering...")
        return 42
    def __exit__(self, ex_type, ex, ex_trace):
        print(f"in __exit__: {ex_type}")

with MyContextManager() as number:
    print(f"in sequence, {number}")
    raise Exception("Error")
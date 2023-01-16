#https://realpython.com/python-with-statement/

from contextlib import contextmanager
class Hugo:
  def __enter__(self):
    print("in")
    return 42
  def __exit__(self, a, b, c):
    print(f"a {a}")
    print(f"b {b}")
    print(f"c {c}")
  def do_it(self):
    print("do")  
with Hugo() as h:
  #raise Exception("ERROR")
  print(h)

@contextmanager
def function_based_context_manager():
  print("enter")
  yield("HUHU ")
  print("exit")

with function_based_context_manager() as value:
  print("Hello")  
  print(value)
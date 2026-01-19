def demo(params):
    for param in params:
        print(param)

def demo_with_varargs(*params):
    for param in params:
        print(param)
def main():
    values = [1,2,3,4]
    demo(values)
    demo_with_varargs(1,2,3,4)
main()
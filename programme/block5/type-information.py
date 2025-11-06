def demo(l: list):
#    if isinstance(l, list):
        l.append('C')
#    else:
#        e = Exception("demo expects a list!")
#        raise e

def main():
    names = ['A', 'B']
    # names.
    demo(names)
    demo(True)
main()
def print_out(list, str):
    print(list)
    list[1] = "Fritz"
    #list = [1,2]
    str = "changed"
    print(list, str)


def main():
    l = ["Hugo", "Emil"]
    s = "Egal"
    l_copy = l.copy()
    print_out(l_copy,s)
    print(l, l_copy, s)
main()
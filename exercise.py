def print_out(list):
    print(list)
    list[1] = "Fritz"
    print(list)


def main():
    l = ["Hugo", "Emil"]
    print_out(l)
    print(l)
main()
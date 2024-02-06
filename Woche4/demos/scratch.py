#print("Hello", "Moon") # wie geht denn das eigentlich???
#print()
#print(1,2,3,34,5)

# eine Funktion mit variabler Parameterliste
def my_print(*list_to_print):
    for to_print in list_to_print:
        print(to_print)

#my_print("Hello", "World", 42, True)
#my_print()


def my_print_with_header(header, *list_to_print):
    print(f"**** {header} ***")
    for to_print in list_to_print:
        print(to_print)
#my_print_with_header("Demo", "Hello", "World", 42, True)


def my_print_with_header_and_footer(header, footer, *list_to_print):
    print(f"**** {header} ***")
    for to_print in list_to_print:
        print(to_print)
    print(f"**** {footer} ***")

# my_print_with_header_and_footer("Demo-Header", "Demo-Footer", "Hello", "World", 42, True)
    
def my_print(*list_to_print, **options): # ** : Keyworded Arguments
# def my_print(*args, **kwargs): # ** : Eine Namenskonvention in Python
    header = options.get("header")
    footer = options.get("footer")
    indent = options.get("indent")
    print(f"**** {header} ***")
    for to_print in list_to_print:
        print(f"{indent}{to_print}")
    print(f"**** {footer} ***")


my_print("Hello", "World")
my_print("Hello", "World", header = "Demo-Header", footer= "Demo Footer", indent="\t")
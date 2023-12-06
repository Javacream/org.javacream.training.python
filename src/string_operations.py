def main():
    string = "This is a small sentence"
    upper_string = string.upper()
    print(upper_string)
    replaced_string = string.replace('e', 'x')
    print(replaced_string)

    splitted = string.split('e')
    for s in splitted:
        print(s)

    titled_string = string.title()
    print(titled_string)    
main()
def convert_strings_to_length(strings):
    return [len(s) for s in strings]

def application():
    names = ["Hugo", "Fritz", "Andrea"]
    print(convert_strings_to_length(names))

application()
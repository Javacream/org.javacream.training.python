def main():
    def string_list_to_length_list(string_list):
        # Ergebnisliste erstellen und diese durch Iteration über die string_list füllen, wobei für jedes Element die Länges bestimmt wird
        return [len(s) for s in string_list]

    def string_list_to_length_list_with_filter(string_list, starts_with):
        # Ergebnisliste erstellen und diese durch Iteration über die string_list füllen, wobei für jedes Element die Länges bestimmt wird
        return [len(s) for s in string_list if s.startswith(starts_with)]



    names = ["Hugo", "Fritz", "Hannah", "Andrea"]
    #names_length_list = string_list_to_length_list(names)
    names_length_list = string_list_to_length_list_with_filter(names, 'H')
    print(names_length_list)

main()
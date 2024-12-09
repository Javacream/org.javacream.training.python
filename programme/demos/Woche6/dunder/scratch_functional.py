def main():
    def string_to_length(s):
        return len(s)


    def simple_sort_demo(s, criteria_function):
        print(criteria_function(s))

    names = ['Hugo', 'Hannah', 'Eduard', 'Andrea', 'Emil']
    # names.sort(reverse=True, key=string_to_length)
    print(names)
    #simple_sort_demo("Egal", string_to_length)
    # simple_sort_demo("Egal", lambda s : len(s))
    string_to_length_var = lambda s : len(s)
    simple_sort_demo('Egal', string_to_length_var)

if __name__ == '__main__':
    main() 
def main():
    def by_length(s):
        return len(s)
    def by_second_char(s):
        return s[1]
    by_third_char = lambda s : s[2]
    names = ['Hugo', 'Eduard', 'Zoero', 'Andreana']
    # names.sort(key=by_third_char)
    names.sort(key= lambda s: s[3])
    print(names)
if __name__ == '__main__':
    main()
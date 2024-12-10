def by_length(s):
    return len(s)
def by_second_char(s):
    return s[1]
def main():
    names = ['Hugo', 'Eduard', 'Zoe', 'Andreana']
    names.sort(reverse=True, key=by_second_char)
    print(names)
if __name__ == '__main__':
    main()
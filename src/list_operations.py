def main():
    names = ['Hugo', 'Emil', 'Frieda', 'Andrea', 'Sepp']
    names.sort()
    print(str(names))
    names.append('Alfons')
    print(str(names))
    names2 = names
    names2[1] = 'Johann'
    print(names[1])
    names3 = names.copy()
    names3[1] = 'Thomas'
    print(names[1])
    print(names3[1])


main()
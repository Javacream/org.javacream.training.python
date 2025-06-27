def main():
    names = ['Hugo', 'Hannah', 'Fridolin', 'Emil']
    names.sort() # names wird intern umsortiert
    # print(names)
    names = ['Hugo', 'Hannah', 'Fridolin', 'Emil']
    sorted_names = sorted(names)
    # print(names, sorted_names)

    def criterion(name):
        return len(name)
    
    names = ['Hugo', 'Hannah', 'Fridolin', 'Emil']
    names.sort(key=criterion)
    criterion = lambda name: len(name)
    names.sort(key=criterion)
    names.sort(key= lambda name: len(name))
    names.sort(key=len)
    print(names)
    names.sort(key= lambda name: name[1])
    print(names)

if __name__ == '__main__':
    main()
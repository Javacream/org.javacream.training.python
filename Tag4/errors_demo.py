
def main():
    number = input('Nummer angeben: ')
    if number.isdecimal():
        number = int(number)
        print(number * 2)
    else:
        print(f'{number} war keine Zahl ')    
if __name__ == '__main__':
    main()
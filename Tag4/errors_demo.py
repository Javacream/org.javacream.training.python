
def main():
    number = input('Nummer angeben: ')
    try:
        number = int(number)
        print(number * 2)
    except:
        print(f'{number} war keine Zahl ')    
if __name__ == '__main__':
    main()
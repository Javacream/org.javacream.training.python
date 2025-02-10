
def main():
    while True:
        input_string = input('Nummer angeben: ')
        try:
            input_string = int(input_string)
            print(input_string * 2)
            break
        except:
            print(f'{input_string} war keine Zahl, bitte nochmal versuchen ')    
if __name__ == '__main__':
    main()
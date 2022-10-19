import postalCodes

while(True):
    command = input("enter command:")
    if (command == 'exit'):
        break
    elif (command == 'add'):
        postalCodes.add()
    elif (command == 'byCity'):
        postalCodes.searchByCity()
    elif (command == 'byCode'):
        postalCodes.searchByCode()
    else:
        print("unknown command:", command)


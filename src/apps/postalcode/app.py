from postalCodes import *

while(True):
    command = input("enter command:")
    if (command == 'exit'):
        break
    elif (command == 'add'):
        add()
    elif (command == 'byCity'):
        searchByCity()
    elif (command == 'byCode'):
        searchByCode()
    else:
        print("unknown command:", command)


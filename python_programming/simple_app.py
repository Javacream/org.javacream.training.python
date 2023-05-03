def doAddition(numbers):
    sum = numbers[0] + numbers[1]
    printResult("Addition", numbers, sum)
def doSubstraction(numbers):
    diff = numbers[0] - numbers[1]
    printResult("Substraction", numbers, diff)
def doMultiplication(numbers):
    product  = numbers[0] * numbers[1]
    printResult("Multiplication", numbers, product)

def doDivision(numbers):
    quotient  = numbers[0] / numbers[1]
    #printResult("Division", numbers, quotient)

def readStringFromConsole(position):
    inputString = input(f"Bitte die {position} Zahl eingeben: ")
    return inputString

def readTwoStringsFromConsole():
    return (readStringFromConsole("erste"), readStringFromConsole("zweite"))

def convertStringListToNumbers(stringList):
    try: 
        return (int(stringList[0]), int(stringList[1]))
    except:
        print(f"Eine der Eingaben kann nicht in eine Zahl umgewandelt werden, eingabe1={stringList[0]} oder eingabe2={stringList[1]}")        
        return None

def printResult(operation, numbers, result):
    print(f"Das Ergebnis der {operation} von {numbers[0]} und {numbers[1]} ist {result}")

def main():
    validOperations = ("+", "-", "*", "/")
    while (userInput := input("Bitte Kommado eingeben, exit zum beenden oder '+', '-', '*', '/': ")) != "exit":
            if userInput in  validOperations:
                stringList = readTwoStringsFromConsole()
                numbers = convertStringListToNumbers(stringList)
                if (numbers != None):
                    if userInput == '+':
                        doAddition(numbers)
                    elif userInput == '-':
                        doSubstraction(numbers)
                    elif userInput == '*':
                        doMultiplication(numbers)
                    elif userInput == '/':
                        doDivision(numbers)
            else:
                print(f"Unbekannte Eingabe: {userInput}")
main()
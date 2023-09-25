def main():
    s1 = "3"
    s2 =  "1.6" #"one point six"
    n1 = 9
    n2 = 33

    message = s1 + s2
#    print(message)
#
    sum = n1 + n2
#    print(sum)

    #result = s1 + n1
    #print(result)

    #diff = s1 - s2
    diff = n1 - n2
#    print(diff)

    # type conversion using build in functions: str() , int(), float()

    result = s1 + str(n1)
    print(result)
    diff = int(s1) - float(s2)
    print(diff)
main()
even_message = "an even number: "
odd_message = "an odd number: "
numbers = range(1, 10)
finished = False

for i in numbers:
    print ("processing number " , i, ", finished: ", finished)
    if i % 2 == 0:
        print (even_message, i)
    else:
        print (odd_message, i)

finished = True
print ("all numbers processed, finished: ", finished)

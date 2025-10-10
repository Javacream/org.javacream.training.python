number = 0

# indent as syntax, indent = 4 spaces
if number == 0:
    print('number is zero')
    print('done')
else:
    print('number is not zero')

# free indent 
if number == 0:
 print('number is zero')
 print('done')
else:
                    print('number is not zero')
# must be unique per block
if number == 0:
 print('number is zero')
#     print('done') # IndentationError
else:
    print('number is not zero')

# strange error: if-block is terminated, else-Block is dangling
if number == 0:
    print('number is zero')
print('done')
#else:
#    print('number is not zero')

if number == 1:
    print('############# number was one')
print('############# done')
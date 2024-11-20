condition = True
if condition:
    print('Bedingung ist erfüllt')

n1 = 3
n2 = 5

# if number1 > number2:
#     print('n1 > n2')
# else:
#     print('n1 <= n2')

if n1 > n2:
    print('n1 > n2')
elif 2 * n1 > n2:
    print('2*n1 > n2')
elif 3 * n1 > n2:
    print('3*n1 > n2')
else:
    print('n1 <= n2')

if n1 < n2:
    if 2*n1 < n2:
        print('2*n1 < n2')
    else:
        print('2*n1 >= n2')

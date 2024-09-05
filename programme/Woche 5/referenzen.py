def application():
    list1 = ['A', 'B']
    list2 = ['A', 'B']
    list3 = list1

    list2.append('C')
    print(list1)

    list3.append('D')
    print(list1)


application()
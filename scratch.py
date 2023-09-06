print("Hello")
# print ('Hell) -> Syntax-Fehler
# print (Hello) # -> NameError
my_dict = {81373: 'München'}


#my_dict[40444]
#int("Hugo")

#if 40444 in my_dict.keys():
#    print(my_dict[40444])
#else:
#    print("40444 nicht gefunden")

try:
    counter = 1
    city = my_dict[40444]
    print(city)
except:
    print("40444 nicht gefunden")

if True:
    Hello = 42

try: 
    print (Hello) # -> NameError
except:
    print("Hello ist eine unbekannte Variable")



#try: 
#    print ('Hello) # -> SyntaxError
#except:
#    print("Hello ist eine unbekannte Variable")


result = int
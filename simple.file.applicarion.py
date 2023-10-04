try: 
    f = open('./README.md', 'r')
    first_line = f.readline()
    number = int(first_line)
    print(number)
except Exception as e:
    print(e)    
finally:
    try:
        f.close()
    except:
        print('okaish exception')    

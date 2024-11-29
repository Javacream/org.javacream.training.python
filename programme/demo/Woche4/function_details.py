def fn_with_param(**kwargs): # Keyworded args
    for arg in kwargs:
        print(arg)

def main():
    fn_with_param(name='Sawitzki', height=183)
main()
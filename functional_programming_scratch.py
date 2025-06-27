def main():
    def do_something():
        print('doing something...')

    def demo(callback):
        callback()


    do_something()
    x = do_something
    x()
    demo(do_something)

    lambda_demo = lambda p1, p2: print(p1, p2) 
    lambda_demo('hello', 'world')
if __name__ == '__main__':
    main()
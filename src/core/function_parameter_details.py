def fn (p1, p2, *varargs, height, weight):
    print('calling fn')

def main():
    height = 183
    fn('A', 'B', height=height, weight=76.6)
    fn('A', 'B', 1,2,3, height=183, weight=76.6)
main()
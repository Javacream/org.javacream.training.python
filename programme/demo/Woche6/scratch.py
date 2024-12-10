class DataWithReferenceIdentity:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'Data: data={self.data}'
class Foo:
    def __init__(self):
        self.this = 'that'
        self.goo = 'goo'
        self.data = 'Hugo'
class DataWithValueIdentity:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'Data: data={self.data}'
    def __eq__(self, other):
        if isinstance(other, DataWithValueIdentity):
            return self.data == other.data
        else:
            return False

def main():
    def demo_data_with_reference_identity():
        d1 = DataWithReferenceIdentity('Hugo')
        d2 = DataWithReferenceIdentity('Emil')
        d3 = DataWithReferenceIdentity('Hugo')
        d4 = d1
        print(d1 == d2)
        print(d1 == d3)
        print(d1 == d4)
    def demo_str():
        s1 = str('Hugo')
        s2 = str('Emil')
        s3 = str('Hugo')
        s4 = s1
        print(s1 == s2)
        print(s1 == s3)
        print(s1 == s4)
    def demo_data_with_value_identity():
        d1 = DataWithValueIdentity('Hugo')
        d2 = DataWithValueIdentity('Emil')
        d3 = DataWithValueIdentity('Hugo')
        d4 = d1
        a = Foo()
        print(d1 == d2)
        print(d1 == d3)
        print(d1 == d4)
        print(d1 == a)

    print('with reference:')
    demo_data_with_reference_identity()
    print('with str')
    demo_str()
    print('with value')
    demo_data_with_value_identity()

if __name__ == '__main__':
    main()
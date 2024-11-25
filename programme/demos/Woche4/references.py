def add_element_to(data):
    data.append('C')

def change_data(data):
    data = ['Y', 'Z']
    return data


def main():
    demo_set = ['A', 'B']
    print(f'vor aufruf: {demo_set}')
    add_element_to(demo_set)
    print(f'nach aufruf: {demo_set}')
    add_element_to(demo_set.copy())
    print(f'nach aufruf mit copy(): {demo_set}')
    print('done')
    changed = change_data(demo_set)
    print(f'nach aufruf von change_data: {demo_set}, {changed}')

main()
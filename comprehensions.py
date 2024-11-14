def main():
    names = ['Hugo', 'Emil', 'Hannah', 'Andrea']

    result = []
    for name in names:
        if name.startswith('H'):
            result.append(len(name))
    print(result)

    # Jetzt alternativ Einzeiler mit List Comprehension
    result = [len(name) for name in names if name.startswith('H')]
    print(result)
main()
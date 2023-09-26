def print_collection(coll):
    for element in coll:
        print(element)
    # coll = ['Violin', 'Cell', 'Organ']    Stack / Heap?
    coll[1] = 'Piano'
def main():
    instruments = ["Guitar", "Bass", "Drums", "Guitar"]
    second_instrument = instruments[1] # index starts with 0
    print("Second instrument: " + second_instrument)
    print_collection(instruments)
    second_instrument = instruments[1] # index starts with 0
    print("Second instrument: " + second_instrument)
main()    
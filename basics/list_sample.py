def main():
    names = ["Hugo", "Emil", "Helga", "Andrea", "Emil"]
    print(names[1]) # -> Emil
    print(names[4]) # -> Emil
    # print(names[42]) # -> out of range
    print(names[-1]) #-> identisch zu names[4]
    names.append("Franz")
    print(len(names))
    for name in names:
        print(name)
    index = 0
    while (index < len(names)):
        name = names[index] 
        print(name)
        index +=1   
main()
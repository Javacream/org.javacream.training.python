def file_read_verbose():
    try:
        file = open("./README.md", 'r')
        lines = file.readlines()
        print(lines)
    except:
        print("an exception occured")
    finally:
        file.close()

def file_read():
    try:
        with open("./READMEE.md", 'r') as file:
            lines = file.readlines()
            print(lines)
    except:
        print("an exception occured")

def main():
    # file_read_verbose()
    file_read()
main()
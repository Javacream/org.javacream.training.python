def main():
    opened_file = open('README.md', 'r') # a = append , w schreiben, t: text, b=binary
    rows = opened_file.readlines()
    for row in rows:
        print(row)
    opened_file.close()    

main()

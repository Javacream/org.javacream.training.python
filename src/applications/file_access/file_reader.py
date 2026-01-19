def main():
    path = 'src/applications/file_access/simple.txt'
    file = open(path, 'rt', encoding='utf-8')
    content = file.read()
    print(content)

main()
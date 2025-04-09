def main():
    with open ("README.md", 'rt', encoding='utf-8') as readme_file:
        lines = readme_file.readlines()
    for line in lines:
        print(line)
main()
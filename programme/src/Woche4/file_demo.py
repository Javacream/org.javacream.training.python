def main():
    readme_file = open ("README.md", 'rt', encoding='utf-8')
    lines = readme_file.readlines()
    readme_file.close()
    for line in lines:
        print(line)
main()
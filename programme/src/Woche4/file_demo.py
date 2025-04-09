def main():
    with open ("README.md", 'rt', encoding='utf-8') as readme_file:
        lines = readme_file.readlines()
    for line in lines:
        print(line)
    with open ("result.txt", 'wt', encoding='utf-8') as result_file:
        result_file.write("Hugo")        
main()
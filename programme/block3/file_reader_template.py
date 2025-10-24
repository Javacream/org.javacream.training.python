try:
    with open('data/README.md', encoding='utf-8') as opened_file:
        content = opened_file.read()
    lines = content.split('\n')
    for line in lines:
        print(line)
except Exception as e:
    print(e)
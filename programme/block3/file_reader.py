try:
    with open('data/README.md', encoding='utf-8') as opened_file:
        lines = opened_file.readlines()
except Exception as e:
    print(e)
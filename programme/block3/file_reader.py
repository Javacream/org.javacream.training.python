try:
    opened_file = open('data/README.md', encoding='utf-8')
    lines = opened_file.readlines()
    opened_file.close()   
except Exception as e:
    print(e)
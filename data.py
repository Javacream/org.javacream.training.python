def main():
    with open('data.txt', 'rt', encoding='utf-8') as file:
        rows =file.readlines()
    print(f'data.txt has {len(rows)} rows')
    content = ''.join(rows)
    content = content.replace('\n', '')
    words = content.split(' ')
    print(f'data.txt has {len(words)} words')
    print(f'data.txt contains {content.count("e")} e chars')
    unique_words = set(words)
    print(f'data.txt contains {len(unique_words)} unique words')
    upper_content = content.upper()
    words = upper_content.split(' ')
    unique_words = set(words)
    print(f'data.txt contains {len(unique_words)} unique words ignoring case')






main()
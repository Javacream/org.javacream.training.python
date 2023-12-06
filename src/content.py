def main():
    with open('content.txt', 'r') as content:
        rows = content.readlines()
        row_count = len(rows)
        print(f'content.txt has {row_count} rows')

main()
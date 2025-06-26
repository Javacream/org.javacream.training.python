def read_raw(path):
    with open(path, 'rt', encoding='utf-8') as file:
        raw_rows = file.readlines()
    return raw_rows

def clean(raw_rows: list[str]):
    rows = [raw_row.replace('\n', '') for raw_row in raw_rows if raw_row.replace('\n', '').strip() != '']
    return rows

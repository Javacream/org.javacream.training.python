import os
import json
def read_lines(path):
    with open(path, 'rt', encoding='utf-8') as people_csv_file:
        rows_with_cr = people_csv_file.readlines()
    rows = []
    for row_with_cr in rows_with_cr:
        rows.append(row_with_cr.replace('\n', ''))
    return rows

def write_data(path, result):
    with open(path, 'wt', encoding='utf-8') as file:
        file.writelines(result)

def check_file_exists(path):
    return os.path.exists(path)


def prepare_dir(dirpath):
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

def write_json(path, data):
    with open (path, 'wt', encoding='utf-8') as file:
        json.dump(data, file)


def read_raw(filename :str):
    with open(filename, encoding='utf-8') as file:
        rows = file.readlines()
        return rows

def clean_data(raw_data :list[str]):
    # Das könnte eine List Comprehension als Einzeiler sein, ich mach aber die ausführliche Umsetzung
    clean_data = list()
    for raw in raw_data:
        if raw != '\n':
            if raw.endswith('\n'):
                clean = raw[:-1] # Letztes Zeichen wegschneiden
            else:
                clean = raw
            clean_data.append(clean)
    return clean_data        

def write_result(result: list[str], filename: str):
    #with open(filename, 'wt', encoding='utf-8') as file:
    #    result = [f'{element}\n' for element in result]
    #    file.writelines(result)
    pass
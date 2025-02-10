filename = './Tag3/shopping_list.txt' 
with open(filename, encoding='utf-8') as file:
    rows = file.readlines()
    #cleaned_rows = [row[:-1] for row in rows if not row == '\n']
    cleaned_rows = []
    for row in rows:
        if not row == '\n':
            row_length = len(row)
            if row[row_length-1] == '\n':                
                shorted_row = row[0:row_length-1]
                cleaned_rows.append(shorted_row)
            else:
                cleaned_rows.append(row)    
        else:
            print('Leerzeile entdeckt!')
    
    shopping_set = set(cleaned_rows)
    print(shopping_set)
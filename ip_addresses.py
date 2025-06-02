with open ('./ip_addresses.csv', 'rt', encoding='utf-8') as file:
    list_of_rows = file.readlines()

list_of_cleaned_rows = []

for row in list_of_rows:
    cleaned_row = row.replace('\n', '')
    list_of_cleaned_rows.append(cleaned_row)

list_of_cleaned_rows = list_of_cleaned_rows[1:]

ip_addresses = []
types = []
status = []
dns_names = []

for data in list_of_cleaned_rows:
    splitted = data.split(',')
    ip_addresses.append(splitted[0])
    types.append(splitted[1])
    status.append(int(splitted[2]))
    dns_names.append(splitted[3])

index = 0
for type in types:
    if not type == 'host':
        types[index] = 'DHCP'
    index = index + 1

# Aktiven IP-Adressen

active_ip_counter = sum(status)

print(f'Anzahl aktiver IP-Adressen: {active_ip_counter} ')
print(f'Anzahl inaktiver IP-Adressen: {len(status) - active_ip_counter} ')



print('done')
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

# Anzahl host / DHCP

host_ips = 0

for type in types:
    if type == 'host':
        host_ips +=1
print(f'Anzahl host: {host_ips} ')
print(f'Anzahl DHCP: {len(types) - host_ips} ')

active_host_ips = 0
index = 0
for type in types:
    if type == 'host' and status[index] == 1:
        active_host_ips += 1
    index += 1

print(f'Anzahl aktiver host: {active_host_ips} ')

index = 0
with open ('inactive_dns_entries.txt', 'at', encoding='utf-8') as result_file:
    for dns_name in dns_names:
        if dns_name != '' and status[index] == 0:
            print(f'DNS-Eintrag {dns_name} ist inaktiv')
            result_file.write(f'DNS-Eintrag {dns_name} ist inaktiv\n')
        index += 1


print('done')
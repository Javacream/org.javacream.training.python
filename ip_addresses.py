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
for ip_type in types:
    if not ip_type == 'host':
        types[index] = 'DHCP'
    index = index + 1

# Aktiven IP-Adressen

active_ip_counter = sum(status)

print(f'Anzahl aktiver IP-Adressen: {active_ip_counter} ')
print(f'Anzahl inaktiver IP-Adressen: {len(status) - active_ip_counter} ')

# Anzahl host / DHCP

host_ips = 0

for ip_type in types:
    if ip_type == 'host':
        host_ips +=1
print(f'Anzahl host: {host_ips} ')
print(f'Anzahl DHCP: {len(types) - host_ips} ')

active_host_ips = 0
index = 0
for ip_type in types:
    if ip_type == 'host' and status[index] == 1:
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

# Doppelte IP-Adressen?

print(len(set(ip_addresses))) # Ein set erkennt Duplikate. Falls also das set der ip_addresses-Liste weniger als 100 Einträge hat, sind Duplikate vorhanden!

# Zur Bestimmung der Duplikate müssen wir das set Element für Element befüllen
ip_addresses_set = set()
for ip_address in ip_addresses:
    if ip_address in ip_addresses_set:
        print(f'Die IP-Adresse {ip_address} ist doppelt vergeben!')
    else:
        ip_addresses_set.add(ip_address)

# Bestimmung der vorhandenen Domänennamen
unique_dns_names = set()
for dns_name in dns_names:
    index_of_first_dot = dns_name.find('.') # Index des ersten Auftretens, sonst 0
    if (index_of_first_dot > 0):
        domain_name = dns_name[index_of_first_dot + 1:]
        unique_dns_names.add(domain_name)
print(f'Vorhndene Domänen-Namen: {unique_dns_names}')
print('done')
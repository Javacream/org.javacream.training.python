def main():
    
    part_prefix = 'DM TEIL1-6:'
    contact_pressure_prefix = 'ANPRESSTIEFE WMT1-6:'
    press_in_pressure_prefix = 'EINPRESSTIEFE WMT1-6:'
    datetime_length = len('2023/12/12 00:11:48 ')
    part_prefix_length = datetime_length + len(part_prefix) + 1
    contact_pressure_prefix_length = datetime_length + len(contact_pressure_prefix) + 2
    press_in_pressure_prefix_length = datetime_length + len(press_in_pressure_prefix) + 2
    with open('Testdatei.txt') as f:
        lines = f.readlines()

    part_id_lines = [line[part_prefix_length:].replace('\n', '') for line in lines if line.count(part_prefix) > 0]
    contact_pressure_lines = [line[contact_pressure_prefix_length:].replace('\n', '') for line in lines if line.count(contact_pressure_prefix) > 0]
    press_in_pressure_lines = [line[press_in_pressure_prefix_length:].replace('\n', '') for line in lines if line.count(press_in_pressure_prefix) > 0]

    result = []
    result.append('part_id, machine_position, contact_pressure, press_in_pressure\n')
    for i in range(len(part_id_lines)):
        part_id_line = part_id_lines[i]
        part_id_line = part_id_line[:len(part_id_line) - 7]
        contact_pressure_line = contact_pressure_lines[i]
        press_in_pressure_line = press_in_pressure_lines[i]
        part_ids = part_id_line.split('*******,')
        contact_pressures = contact_pressure_line.split('\t')
        press_in_pressures = press_in_pressure_line.split('\t')
        for j in range(6):
            result.append(f'{part_ids[j]}, {j + 1}, {contact_pressures[j]}, {press_in_pressures[j]}\n')
    with open('Testdatei.tidy.txt', 'wt') as f:
        f.writelines(result)
main()
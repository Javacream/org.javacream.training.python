data_type = type("Hugo")
print(data_type)

data_type = type('Hugo')
print(data_type)

data_type = type(42)
print(data_type)

data_type = type(4.2)
print(data_type)

# Typumwandlung variable = new_type(old_type)
data_type = type(str(4.2))
print(data_type)

data_type = type(int('42'))
print(data_type)

data_type = type(float('4.2'))
print(data_type)

data_type = type(float('42'))
print(data_type)

# Fehler bei der Typ-Umwandlung
#data_type = type(float('4,2'))
#data_type = type(float('Hugo'))

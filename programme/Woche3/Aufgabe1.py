text = "Das ist ein simple Text"
print(text[::-1])

# Alternativ-Lösung, viel aufwändiger
interval = range(len(text)-1, -1, -1)

reversed_text = ''
for index in interval:
    reversed_text += text[index]
print(reversed_text)
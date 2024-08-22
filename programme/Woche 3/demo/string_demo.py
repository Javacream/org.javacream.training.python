message = 'Hello'
# Nicht vergessen: Strings sind unveränderbar, der Rückgabewert muss genutzt werden
upper_message = message.upper()
print(upper_message)

second_character = message[1]
print(second_character)

for char in message:
    print(char)

# message[1] = 'a'

result = [char for char in message]
print(result)

sentence = '''a quite
long sentence 
spanning multiple
rows
'''

words_list = sentence.split(' ')
print(words_list)


# Intervall-Schreibweise zum Erzeugen eines Sub-Strings oder einer Subliste

print(message[1:3])
print(message[:3])
print(message[3:])
print(message[:]) # ziemlich sinnlos, aber möglich
print(message[-1::-1])

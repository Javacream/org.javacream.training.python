message = 'Hello'


def print_out():
    global message
    local_message = 'World'
    local_message = 'World!'
    message = 'Goodbye'
    print(f'{message} in print_out')
    print(local_message)

print_out()
print(f'{message} in script' )

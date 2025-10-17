actual_number = 0
END = 5
while True:
    actual_number += 1 #  Identisch zu actual_number = actual_number + 1
    if actual_number % 2 != 0:
        continue
    print(f"{actual_number}")
    if actual_number >= END:
        break

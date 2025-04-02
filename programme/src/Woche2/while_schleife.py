condition = True

actual_number = 0
END = 5
while condition:
    actual_number += 1 #  Identisch zu actual_number = actual_number + 1
    print(f"{actual_number}")
    condition = actual_number < END

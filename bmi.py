def calculate_bmi(height, weight):
    bmi = weight / (height*height) * 10000
    return bmi

def main():
    sawitzki_height = 183
    sawitzki_weight = 75.6
    sawitzki_bmi = calculate_bmi(sawitzki_height, sawitzki_weight)
    print(sawitzki_bmi)

main()


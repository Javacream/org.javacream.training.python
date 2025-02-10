def calculate_bmi(height, weight):
    bmi = weight / (height*height) * 10000
    return bmi


if __name__ == '__main__':
    print(f'In bmi.py, __name__ = {__name__}')

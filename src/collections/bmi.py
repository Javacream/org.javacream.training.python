data = [
    ['Hugo', 76.6, 185],
    ['Andrea', 66.6, 166],
    ['Hannah', 57, 176]
]

for person in data:
    name, weight, height = person
    height = height / 100
    bmi = weight/(height**2)
    print(f'{name} with height={height} and weight={weight} has a bmi of {bmi:.2f}')
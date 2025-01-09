name = 'Sawitzki'
height = '183'
height = int(height)
weight= '75.3'
weight = float(weight)
bmi = weight / (height*height)*10000

# Herr Sawitzki hat einen BMI von 22.4
bmi_string = str(bmi)
message = 'Herr ' + name + ' hat einen BMI von ' + bmi_string
print(message)
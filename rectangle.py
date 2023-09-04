# this program calculates the rectangle area

# get data
rectangle_width_string = input("Input width: ")
rectangle_width = int(rectangle_width_string)
rectangle_height = int(input("Input height: "))

# transform data
rectangle_area = rectangle_height*rectangle_width
rectangle_perimeter = 2 * (rectangle_height + rectangle_width)

# output result
print("Area: " + str(rectangle_area))
print("Perimeter: " + str(rectangle_perimeter))

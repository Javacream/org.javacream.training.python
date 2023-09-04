# this program calculates the rectangle area

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def print_result(area, perimeter):
    print("Area: " + str(area))
    print("Perimeter: " + str(perimeter))

def read_heigth():
    return int(input("Input height: "))
    
def read_width():
    rectangle_width_string = input("Input width: ")
    return int(rectangle_width_string)


def main():
    height = read_heigth()
    width = read_width()
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(height, width)
    print_result(area, perimeter)

main()

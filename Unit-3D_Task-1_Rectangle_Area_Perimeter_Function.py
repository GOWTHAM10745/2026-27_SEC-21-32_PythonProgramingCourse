#a python program that defines a function to calculate the area and perimeter of a rectangle (length and breadth as parameters) and returns both values
def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
length = int(input("num1:"))
breadth = int(input("num2:")) 
area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        area = self.length * self.breadth
        return area

    def Perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter


length1 = int(input("Enter the length of the first rectangle :"))
breadth1 = int(input("Enter the breadth of the first rectangle :"))

rect1 = Rectangle(length1, breadth1)

length2 = int(input("Enter the length of the second rectangle :"))
breadth2 = int(input("Enter the breadth of the second rectangle :"))

rect2 = Rectangle(length2, breadth2)

area1 = rect1.Area()
perimeter1 = rect1.Perimeter()
area2 = rect2.Area()
perimeter2 = rect2.Perimeter()

print("Area of first rectangle ", area1)
print("Area of second rectangle ", area2)
print("Perimeter of first rectangle ", perimeter1)
print("Perimeter second rectangle ", perimeter2)

if rect1.Area() > rect2.Area():
    print("\nFirst Rectangle  have more area with area difference :", rect1.Area() - rect2.Area())
else:
    print("\nSecond Rectangle  have more area with area difference :", rect2.Area() - rect1.Area())

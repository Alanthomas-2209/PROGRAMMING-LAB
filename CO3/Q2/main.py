# package calling
from graphics import rectangle, circle
from graphics.threeDgraphics import cuboid, sphere

print(" RECTANGLE ")
length = int(input("Enter the length of the rectangle:"))
breadth = int(input("Enter the breadth of the rectangle:"))
area = rectangle.area(length, breadth)
perimeter = rectangle.perimeter(length, breadth)
print("Area of the rectangle :", area, "Perimeter of the rectangle", perimeter)

print(" CIRCLE ")

radius = int(input("Enter the radius for circle :"))
area = circle.area(radius)
circumference = circle.circumference(radius)
print("Area of the circle :", area, "Circumference of the circle", circumference)

print(" CUBOID ")
length=int(input("Enter the length of the cuboid :"))
width=int(input("Enter the width of the cuboid :"))
height=int(input("Enter the height of the cuboid :"))
area = cuboid.area(length, width, height)
volume = cuboid.volume(length,width,height)
print("surface area of the cuboid :", area, "Volume of the cuboid", volume)

print(" SPHERE ")
radius = int(input("Enter the radius for sphere:"))
area = sphere.area(radius)
volume=sphere.volume(radius)
print("surface area of the sphere :", area, "Volume of the sphere", volume)


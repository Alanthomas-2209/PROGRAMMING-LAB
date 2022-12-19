class compare:

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.area = self.__length * self.__breadth

    def __str__(self):
        print("Area :", self.area)

    def __lt__(self, obj):
        return self.area < obj.area


length1 = int(input("Enter the length of the first rectangle :"))
breadth1 = int(input("Enter the breadth of the first rectangle :"))
rect1 = compare(length1, breadth1)
print(rect1.__str__())

length2 = int(input("Enter the length of the second rectangle :"))
breadth2 = int(input("Enter the breadth of the second rectangle :"))
rect2 = compare(length2, breadth2)
print(rect2.__str__())

if rect1 < rect2:
    print("Area of second rectangle is greater")
else:
    print("Area of first rectangle is greater")

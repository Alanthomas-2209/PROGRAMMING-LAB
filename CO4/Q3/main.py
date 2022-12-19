class compare:

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.area = self.__length * self.__breadth

    def __str__(self):
        print("Area :", self.area)

    def __lt__(self, obj):
        return self.area < obj.area


rect1 = compare(5,6)
print(rect1.__str__())

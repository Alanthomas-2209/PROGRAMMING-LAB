class Time:
    def __init__(self, hour, min, sec):
        self.__hour = hour
        self.__minute = min
        self.__second = sec

    def __add__(self, other):
        s = (self.__second + other.__second) % 60
        m = (self.__minute + other.__minute + int((self.__second + other.__second) / 60)) % 60
        h = (self.__hour + other.__hour + int((self.__minute + other.__minute) / 60)) % 24
        return h, m, s

    def __str__(self):
        print("Time =", self.__hour, ":", self.__minute, ":", self.__second)


hour1 = int(input("Enter the Time in the order of Hour,minute,second respectively:"))
min1 = int(input())
sec1 = int(input())
time1 = Time(hour1, min1, sec1)
print(time1.__str__())

hour2 = int(input("Enter the next Time to add in the order of Hour,minute,second respectively:"))
min2 = int(input())
sec2 = int(input())
time2 = Time(hour2, min2, sec2)
print(time2.__str__())

finTime = time1 + time2
print(finTime)

# print(type(finTime))

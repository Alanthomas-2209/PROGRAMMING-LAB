from math import sqrt

def is_square(n):
    if sqrt(n) == int(sqrt(n)):
        return True
    return False

def is_every_digit_even(n):
    while n > 0:
        d = n%10
        if d%2 == 1:
            return False
        n = n//10
    return True

a = int(input("Start: "))
b = int(input("Stop: "))

req_list = [x for x in range(a, b+1) if is_every_digit_even(x) and is_square(x)]
print(req_list)

import math
def gcd(a, b):

	if (a == 0):
		return b
	if (b == 0):
		return a


	if (a == b):
		return a

	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)
a=int(input("Enter the value a :"))
b=int(input("Enter the value b :"))
print("using math function :",math.gcd(a,b),"\n")

print("Using Euclidean Algorithm :\n")
if(gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
	print('not found')

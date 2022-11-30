num=int(input("Enter nth term :"))
print(0)
a=1
b=1
print(a)
print(b)
fib=a+b
while(fib<=num):
    fib=a+b
    if(fib<=num):
        print(fib)
    a=b
    b=fib



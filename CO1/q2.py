current=int(input("Enter the current year :"))
future=int(input("Enter the final year :"))
for year in range(current,future):
    if((year%4==0 and year%100!=0) or (year%400==0 and year%100==0)):
        print(year)

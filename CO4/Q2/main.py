class Bank:
    # balance
    def __init__(self, acNumber, name, acType, balance):
        self.acNumber = acNumber
        self.name = name
        self.acType = acType
        self.balance = balance

    def dePosit(self):
        amount = int(input("Enter the  amount to deposit :"))
        self.balance += amount
        print("current balance :", self.balance)

    def withDraw(self):
        amount = int(input("Enter the  amount to withdraw :"))
        if self.balance < amount or (self.balance - amount) < 1000:
            print("ERROR....!")
        else:
            self.balance -= amount
            print("Remaining balance :", self.balance)

    def __str__(self):
        print("A/c Number :", self.acNumber, " \n Name :", self.name)
        print("your account type :", self.acType, "\n current balance :", self.balance)


flag = 1
print("OPTIONS \n1. TO Enter the details \n2. To Deposit \n3. To withdraw \n4.To Display")
while flag != 0:
    flag = int(input("Enter your choice :"))
    match flag:
        case 1:
            acNumber = int(input("Enter your A/c Number :"))
            name = input("Enter your name :")
            acType = input("Enter your account type :")
            balance = int(input("Enter your current balance :"))
            user1 = Bank(acNumber, name, acType, balance)
        case 2:
            user1.dePosit()
        case 3:
            user1.withDraw()
        case 4:
            print(user1.__str__())
        case _:
            print("Invalid option ")

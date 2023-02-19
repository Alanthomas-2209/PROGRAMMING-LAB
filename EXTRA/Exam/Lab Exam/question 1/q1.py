def product(list):
    flatlist=[]
    for data in list:
        if type(data)== type(1):
            flatlist.append(data)
        elif type(data) == type(True):
            flatlist.append((data))
        elif type(data)==type(flatlist):
            for line in data:
                if type(line)==type(1):
                    flatlist.append(line)
                elif type(line) == type(True):
                    flatlist.append((line))
        elif type(data) == type(tuple()):
            for tupline in data:
                if type(tupline)==type(1):
                    flatlist.append(tupline)
                elif type(tupline) == type(True):
                    flatlist.append((tupline))
        elif type(data) ==type(set()):
            for setline in data:
                if type(setline)==type(1):
                    flatlist.append(setline)
                elif type(setline) == type(True):
                    flatlist.append((setline))
        elif type(data) == type(dict()):
            li=[]
            li2=[]
            li3=[]
            for dictline in data:
                li.append(dictline)
                if type(data[dictline]) == type(flatlist):
                    li2=data[dictline]
                    # print(li2)
                    for dictline2 in li2:
                        li.append(dictline2)
                elif type(data[dictline])== type(tuple()):
                    li3=data[dictline]
                    # print(li3)
                    for dictline2 in li3:
                        li.append(dictline2)
                elif type(data[dictline]) == type(int()):
                    li.append(data[dictline])
            for data2 in li:
                if type(data2)==type(1):
                        flatlist.append(data2)
            # print(li)
        
    result=1
    print("flatlist")
    print(flatlist)
    for num in flatlist:
        result*=num
    return result
#end of function

list1=[1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'Machine Learning']
result = product(list1)
print(result)            
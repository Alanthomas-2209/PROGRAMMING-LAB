from collections import Counter
string=input("Enter a string :")
list=string.split()
print(Counter(list))

# string=input("Enter the string")
# unique=set(string.split())
# words=string.split()
# count={}
# for word in unique:
#     count[word]=words.count(word)
# print(count)
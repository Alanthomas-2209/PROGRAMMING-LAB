#Generate a list of four digit numbers in a given range with all their digits even and the 
 #number is a perfect square.


from math import sqrt

start = int (input("Enter a starting number ( 4 digit ) : "))
end = int (input("Enter a ending number ( 4 digit ) : "))

numbers = [ elm for elm in range(start,end)  if (int(sqrt(elm))*int(sqrt(elm))) == elm]


new_numbers = [ elm for elm in numbers if all(int(b) %2 == 0 for b in str(elm))]

# for elm in numbers:
#       if all(int(b) %2 == 0 for b in str(elm)):
#         new_numbers.append(elm)



print(new_numbers)
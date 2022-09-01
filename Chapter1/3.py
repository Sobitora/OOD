print(" *** Summation of each digit ***")
number = input("Enter a positive number : ")
sum = 0
for x in number:
    sum += int(x)
print("Summation of each digit =  ",sum,sep="")
inp = input("Enter Input : ").split("/")
l1 = [int(i) for i in inp[0].split(" ")]
l2 = [int(i) for i in inp[1].split(" ")]
l1 = sorted(l1)
for num1 in l1 :
    if len(l2):
        if num1 > l2[0]:
            l2.pop(0)
            print(num1)
    else:
        break
if len(l2):
    for i in l2:
        print("No First Greater Value")
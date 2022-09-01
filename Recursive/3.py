def dec2bin(n,l:list,k):
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
        return
    if n == 0:
        print("0")
        return
    if k == n:
        print("".join(l))
        return 
    if k < n:
        l.append("0")
        dec2bin(n,l,k+1)
        l.pop()
        l.append("1")
        dec2bin(n,l,k+1)
        l.pop()
    return

l = []
num = input("Enter Number : ")
dec2bin(int(num),l,0)
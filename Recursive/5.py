def staircase(k,n):
    if n == (abs(k)-1):
        if k > 0:
            return "_"*(k-n-1)+"#"*(n+1)
        elif k < 0 :
            return "_"*n+"#"*(abs(k)-n)
    if k > 0:
        return "_"*(k-n-1)+"#"*(n+1)+"\n"+str(staircase(k,n+1))
    elif k < 0:
        return "_"*n+"#"*(abs(k)-n)+"\n"+str(staircase(k,n+1))
    else:
        return "Not Draw!"

print(staircase(int(input("Enter Input : ")),0))
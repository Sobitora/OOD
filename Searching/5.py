def minweight(l,box,m,weight):
    b = 0
    for i in l:
        if weight+i <= m :
            weight += i
        else:
            b += 1
            weight = i
    if b+1 == int(box):
        return m
    return minweight(l,box,m+1,0)

inp = input("Enter Input : ").split("/")
inp[0] = [int(i) for i in inp[0].split(" ")]
print(f'Minimum weigth for {inp[1]} box(es) = {minweight(inp[0],inp[1],max(inp[0]),0)}')
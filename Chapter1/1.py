print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split(" ")
h = int(h)
m = int(m)
s = int(s)
sec = (h*60*60)+(m*60)+s
if int(h) < 0:
    print("hh("+str(h)+") is invalid!")
elif int(m) < 0 or int(m) > 59 :
    print("mm("+str(m)+") is invalid!")
elif int(s) < 0 or int(s) > 59 :
    print("ss("+str(s)+") is invalid!")
else:
    if h < 10 :
        h = "0"+str(h)
    if m < 10 :
        m = "0"+str(m)
    if s < 10 :
        s = "0"+str(s)
    print(h,":",str(m),":",str(s)," = ",f"{sec:,}"," seconds",sep="")
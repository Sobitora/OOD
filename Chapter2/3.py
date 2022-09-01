class TorKham:
    def __init__(self) :
        self.words = []
    
    def restart(self) :
        self.words = []
        return "game restarted"
    
    def play(self,word) :
        self.words.append(word)
        if len(self.words) == 1:
            return "'"+word+"' -> "+str(self.words)
        elif self.words[-1][:2].lower() == self.words[len(self.words)-2][-2:].lower():
            return "'"+word+"' -> "+str(self.words)
        else:
            return "'"+word+"' -> game over"

torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
# sf = []
# print(len(sf))
for x in S:
    if x[0] == "P" :
        word = x.split(" ")
        print(torkham.play(word[1]))
    elif x[0] == "R" :
        print(torkham.restart())
    elif x[0] == "X" :
        break
    else :
        print("'"+x+"' is Invalid Input !!!")
        break
    # print(S[-1])
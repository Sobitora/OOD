class translator:

    def deciToRoman(self,num):
        Roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        Deci = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numRoman = ""
        while num != 0:
            for x in range(len(Roman)):
                if num >= Deci[x]:
                    numRoman += Roman[x]
                    num -= Deci[x]
                    break
        return numRoman

    def romanToDeci(self,numRoman):
        Romantran={'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
        sum = 0
        for x in range(len(numRoman)-1):
            if Romantran[numRoman[x]] < Romantran[numRoman[x+1]]:
                sum -= Romantran[numRoman[x]]
            else:
                sum += Romantran[numRoman[x]]
        sum += Romantran[numRoman[-1]]
        return sum

num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
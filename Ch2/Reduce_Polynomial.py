L = input("Order: ")
Len = int(L)
Arr = [0] * (Len + 1)
for i in range(len(Arr)):
    Teem = input()
    Arr[i] = float(Teem)
    
while(True):
    R = input("Root: ")
    Brr = [0] * Len
    Cr = 0
    for i in range(len(Brr)):
        Brr[i] = round((Arr[i] + Cr * float(R)) , 2)
        Cr = Brr[i]
        
    print(Brr)
    Ans = input("Keep Going? (Y/N) ")
    if(Ans != "Y"):
        break
    Len -= 1
    Arr = Brr.copy()
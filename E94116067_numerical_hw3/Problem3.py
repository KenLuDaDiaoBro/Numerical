T = [0 , 3 , 5 , 8 , 13]
D = [0 , 200 , 375 , 620 , 990]
V = [75 , 77 , 80 , 74 , 72]

def Herm (X , F , x):
    
    n = len(X)
    Co = [0] * n
    
    for i in range(n):
        if(i != 0):
            for j in range(5 - i):
                F[j] = (F[j + 1] - F[j]) / (X[j + i] - X[j])
        Co[i] = F[0]
    
    Ans = Co[0]
    Tem = 1
    for i in range(1 , n):
        Tem = Tem * (x - X[i - 1])
        Ans = Ans + Co[i] * Tem
    return Ans
 
X = T.copy()
F = D.copy()
Y = T.copy()
G = V.copy()
print(f"a: {Herm(X , F , 10):.6f} ft , {Herm(Y , G , 10):.6f} ft/s")

X = V.copy()
F = T.copy()
S = Herm(X , F , 55 * 5280 / 3600)
if(S < 0):
    Re = "No"
else:
    Re = "Yes"
print(f"b: {Re}, time: {S:.6f} s")

x = 0
max = 0
for i in range(1000000):
    X = T.copy()
    F = V.copy()
    em = Herm(X , F , x)
    if max < em:
        max = em
    x += 0.00001
print(f"c: {max:.6f} ft/s")
    
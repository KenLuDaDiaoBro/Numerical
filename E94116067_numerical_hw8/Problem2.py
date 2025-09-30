import math

def Gauss(A , B):
    n = len(A)
    for i in range(n):
        for j in range(n):
            pivot = A[i][i]
            if j != i:
                C =  A[j][i] / pivot
                for k in range(n):
                    A[j][k] -= C * A[i][k]
                B[j] -= C * B[i]
                
    for i in range (n):
        B[i] /= A[i][i]
        
    return B  

def y(x):
    return 0.5 * math.cos(x) + 0.25 * math.sin(2 * x)

Start = -1
End = 1
n = 10000
step = (End - Start) / n

x = [(Start + i * step) for i in range(n)]

S1 = sum(1 * step for x in x)
Sx = sum(x * step for x in x) 
Sx2 = sum(x**2 * step for x in x) 
Sx3 = sum(x**3 * step for x in x) 
Sx4 = sum(x**4 * step for x in x)  

Sy = sum(y(x) * step for x in x)
Sxy = sum(x * y(x) * step for x in x)
Sx2y = sum(x**2 * y(x) * step for x in x)

A = [[Sx2 , Sx , S1],
     [Sx3 , Sx2 , Sx],
     [Sx4 , Sx3 , Sx2]]
B = [Sy , Sxy , Sx2y]

Ans = Gauss(A , B)

print(f"a = {Ans[0]:.4f} , b = {Ans[1]:.4f} , c = {Ans[2]:.4f}")
E = sum((y(x) - (Ans[0] * x**2 + Ans[1] * x + Ans[2]))**2 * step for x in x)
print(f"Error: {E:.4f}")

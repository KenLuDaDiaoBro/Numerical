import math

x = [4.0 , 4.2 , 4.5 , 4.7 , 5.1 , 5.5 , 5.9 , 6.3]
y = [102.6 , 113.2 , 130.1 , 142.1 , 167.5 , 195.1 , 224.9 , 256.8]

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

n = len(x)

Sx = sum(x)
Sx2 = sum(x**2 for x in x)
Sx3 = sum(x**3 for x in x)
Sx4 = sum(x**4 for x in x)

Sy = sum(y)
Sxy = sum(x[i] * y[i] for i in range(n))
Sx2y = sum(x[i]**2 * y[i] for i in range(n))

A = [[Sx2 , Sx , n],
     [Sx3 , Sx2 , Sx],
     [Sx4 , Sx3 , Sx2]]
B = [Sy , Sxy , Sx2y]

Ans = Gauss(A , B)

print(f"(a)\na = {Ans[0]:.4f} , b = {Ans[1]:.4f} , c = {Ans[2]:.4f}")
E = sum((y[i] - (Ans[0] * x[i]**2 + Ans[1] * x[i] + Ans[2]))**2 for i in range(n))
print(f"Error: {E:.4f}\n")

lnSy = sum(math.log(y[i]) for i in range(n))
lnSxy = sum(x[i] * math.log(y[i]) for i in range(n))

A = [[Sx , n],
     [Sx2 , Sx]]
B = [lnSy , lnSxy]

Ans = Gauss(A , B)
a = Ans[0]
b = math.exp(Ans[1])
print(f"(b)\na = {a:.4f} , b = {b:.4f}")
E = sum((y[i] - (b * math.exp(a * x[i])))**2 for i in range(n))
print(f"Error: {E:.4f}\n")

lnSx = sum(math.log(x[i]) for i in range(n))
lnSx2 = sum(math.log(x[i])**2 for i in range(n))

lnlnSxy = sum(math.log(x[i]) * math.log(y[i]) for i in range(n))

A = [[lnSx , n],
     [lnSx2 , lnSx]]
B = [lnSy , lnlnSxy]

Ans = Gauss(A , B)
a = Ans[0]
b = math.exp(Ans[1])
print(f"(c)\nn = {a:.4f} , b = {b:.4f}")
E = sum((y[i] - (b * (x[i]**a)))**2 for i in range(n))
print(f"Error: {E:.4f}")

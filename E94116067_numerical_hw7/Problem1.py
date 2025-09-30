A = [
    [ 4 , -1 ,  0 , -1 ,  0 ,  0],
    [-1 ,  4 , -1 ,  0 , -1 ,  0],
    [ 0 , -1 ,  4 ,  0 ,  1 , -1],
    [-1 ,  0 ,  0 ,  4 , -1 , -1],
    [ 0 , -1 ,  0 , -1 ,  4 , -1],
    [ 0 ,  0 , -1 ,  0 , -1 ,  4]
]

b = [0 , -1 , 9 , 4 , 8 , 6]

#Jacobi method
x_k1 = [0 , 0 , 0 , 0 , 0 , 0]

for t in range(1000):
    x_k = x_k1[:]
    for i in range(len(x_k)):
        sigma = 0
        for j in range(len(x_k)):
            if i != j:
                sigma += A[i][j] * x_k[j]
        x_k1[i] = (b[i] - sigma) / A[i][i]

x = [format(i, ".6f") for i in x_k1]        
print(f"Jacobi method:\n{x}\n")

#Gauss-Seidel method
x = [0 , 0 , 0 , 0 , 0 , 0]

for t in range(1000):
    for i in range(len(x)):
        sigma = 0
        for j in range(len(x)):
            if i != j:
                sigma += A[i][j] * x[j]
        x[i] = (b[i] - sigma) / A[i][i]

x = [format(i, ".6f") for i in x]        
print(f"Gauss-Seidel method:\n{x}\n")

#SOR method
x = [0 , 0 , 0 , 0 , 0 , 0]
w = 1.2

for t in range(1000):
    for i in range(len(x)):
        sigma = 0
        for j in range(len(x)):
            if i != j:
                sigma += A[i][j] * x[j]
        x[i] = (1 - w) * x[i] + (b[i] - sigma) * w / A[i][i]
        
x = [format(i, ".6f") for i in x]
print(f"SOR method:\n{x}\n")

# Conjugate Gradient Method
x = [0 , 0 , 0 , 0 , 0 , 0]
r = [0 , 0 , 0 , 0 , 0 , 0]
p = [0 , 0 , 0 , 0 , 0 , 0]

for i in range(len(x)):
    sigma = 0
    for j in range(len(x)):
        sigma += A[i][j] * x[j]
    r[i] = b[i] - sigma
p = r.copy()

for t in range(1000):
    U = 0
    L = 0
    Ap = [0 , 0 , 0 , 0 , 0 , 0]
    for i in range(len(x)):
        U += r[i] * r[i]
        for j in range(len(x)):
            Ap[i] += A[i][j] * p[j]
        L += p[i] * Ap[i]
    if L == 0:
        break
    ak = U / L

    for i in range(len(x)):
        x[i] += ak * p[i]

    r_new = [r[i] - ak * Ap[i] for i in range(len(x))]
    if max(abs(x[i] - x_k1[i]) for i in range(len(x))) < 0.0006:
        break

    U_new = sum(r_new[i] * r_new[i] for i in range(len(x)))
    bk = U_new / U

    for i in range(len(x)):
        p[i] = r_new[i] + bk * p[i]
        r[i] = r_new[i]

x = [format(i, ".6f") for i in x]
print(f"Conjugate gradient method:\n{x}\n")
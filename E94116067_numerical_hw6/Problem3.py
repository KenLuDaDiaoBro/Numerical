A = [[3 , -1 , 0 , 0] , [-1 , 3 , -1 , 0] , [0 , -1 , 3 , -1] , [0 , 0 , -1 , 3]]
B = [2 , 3 , 4 , 1]
L = [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
U = [[1 , 0 , 0 , 0] , [0 , 1 , 0 , 0] , [0 , 0 , 1 , 0] , [0 , 0 , 0 , 1]]
x = [0 , 0 , 0 , 0]
y = [0 , 0 , 0 , 0]
n = len(A)

for i in range(n):
    for j in range(n):
        total = 0
        if(i < j):
            for k in range(i):
                total += L[i][k] * U[k][j]
            U[i][j] = round((A[i][j] - total) / L[i][i] , 3)
        else:
            for k in range(j):
                total += L[i][k] * U[k][j]
            L[i][j] = round(A[i][j] - total , 3)
            
for i in range(n):
    total = 0
    for j in range(n):
        total += L[i][j] * y[j]
    y[i] = round((B[i] - total) / L[i][i] , 3)
    
for i in reversed(range(n)):
    total = 0
    for j in range(n):
        total += U[i][j] * x[j]
    x[i] = round((y[i] - total) , 3)
  
for i in range(n):
    print(f"x{i + 1}: {x[i]}")

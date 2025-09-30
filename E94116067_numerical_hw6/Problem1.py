mat = [[1.19 , 2.11 , -100 , 1 , 1.12] , [14.2 , -0.112 , 12.2 , -1 , 3.44] , [0 , 100 , -99.9 , 1 , 2.15] , [15.3 , 0.110 , -13.1 , -1 , 4.16]]
n = len(mat)
for i in range(n):
    max = mat[i][i]
    MaxL = i
    for j in range(i , n):
        if mat[j][i] > max:
            max = mat[j][i]
            MaxL = j
            
    mat[i] , mat[MaxL] = mat[MaxL] , mat[i]
    
    pivot = mat[i][i]
    
    for j in range(n):
        if j != i:
            t = mat[j][i]
            for k in range(len(mat[0])):
                mat[j][k] -= mat[i][k] * t / pivot
                
for i in range(n):
    print(f"x{i + 1}: {round(mat[i][4] / mat[i][i] , 6)}")

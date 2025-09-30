mat = [[4 , 1 , -1 , 0] , [1 , 3 , -1 , 0] , [-1 , -1 , 6 , 2] , [0 , 0 , 2 , 5]]
rev_mat = [[1 , 0 , 0 , 0] , [0 , 1 , 0 , 0] , [0 , 0 , 1 , 0] , [0 , 0 , 0 , 1]]
n = len(mat)
for i in range(n):
    mother = mat[i][i]
    for k in range(n):
        mat[i][k] /= mother
        rev_mat[i][k] /= mother
                
    for j in range(n):
        if j != i:
            kid = mat[j][i]
            for k in range(n):
                mat[j][k] -= kid * mat[i][k]
                rev_mat[j][k] -= kid * rev_mat[i][k]

for i in  range(n):   
    for j in range(n):
        rev_mat[i][j] = round(rev_mat[i][j] , 6)
    print(rev_mat[i])

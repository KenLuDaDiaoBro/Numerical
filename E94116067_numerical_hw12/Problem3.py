import math
import numpy as np
import matplotlib.pyplot as plt

r_min = 0.5
r_max = 1.0
θ_min = 0.0
θ_max = math.pi / 3
h = 0.05
k = math.pi / 30
n = int((r_max - r_min) / h - 1)
m = int((θ_max - θ_min) / k - 1)
alpha = (h / k) ** 2

r = [r_min + i * h for i in range(n + 2)] # 0 ~ n + 1
θ = [θ_min + j * k for j in range(m + 2)] # 0 ~ m + 1
size = n * m
A = [[0.0 for _ in range(size)] for _ in range(size)]
F = [0.0 for _ in range(size)]
U = [0.0 for _ in range(size)]

# Build A F
for i in range(1, n + 1): # 1 ~ n
    for j in range(1, m + 1): # 1 ~ m
        l = i - 1 + n * (j - 1)  # 0 ~ nm - 1
        ri = r[i]
        
        coef1 = alpha  # T_{i,j-1}
        coef2 = ri**2 - (h / 2) * ri  # T_{i-1,j}
        coef3 = -2 * (alpha + ri**2)  # T_{i,j}
        coef4 = ri**2 + (h / 2) * ri  # T_{i+1,j}
        coef5 = alpha  # T_{i,j+1}
        
        # fill A
        if j > 1:  # T_{i,j-1}
            A[l][l - n] = coef1
        if i > 1:  # T_{i-1,j}
            A[l][l - 1] = coef2
        A[l][l] = coef3  # T_{i,j}
        if i < n:  # T_{i+1,j}
            A[l][l + 1] = coef4
        if j < m:  # T_{i,j+1}
            A[l][l + n] = coef5
        # fill F
        F[l] = 0.0
        if j == 1:  # T_{i,0} = 0
            F[l] -= coef1 * 0
        if i == 1:  # T_{0,j} = 50
            F[l] -= coef2 * 50
        if i == n:  # T_{n+1,j} = 100
            F[l] -= coef4 * 100
        if j == m:  # T_{i,m+1} = 0
            F[l] -= coef5 * 0

# Gauss Elimination
for i in range(size):
    max_element = abs(A[i][i])
    max_row = i
    for k in range(i + 1, size):
        if abs(A[k][i]) > max_element:
            max_element = abs(A[k][i])
            max_row = k
    # switch line
    A[i], A[max_row] = A[max_row], A[i]
    F[i], F[max_row] = F[max_row], F[i]

    for k in range(i + 1, size):
        if A[i][i] == 0:
            raise ValueError("No Solution")
        factor = A[k][i] / A[i][i]
        for j in range(i, size):
            A[k][j] -= factor * A[i][j]
        F[k] -= factor * F[i]

for i in range(size - 1, -1, -1):
    if A[i][i] == 0:
        raise ValueError("No Solution")
    U[i] = F[i]
    for j in range(i + 1, size):
        U[i] -= A[i][j] * U[j]
    U[i] /= A[i][i]


T = [[0.0 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        l = i - 1 + n * (j - 1)
        T[i][j] = U[l]
        
# boundry condition
for j in range(m + 2):
    T[0][j] = 50.0
    T[n + 1][j] = 100.0
for i in range(n + 2):
    T[i][0] = 0.0
    T[i][m + 1] = 0.0

print("r\t θ\t T(r,θ)")
for j in range(m + 2):
    for i in range(n + 2):
        print(f"{r[i]:.3f}\t{θ[j]:.3f}\t{T[i][j]:.6f}")
        
R, θ = np.meshgrid(r, θ)
T = np.array(T).T

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(R, θ, T, cmap='viridis')
ax.set_xlabel('r')
ax.set_ylabel('θ')
ax.set_zlabel('T(r,θ)')
ax.set_title('Problem 3')
fig.colorbar(surf, label='T(r,θ)')
plt.tight_layout()
plt.show()
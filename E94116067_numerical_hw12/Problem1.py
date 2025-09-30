import math
import numpy as np
import matplotlib.pyplot as plt

x_min = 0.0
x_max = math.pi
y_min = 0.0
y_max = math.pi / 2
h = 0.1 * math.pi
k = 0.1 * math.pi
n = int((x_max - x_min) / h - 1)
m = int((y_max - y_min) / k - 1)
alpha = (h / k) ** 2

x = [x_min + i * h for i in range(n + 2)]  # 0 ~ n + 1
y = [y_min + j * k for j in range(m + 2)]  # 0 ~ m + 1
size = n * m
A = [[0.0 for _ in range(size)] for _ in range(size)]
F = [0.0 for _ in range(size)]
U = [0.0 for _ in range(size)]

# Build A F
for i in range(1, n + 1):
    for j in range(1, m + 1):
        l = (i - 1) + n * (j - 1)
        xi = x[i]
        yj = y[j]
        
        # fill A
        if j > 1:  # u_{i,j-1}
            A[l][l - n] = 1.0
        if i > 1:  # u_{i-1,j}
            A[l][l - 1] = alpha
        A[l][l] = -2 * alpha - 2  # u_{i,j}
        if i < n:  # u_{i+1,j}
            A[l][l + 1] = alpha
        if j < m:  # u_{i,j+1}
            A[l][l + n] = 1.0
            
        # fill F
        F[l] = h * h * xi * yj
        if j == 1:  # u_{i,0}
            F[l] -= math.cos(xi)
        if i == 1:  # u_{0,j}
            F[l] -= math.cos(yj)
        if i == n:  # u_{n+1,j}
            F[l] -= (-math.cos(yj))
        if j == m:  # u_{i,m+1}
            F[l] -= 0.0

# Gauss Elimination
for i in range(size):
    max_element = abs(A[i][i])
    max_row = i
    for k in range(i + 1, size):
        if abs(A[k][i]) > max_element:
            max_element = abs(A[k][i])
            max_row = k
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

u = [[0.0 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        l = (i - 1) + n * (j - 1)
        u[i][j] = U[l]
        
# boundry condition
for j in range(m + 2):
    u[0][j] = math.cos(y[j])
    u[n + 1][j] = -math.cos(y[j])
for i in range(n + 2):
    u[i][0] = math.cos(x[i])
    u[i][m + 1] = 0.0

print("x\t y\t u(x,y)")
for j in range(m + 2):
    for i in range(n + 2):
        print(f"{x[i]:.3f}\t{y[j]:.3f}\t{u[i][j]:.6f}")
        
X, Y = np.meshgrid(x, y)
U = np.array(u).T

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, U, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x,y)')
ax.set_title('Problem 1')
fig.colorbar(surf, label='u(x,y)')
plt.tight_layout()
plt.show()